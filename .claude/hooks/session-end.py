#!/usr/bin/env python3
"""
AI OS Session End Hook (documentacion automatica OPT-IN)

Dispara en SessionEnd. Por defecto NO hace nada (salida instantanea, costo cero).
Solo corre si la documentacion automatica esta PRENDIDA, lo que evita dos problemas
que generaban queja: trabar la salida de la sesion y gastar tokens en silencio.

Como prender la documentacion automatica:
  - crea el archivo `AIOS/autodoc.enabled` en el vault, O
  - exporta la variable de entorno AIOS_AUTODOC=1

Cuando esta prendida: lee el transcript, lo resume con Claude headless (claude -p,
timeout de 60s) y lo escribe en 01 Daily/HOY.md. Si el resumen falla, sale en
silencio (no escribe basura).

Guard anti-recursion: la llamada headless de claude dispara los hooks de nuevo.
La variable AIOS_DOCUMENTING=1 (puesta en el subproceso) hace que los hooks salgan temprano.
"""
import json
import os
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

# Nunca corre dentro de su propia ronda de documentacion (evita el loop).
if os.environ.get("AIOS_DOCUMENTING") == "1":
    sys.exit(0)

# Vault root = padre de .claude/hooks/ (sin depender de variables de entorno)
VAULT = Path(__file__).resolve().parent.parent.parent


def autodoc_enabled():
    if os.environ.get("AIOS_AUTODOC") == "1":
        return True
    return (VAULT / "AIOS" / "autodoc.enabled").exists()


# OPT-IN: apagado por defecto. Salida instantanea, nada de claude -p.
if not autodoc_enabled():
    sys.exit(0)


def read_hook_input():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def extract_conversation(path, max_chars=120000):
    """Extrae el texto de user + assistant del transcript JSONL."""
    out = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                msg = obj.get("message") or obj
                role = msg.get("role") or obj.get("type") or ""
                if role not in ("user", "assistant"):
                    continue
                content = msg.get("content")
                text = ""
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            text += block.get("text", "")
                if text.strip():
                    out.append(f"[{role}] {text.strip()}")
    except Exception:
        return ""
    convo = "\n\n".join(out)
    if len(convo) > max_chars:
        convo = "(inicio truncado)\n\n" + convo[-max_chars:]
    return convo


def find_claude():
    c = shutil.which("claude")
    if c:
        return c
    candidates = [
        "/opt/homebrew/bin/claude",
        os.path.expanduser("~/.claude/local/claude"),
        "/usr/local/bin/claude",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None


def summarize(convo):
    claude = find_claude()
    if not claude:
        return None
    prompt = (
        "Resume esta sesion de trabajo para una nota diaria de Obsidian. "
        "Usa exactamente este formato en espanol, conciso y especifico:\n\n"
        "**Decisiones tomadas:** (decisiones reales de esta sesion, o 'ninguna')\n"
        "**Lo que se hizo:** (acciones concretas realizadas)\n"
        "**Aprendizajes:** (que funciono, que fallo)\n"
        "**Proximos pasos:** (acciones pendientes)\n\n"
        "No inventes. Basate solo en lo que esta en la conversacion de abajo.\n\n"
        "=== CONVERSACION ===\n" + convo
    )
    env = dict(os.environ)
    env["AIOS_DOCUMENTING"] = "1"
    try:
        result = subprocess.run(
            [claude, "-p", prompt],
            capture_output=True,
            text=True,
            timeout=60,
            env=env,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except Exception:
        pass
    return None


def write_to_daily(summary):
    today = date.today().isoformat()
    daily_dir = VAULT / "01 Daily"
    try:
        daily_dir.mkdir(parents=True, exist_ok=True)
        daily_path = daily_dir / f"{today}.md"
        ts = datetime.now().strftime("%H:%M")
        if not daily_path.exists():
            daily_path.write_text(
                f"---\ntype: daily\ndate: {today}\nstatus: active\ntags: [daily]\n---\n",
                encoding="utf-8",
            )
        entry = f"\n\n## Sesion {ts}\n\n{summary}\n"
        with open(daily_path, "a", encoding="utf-8") as f:
            f.write(entry)
    except Exception:
        pass


def main():
    hook = read_hook_input()
    transcript_path = hook.get("transcript_path", "")

    if not transcript_path or not os.path.exists(transcript_path):
        sys.exit(0)

    convo = extract_conversation(transcript_path)
    if not convo.strip():
        sys.exit(0)

    summary = summarize(convo)
    if not summary:
        # Fallo: sale en silencio en vez de ensuciar el daily con un placeholder.
        sys.exit(0)

    write_to_daily(summary)


if __name__ == "__main__":
    main()
