#!/usr/bin/env python3
"""
AI OS Session Start Hook

Inyecta el contexto central del vault al inicio de cada sesion de Claude Code.

IMPORTANTE: dispara en el evento SessionStart. El stdout de SessionStart SI se
inyecta en el contexto del modelo. El evento antiguo (PreToolUse) NO inyecta el
stdout en el contexto, y por eso el agente parecia "no conectado" aunque el hook
estuviera corriendo.

Reglas de robustez:
- El output siempre por debajo de 10.000 caracteres (limite por hook). Techo de 9.000 aca.
- Sin dependencia de /tmp (no existe en Windows nativo). SessionStart corre una vez
  por sesion, asi que no necesita lock.
- Lectura siempre en utf-8. Toda operacion de archivo tolera fallas sin romperse.
- El vault se detecta por la ubicacion de este archivo, sin rutas absolutas.

Aunque este hook falle (por ejemplo, si no hay python), el agente igual se conecta:
el CLAUDE.md (que Claude Code siempre carga) le indica a la IA leer estos archivos.
"""
import os
import sys
from datetime import date
from pathlib import Path

# Guard anti-recursion: la documentacion automatica de fin de sesion llama a
# 'claude -p' headless, que dispara SessionStart de nuevo. En esa ronda, sale.
if os.environ.get("AIOS_DOCUMENTING") == "1":
    sys.exit(0)

# Consume el stdin del hook (el JSON de SessionStart) sin depender de el.
try:
    sys.stdin.read()
except Exception:
    pass

# Vault root = padre de .claude/hooks/
VAULT = Path(__file__).resolve().parent.parent.parent

CHAR_BUDGET = 9000  # margen de seguridad bajo el limite de 10k por hook


def read_capped(rel_path, limit):
    p = VAULT / rel_path
    if not p.exists():
        return None
    try:
        text = p.read_text(encoding="utf-8")
    except Exception:
        return None
    if len(text) > limit:
        text = text[:limit] + "\n[... truncado, lee el archivo completo si lo necesitas ...]"
    return text


def detect_mode():
    op = VAULT / "02 Context" / "operator.md"
    org = VAULT / "02 Context" / "organization.md"
    return "empresa" if (op.exists() and org.exists()) else "solo"


def latest_daily():
    d = VAULT / "01 Daily"
    if not d.exists():
        return None
    files = sorted(d.glob("????-??-??.md"), reverse=True)
    return files[0] if files else None


def ensure_today_daily():
    today = date.today().isoformat()
    d = VAULT / "01 Daily"
    try:
        d.mkdir(parents=True, exist_ok=True)
        f = d / f"{today}.md"
        if not f.exists():
            f.write_text(
                f"---\ntype: daily\ndate: {today}\nstatus: active\ntags: [daily]\n---\n",
                encoding="utf-8",
            )
    except Exception:
        pass
    return today


header = "[AI OS Session Start] Eres la IA personal que opera este vault. Contexto cargado abajo.\n"
parts = [header]
used = len(header)


def add(block):
    global used
    if used + len(block) < CHAR_BUDGET:
        parts.append(block)
        used += len(block)


# 1. Identidad (prioridad maxima, es lo que hace que el agente "te conozca")
if detect_mode() == "empresa":
    identity = [
        ("02 Context/operator.md", "Operador", 2500),
        ("02 Context/organization.md", "Empresa", 2500),
    ]
else:
    identity = [("02 Context/me.md", "Identidad", 4000)]

for rel, label, lim in identity:
    txt = read_capped(rel, lim)
    if txt:
        add(f"--- {label} ({rel}) ---\n{txt}\n")

# 2. Ultima sesion (continuidad)
ld = latest_daily()
if ld:
    txt = read_capped(ld.relative_to(VAULT).as_posix(), 2000)
    if txt:
        add(f"--- Ultima Sesion ({ld.stem}) ---\n{txt}\n")

# 3. Punteros al resto (la IA los lee bajo demanda)
add(
    "--- Lee bajo demanda ---\n"
    "- AIOS/index.md (skills y comandos disponibles)\n"
    "- AIOS/operating-rules.md (como operar en este vault)\n"
    "- AIOS/knowledge-routing.md (donde guardar cada cosa)\n"
    "- knowledge/index.md (conocimiento permanente)\n"
)

# 4. Garantiza el daily de hoy + la instruccion de documentacion
today = ensure_today_daily()
add(
    f"--- Documentacion ---\n"
    f"La nota de hoy existe en `01 Daily/{today}.md`. Registra ahi las decisiones reales, "
    f"o en `03 Intelligence/decisions/`, a medida que trabajas.\n"
)

sys.stdout.write("\n".join(parts))
