#!/usr/bin/env python3
"""
AI OS Session Capture Hook

Dispara en Stop. Le pide a la IA persistir la sesion en el daily antes de que
termine el turno.

POR QUE Stop Y NO PreCompact
----------------------------
Este hook corria en PreCompact, escribiendo el recordatorio con print() y
saliendo con codigo 0. Segun la spec de hooks de Claude Code, solo
UserPromptSubmit, UserPromptExpansion y SessionStart ponen el stdout del hook
en el contexto del modelo. Todo lo demas, PreCompact incluido, manda el stdout
al transcript y nadie lo lee. O sea: el recordatorio se escribia y se leia cero
veces. Es el mismo defecto que hacia que session-start.py no hiciera nada
cuando estaba en PreToolUse.

Stop es el unico evento de ciclo de vida con un canal documentado de vuelta a
la conversacion: devolver {"decision": "block", "reason": "..."} impide la
parada y le entrega el `reason` a la IA como instruccion de que hacer ahora.
El mecanismo es ese, no el stdout.

DOS GUARDS, Y POR QUE EL PRIMERO NO BASTA
-----------------------------------------
1. stop_hook_active. Bloquear el Stop hace que la IA trabaje e intente parar de
   nuevo. Sin este guard se vuelve un loop infinito. El payload trae
   stop_hook_active: true desde el segundo intento DENTRO DEL MISMO TURNO, asi
   que el guard sale con 0 y deja que ese turno termine.

   Atencion: la flag se reinicia en cada turno. El guard 1 evita el loop, no la
   repeticion.

2. Frescura del daily. Disparar en todo turno es ruido, incluso en los turnos
   que acaban de escribir el daily. Entonces, si la nota de hoy se modifico en
   los ultimos FRESH_MINUTES, la sesion ya se esta persistiendo y el hook sale
   callado. El recordatorio solo aparece cuando la persistencia de verdad quedo
   vieja.

Guard anti-recursion: la documentacion automatica de session-end.py llama a
'claude -p' headless, que dispara los hooks de nuevo. AIOS_DOCUMENTING=1 hace
salir temprano.

Salida sin tildes a proposito: en Windows la consola usa cp1252 y un caracter
con tilde crudo rompe la escritura.
"""
import json
import os
import sys
import time
from datetime import date
from pathlib import Path

# Vault root = padre de .claude/hooks/ (sin path absoluto, funciona en cualquier maquina)
VAULT = Path(__file__).resolve().parent.parent.parent

FRESH_MINUTES = 20


def main() -> int:
    # Nunca corre dentro de la propia ronda de documentacion headless.
    if os.environ.get("AIOS_DOCUMENTING") == "1":
        return 0

    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # Sin payload legible no se puede revisar el guard. Quedarse callado es
        # mejor que arriesgar un loop.
        return 0

    if payload.get("stop_hook_active"):
        return 0

    today = date.today().isoformat()

    note = VAULT / "01 Daily" / f"{today}.md"
    try:
        if (time.time() - note.stat().st_mtime) < FRESH_MINUTES * 60:
            return 0
    except OSError:
        # La nota todavia no existe o no se puede leer. Es justo cuando el
        # recordatorio vale, asi que sigue.
        pass

    reason = (
        f"[AI OS Session Capture] Antes de terminar: persiste esta sesion en "
        f"01 Daily/{today}.md.\n\n"
        "Agrega una entrada `## Sesion` con:\n"
        "- **Decisiones tomadas:** decisiones reales de esta sesion\n"
        "- **Lo que se hizo:** acciones concretas realizadas\n"
        "- **Aprendizajes:** que funciono, que fallo, que se descubrio\n"
        "- **Proximos pasos:** acciones pendientes, especificas y con fecha\n\n"
        "Despues enruta el resto al lugar correcto: una decision importante va a "
        "03 Intelligence/decisions/, un estado nuevo de proyecto va a la nota del "
        "proyecto, una correccion que el usuario te dio se vuelve regla permanente "
        "en 02 Context/me.md. Si tienes dudas, consulta AIOS/knowledge-routing.md.\n\n"
        "Si la sesion fue solo conversacion y no hay nada que valga la pena guardar, "
        "dilo en una linea y para. No inventes una entrada para satisfacer el hook."
    )

    json.dump({"decision": "block", "reason": reason}, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
