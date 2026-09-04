#!/usr/bin/env python3
"""
AI OS — Session Capture Hook

Dispara en PreCompact — red de seguridad para sesiones largas. Le recuerda a la IA
persistir el conocimiento de la sesion en el daily ANTES de que el contexto se
comprima y se pierdan los detalles.

El resumen final automatico corre por cuenta de session-end.py (SessionEnd).
Este hook cubre el caso de las sesiones largas que se comprimen antes de terminar.
"""
import os
import sys
from datetime import date

# Guard anti-recursion: no corre durante la documentacion headless.
if os.environ.get("AIOS_DOCUMENTING") == "1":
    sys.exit(0)

today = date.today().isoformat()

print(f"""[AI OS — Session Capture]
El contexto se va a comprimir. Persiste esta sesion en 01 Daily/{today}.md AHORA.

Usa este esquema como nueva entrada `## Sesion`:

**Decisiones tomadas:** (decisiones de arquitectura, estrategia o producto de esta sesion)
**Lo que se hizo:** (acciones concretas realizadas)
**Aprendizajes:** (que funciono, que fallo, que se descubrio)
**Proximos pasos:** (acciones concretas, especificas, con responsable y fecha si se puede)

Enruta cualquier informacion nueva de proyecto, correccion o decision al archivo correcto del vault antes de comprimir.
Consulta AIOS/knowledge-routing.md si tienes dudas sobre donde va algo.
""")
