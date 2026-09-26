#!/usr/bin/env python3
"""
AI OS Hook Self Test

Corre los hooks de verdad y revisa lo que devuelven. No lee el codigo para
adivinar, ejecuta y mide.

Como correrlo:
    python3 .claude/hooks/test-hooks.py      (Mac e Linux)
    python .claude/hooks/test-hooks.py       (Windows)

Sale con codigo 0 si todo paso, 1 si cualquier caso fallo. Ese codigo de
salida es la prueba: "paso" impreso en pantalla no vale nada si el exit es 1.

EL CASO 3 ES LA RAZON DE QUE ESTE ARCHIVO EXISTA
------------------------------------------------
Solo cuatro caminos le hablan a la IA:
  - SessionStart, UserPromptSubmit, UserPromptExpansion: el stdout del hook
    entra en el contexto del modelo.
  - Stop: no es stdout. Devuelve {"decision": "block", "reason": "..."} y el
    reason se vuelve instruccion.
En cualquier otro evento el print() va al transcript y nadie lo lee. El hook
corre, sale con codigo 0, parece sano, y no hace nada. Este kit ya cometio
ese error dos veces (session-start.py en PreToolUse, session-capture.py en
PreCompact). El caso 3 ejecuta cada hook configurado y reprueba a cualquiera
que escriba en stdout en un evento que no le entrega el stdout a nadie.

Salida sin tildes a proposito: en Windows la consola usa cp1252 y un caracter
con tilde crudo rompe la escritura.
"""
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

HOOKS_DIR = Path(__file__).resolve().parent
VAULT = HOOKS_DIR.parent.parent
SETTINGS = HOOKS_DIR.parent / "settings.json"
SETTINGS_WIN = HOOKS_DIR.parent / "settings-windows.json"

# Eventos cuyo stdout el modelo realmente lee.
STDOUT_CHANNELS = {"SessionStart", "UserPromptSubmit", "UserPromptExpansion"}
# Stop habla por la clave decision, no por stdout suelto.
DECISION_CHANNEL = "Stop"
ALLOWED_EVENTS = STDOUT_CHANNELS | {DECISION_CHANNEL, "SessionEnd"}

results = []


def check(name, passed, evidence):
    results.append((name, passed, evidence))
    print(("PASS  " if passed else "FAIL  ") + name)
    print("      " + evidence)


def run_hook(script, payload, env_extra=None):
    """Corre un hook y devuelve (exit_code, stdout, stderr)."""
    env = dict(os.environ)
    if env_extra:
        env.update(env_extra)
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )
    return proc.returncode, proc.stdout, proc.stderr


def load_events(path):
    """Devuelve [(evento, ruta_del_script)] a partir de un settings.json."""
    out = []
    data = json.loads(path.read_text(encoding="utf-8"))
    for event, groups in data.get("hooks", {}).items():
        for group in groups:
            for hook in group.get("hooks", []):
                cmd = hook.get("command", "")
                for candidate in HOOKS_DIR.glob("*.py"):
                    if candidate.name in cmd:
                        out.append((event, candidate))
    return out


class DailyNote:
    """Guarda y restaura el estado de la nota de hoy, para que la prueba no ensucie el vault."""

    def __init__(self):
        self.path = VAULT / "01 Daily" / f"{date.today().isoformat()}.md"
        self.existed = self.path.exists()
        self.backup = None
        self.mtime = None
        if self.existed:
            self.backup = self.path.read_bytes()
            self.mtime = self.path.stat().st_mtime

    def write_with_age(self, minutes_old):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("prueba\n", encoding="utf-8")
        stamp = time.time() - minutes_old * 60
        os.utime(self.path, (stamp, stamp))

    def remove(self):
        if self.path.exists():
            self.path.unlink()

    def restore(self):
        if self.existed:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_bytes(self.backup)
            os.utime(self.path, (self.mtime, self.mtime))
        else:
            self.remove()


def main():
    print("AI OS Hook Self Test")
    print("vault: " + str(VAULT))
    print("")

    # ---- 1. settings valido, eventos conocidos, scripts existen -----------
    for path in (SETTINGS, SETTINGS_WIN):
        if not path.exists():
            check("settings existe: " + path.name, False, "archivo no encontrado")
            continue
        try:
            events = load_events(path)
        except json.JSONDecodeError as exc:
            check("settings es JSON valido: " + path.name, False, str(exc))
            continue
        check(
            "settings es JSON valido: " + path.name,
            True,
            str(len(events)) + " hook(s): " + ", ".join(e for e, _ in events),
        )
        desconocidos = [e for e, _ in events if e not in ALLOWED_EVENTS]
        check(
            "eventos conocidos: " + path.name,
            not desconocidos,
            "todos previstos" if not desconocidos else "evento inesperado: " + str(desconocidos),
        )

    events = load_events(SETTINGS)

    # ---- 2. todo hook configurado compila --------------------------------
    for event, script in events:
        proc = subprocess.run(
            [sys.executable, "-m", "py_compile", str(script)],
            capture_output=True,
            text=True,
        )
        check(
            "compila: " + script.name,
            proc.returncode == 0,
            "py_compile exit=" + str(proc.returncode)
            + (" " + proc.stderr.strip()[:120] if proc.returncode else ""),
        )

    # ---- 3. el canal existe de verdad (el caso que atrapa el hook muerto) -
    note = DailyNote()
    try:
        for event, script in events:
            # Reinicia ANTES DE CADA hook, no una vez para todo el loop. El
            # session-start.py recrea la nota de hoy cuando corre, asi que un
            # reset unico dejaria al session-capture ver un daily fresco,
            # quedarse callado, y PASAR por no tener nada que decir. Eso es un
            # PASS falso: el caso nunca llega a probar el canal.
            note.remove()
            code, out, _ = run_hook(script, {})
            hablo = bool(out.strip())

            if not hablo:
                check(
                    "canal ok: " + script.name + " en " + event,
                    True,
                    "no escribe en stdout, entrega por archivo o no tiene nada que decir",
                )
            elif event in STDOUT_CHANNELS:
                check(
                    "canal ok: " + script.name + " en " + event,
                    True,
                    str(len(out)) + " chars en stdout, y " + event + " inyecta stdout en el contexto",
                )
            elif event == DECISION_CHANNEL:
                try:
                    payload = json.loads(out)
                    ok = payload.get("decision") == "block" and bool(payload.get("reason"))
                    detalhe = "decision=" + str(payload.get("decision")) + ", reason=" + str(len(payload.get("reason", ""))) + " chars"
                except json.JSONDecodeError as exc:
                    ok, detalhe = False, "stdout no es JSON de decision: " + str(exc)
                check("canal ok: " + script.name + " en " + event, ok, detalhe)
            else:
                check(
                    "canal ok: " + script.name + " en " + event,
                    False,
                    "HOOK MUERTO: escribe " + str(len(out)) + " chars en stdout, pero "
                    + event + " no le entrega el stdout a la IA. Corre, sale con 0, y nadie lo lee.",
                )
    finally:
        note.restore()

    # ---- 4. session-start cabe en el limite de contexto -------------------
    start = HOOKS_DIR / "session-start.py"
    if start.exists():
        note = DailyNote()
        try:
            code, out, err = run_hook(start, {})
            check(
                "session-start inyecta contexto",
                code == 0 and 0 < len(out) < 10000,
                "exit=" + str(code) + ", " + str(len(out)) + " chars (limite de Claude Code = 10000)",
            )
        finally:
            note.restore()

    # ---- 5. guards del session-capture -----------------------------------
    capture = HOOKS_DIR / "session-capture.py"
    if capture.exists():
        note = DailyNote()
        try:
            code, out, _ = run_hook(capture, {"stop_hook_active": True})
            check(
                "guard 1: stop_hook_active corta el loop",
                code == 0 and not out.strip(),
                "exit=" + str(code) + ", stdout=" + str(len(out)) + " chars (esperado 0)",
            )

            note.write_with_age(0)
            code, out, _ = run_hook(capture, {})
            check(
                "guard 2: daily fresco, el hook se queda callado",
                code == 0 and not out.strip(),
                "exit=" + str(code) + ", stdout=" + str(len(out)) + " chars (esperado 0)",
            )

            note.write_with_age(60)
            code, out, _ = run_hook(capture, {})
            try:
                payload = json.loads(out)
                ok = payload.get("decision") == "block"
                detalhe = "daily con 60 min, decision=" + str(payload.get("decision"))
            except json.JSONDecodeError:
                ok, detalhe = False, "daily viejo pero stdout no es JSON: " + repr(out[:80])
            check("guard 2 al reves: daily viejo, el hook cobra", ok and code == 0, detalhe)

            code, out, _ = run_hook(capture, {}, {"AIOS_DOCUMENTING": "1"})
            check(
                "guard 3: AIOS_DOCUMENTING corta la recursion",
                code == 0 and not out.strip(),
                "exit=" + str(code) + ", stdout=" + str(len(out)) + " chars (esperado 0)",
            )

            proc = subprocess.run(
                [sys.executable, str(capture)],
                input="esto no es json",
                capture_output=True,
                text=True,
                timeout=30,
            )
            check(
                "stdin invalido no tumba la sesion",
                proc.returncode == 0 and not proc.stdout.strip(),
                "exit=" + str(proc.returncode) + ", stdout=" + str(len(proc.stdout)) + " chars",
            )

            note.write_with_age(60)
            _, out, _ = run_hook(capture, {})
            no_ascii = [c for c in out if ord(c) > 127]
            check(
                "salida ASCII, aguanta cp1252 en Windows",
                not no_ascii,
                "sin tildes en la salida" if not no_ascii else "caracteres que rompen: " + str(no_ascii[:10]),
            )
        finally:
            note.restore()

    # ---- marcador ---------------------------------------------------------
    print("")
    paso = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    print("=" * 60)
    print("RESULTADO: " + str(paso) + "/" + str(total) + " casos pasaron")
    if paso != total:
        print("")
        print("Fallo:")
        for name, ok, evidence in results:
            if not ok:
                print("  - " + name + ": " + evidence)
    print("=" * 60)
    return 0 if paso == total else 1


if __name__ == "__main__":
    if shutil.which(sys.executable) is None and not Path(sys.executable).exists():
        print("python no encontrado")
        sys.exit(1)
    sys.exit(main())
