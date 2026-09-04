# AI OS — Central de Comando

Eres la IA que opera este vault. Todo lo que necesitas para trabajar bien está en los archivos de abajo.

Léelos al comienzo de cada sesión. No anuncies que estás leyendo. Solo absórbelo y responde como si ya estuvieras en la conversación.

---

## Session Startup (hazlo en el primer mensaje)

Lee estos archivos al comienzo de cada sesión. No lo anuncies, solo absórbelo y responde:

1. `02 Context/me.md` (modo solo) **o** `02 Context/operator.md` + `organization.md` (modo empresa). Quién es el usuario.
2. La nota más reciente en `01 Daily/`. Qué pasó en la sesión anterior.
3. `AIOS/operating-rules.md`. Cómo operas en este vault.
4. `AIOS/index.md`. Skills y comandos disponibles.
5. `knowledge/index.md`. Conocimiento permanente.

El hook `SessionStart` ya inyecta la identidad y el último daily en el contexto automáticamente. Si no recibiste ese bloque (por ejemplo, porque Python no está instalado en la máquina), lee tú mismo los archivos de arriba antes de responder. Eso es lo que garantiza que siempre te conectes al vault, con hook o sin él.

---

## Mapas del vault (load on demand)

| Archivo | Cuándo leerlo |
|---|---|
| `AIOS/Vault-Map.md` | Cuando necesites saber dónde vive algo o hacia dónde enrutar información nueva |
| `AIOS/knowledge-routing.md` | Cuando estés guardando algo y no tengas certeza de dónde ponerlo |
| `AIOS/project-map.md` | Cuando el usuario mencione un proyecto por su nombre |
| `AIOS/operating-rules.md` | Cuando necesites repasar las reglas de comportamiento |

---

## Estructura del vault

```
00 Inbox/        — Captura rápida, procesar y mover
01 Daily/        — Notas diarias (YYYY-MM-DD.md)
02 Context/      — Identidad permanente
03 Intelligence/ — Reuniones, decisiones, competidores, mercado, investigaciones
03 Projects/     — Una subcarpeta por proyecto activo
04 Resources/    — Biblioteca: resultados de los comandos, prompts, marcos de trabajo
05 Archives/     — Contenido terminado e histórico
AIOS/            — Capa portátil: skills, mapas, reglas
knowledge/       — Knowledge hub que se carga solo en cada sesión
prompts/         — 10 prompts listos para copiar y pegar
```

Detalles completos en `AIOS/Vault-Map.md`. Punto de partida del grafo: [[Home]].

---

## Enrutamiento rápido

| Tipo de contenido | Dónde guardarlo |
|---|---|
| Identidad, preferencias, estilo | `02 Context/me.md` (solo) / `operator.md` (empresa) |
| Sobre la empresa (modo empresa) | `02 Context/organization.md` |
| Sobre el equipo (modo empresa) | `02 Context/team.md` |
| Objetivos, estrategia | `02 Context/strategy.md` o `estrategia.md` |
| Tono de voz, marca | `02 Context/brand.md` o `marca.md` |
| Decisión con su razonamiento | `03 Intelligence/decisions/YYYY-MM-DD-{slug}.md` |
| Notas de reunión | `03 Intelligence/meetings/{tipo}/` |
| Investigación profunda | `03 Intelligence/research/` |
| Proyecto activo | `03 Projects/{nombre}/README.md` |
| Resultados de los comandos | `04 Resources/{categoría}/` |
| Captura rápida | `00 Inbox/` |
| Sesión del día | `01 Daily/YYYY-MM-DD.md` |
| Conocimiento permanente (auto-cargado) | `knowledge/{dominio}.md` |
| Contenido terminado | `05 Archives/` |

Tabla completa en `AIOS/knowledge-routing.md`.

> Nota: los archivos `02 Context/operator.md`, `organization.md`, `team.md`, `estrategia.md` y `marca.md` los crea `/setup`, según el modo (solo o empresa) y las respuestas. Puede que todavía no existan en tu vault. Las referencias de arriba quedan listas para cuando se creen.

---

## Reglas generales

Detalles en `AIOS/operating-rules.md`. Resumen:

- Lee los archivos del Session Startup siempre en el primer mensaje
- Usa `[[wikilinks]]` para TODA referencia interna — nunca enlaces de markdown
- Frontmatter YAML en todo archivo: `type`, `date`, `status`, `tags`
- **Nunca pidas permiso para guardar** — guarda e informa dónde quedó
- Cuando el usuario te corrija, guárdalo como regla permanente en `me.md`
- Prefiere editar notas existentes antes que crear nuevas
- Todo en español (los paths y las claves del frontmatter quedan en inglés)
- Sin adornos: nunca "espero que estés bien", "imagina", "en el mundo de hoy", "vamos allá"

---

## Comandos

**Operativo:**
- `/setup` — Personaliza el vault: modo solo/empresa, agente, importación desde otra IA, 8 preguntas
- `/asistente`: operación diaria, resumen de sesión, revisión diaria/semanal, tareas, memoria, reuniones
- `/organizar`: limpia el vault, enruta notas huérfanas, conecta con wikilinks, archiva lo redundante
- `/importar-contexto`: traer contexto de otra IA después del setup inicial

**Escritura y contenido:**
- `/escribir` — Texto corto en tu voz — 3 variaciones
- `/linkedin` — Post de LinkedIn dedicado, con hooks y estructuras
- `/newsletter` — Edición completa de newsletter
- `/case-study` — Caso de estudio estructurado

**Web y SEO:**
- `/landing-page` — Brief completo de landing page
- `/seo-pagina` — Auditoría SEO de una URL

**Crecimiento:**
- `/secuencia-email` — Campaña de correos automatizada
- `/ads-google` — Google Ads (auditar/construir/optimizar/copy)
- `/investigacion` — Investigación profunda multifuente

---

## Hooks

Configurados en `.claude/settings.json`, corren solos (requieren `python3` en el PATH):

- `SessionStart` llama a `.claude/hooks/session-start.py`: inyecta identidad + último daily en el contexto al comienzo de la sesión. El stdout de `SessionStart` entra en el contexto del modelo. El evento `PreToolUse`, usado antes, NO inyecta stdout en el contexto, y era por eso que el agente parecía desconectado.
- `SessionEnd` llama a `.claude/hooks/session-end.py`: documentación automática OPT-IN, apagada por defecto. Para prenderla, crea el archivo `AIOS/autodoc.enabled` (o exporta `AIOS_AUTODOC=1`). Queda apagada por defecto para no gastar tokens ni trabar la salida de la sesión.
- `PreCompact` llama a `.claude/hooks/session-capture.py`: recuerda persistir la sesión antes de comprimirla.

Sin Python, el vault y los comandos siguen funcionando. Solo quedan apagadas la inyección y el resumen automáticos, y la IA lee los archivos del Session Startup a mano.

---

## Prompts para copiar y pegar

`prompts/` tiene 10 prompts listos para pegar en el chat sin correr ningún comando. Úsalos para los casos simples:

| Prompt | Cuándo usarlo |
|---|---|
| `01-revision-diaria.md` | Comienzo o fin del día (alternativa simple a `/asistente`) |
| `02-notas-reunion.md` | Después de una reunión (alternativa a `/asistente` en modo reunión) |
| `03-brief-contenido.md` | Antes de crear contenido |
| `04-borrador-email.md` | Correos profesionales |
| `05-plan-proyecto.md` | Arrancar un proyecto nuevo |
| `06-investigacion-competidores.md` | Análisis rápido de un competidor |
| `07-post-linkedin.md` | Post de LinkedIn rápido (alternativa a `/linkedin`) |
| `08-revision-semanal.md` | Revisión semanal |
| `09-registro-decision.md` | Documentar una decisión |
| `10-lluvia-de-ideas.md` | Lluvia de ideas libre |

Los comandos `/...` son más robustos; los prompts para copiar y pegar son más rápidos.

---

## Subagentes

El kit trae cuatro subagentes, en `.claude/agents/`. Son de proyecto, así que valen solo en este vault y no ensucian la carpeta personal de la máquina:

- `vault-keeper` — lee el vault y responde con contexto histórico, citando el archivo
- `social-agent` — redacta la respuesta a un mensaje con el contexto de los proyectos
- `decision-tracker` — captura una decisión en `03 Intelligence/decisions/` con su porqué
- `research-agent` — investigación de anuncios, copy y medios, solo de fuentes públicas

Para activar uno, pídelo por su nombre. Para ajustarlo, edita el archivo — es markdown.
