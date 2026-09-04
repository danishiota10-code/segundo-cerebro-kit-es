---
type: reference
status: active
tags: [navigation, vault-map, ai-os]
updated: 2026-05-26
---

# Vault Map — AI OS

Mapa completo de tu vault. Consúltalo siempre que necesites saber dónde vive algo, hacia dónde enrutar información nueva, o cuando la IA pregunte por algún proyecto.

Este archivo responde **dónde van las cosas**. `02 Context/me.md` responde **quién opera** este vault. `CLAUDE.md` responde **cómo se usa**. `AIOS/index.md` responde **qué se puede hacer**.

---

## Estructura raíz

```
CLAUDE.md                      — Puntero principal + mapa de proyectos
Vault-Map.md                   — Este archivo: mapa completo + enrutamiento
00 Inbox/                      — Zona de captura: notas en bruto que hay que procesar
01 Daily/                      — Notas diarias de sesión (YYYY-MM-DD.md)
02 Context/                    — Capa de identidad (me.md, strategy.md, brand.md)
03 Intelligence/               — Reuniones, decisiones, competidores, mercado, investigaciones
03 Projects/                   — Todos los proyectos activos
04 Resources/                  — Prompts, marcos de trabajo, swipe files, plantillas
05 Archives/                   — Contenido terminado e histórico
AIOS/                          — Capa portátil de operación: skills, mapas, reglas
knowledge/                     — Knowledge hub que se carga solo en cada sesión
.claude/                       — Configuración y hooks de Claude Code
prompts/                       — 10 prompts listos para copiar y pegar
```

---

## Las carpetas en detalle

### `00 Inbox/`
Zona de captura. Todo lo que llega acá hay que procesarlo y moverlo.

**Cómo se usa:** cuando el usuario dice "anota", "captura", "guarda esto por ahora" → cae acá. No es destino final.

**Cuándo procesarlo:** durante la revisión diaria o semanal, corriendo `/asistente` en modo "tareas" para mover cada ítem a su lugar.

---

### `01 Daily/`
Notas diarias de sesión. Una por día, en formato `YYYY-MM-DD.md`.

**Qué tiene adentro:**
- El foco del día
- Lo que se hizo
- Las decisiones tomadas
- Los aprendizajes
- Los próximos pasos para mañana
- Las tareas abiertas

**Se lee sola:** la nota más reciente se carga al comienzo de cada sesión con el hook `session-start.py`.

---

### `02 Context/`
Capa de identidad permanente. Se lee al comienzo de cada sesión.

**Archivos:**
- `me.md` (solo) o `operator.md` + `organization.md` + `team.md` (empresa) — quién eres
- `brand.md` — voz, tono y palabras clave de la marca (se crea si es relevante)
- `strategy.md` — visión, metas a 90 días / 1 año / 3-5 años (se crea si es relevante)
- Otros que se van creando a medida que aparece el contexto

---

### `03 Intelligence/`
Conocimiento sobre el mundo externo + decisiones internas.

**Estructura:**
```
03 Intelligence/
├── meetings/              — Notas de reunión por tipo
│   ├── client-calls/      — Llamadas con clientes
│   ├── one-on-ones/       — 1:1 con colaboradores
│   ├── team-standups/     — Standups del equipo
│   └── general/           — Reuniones sueltas
├── decisions/             — Decisiones importantes con su razonamiento (YYYY-MM-DD-{slug}.md)
├── competitors/           — Análisis de competidores (1 archivo por competidor)
├── market/                — Hallazgos de mercado por tema
├── research/              — Salidas del comando /investigacion
└── archive/               — Archivo del contenido de esta carpeta
```

**El modo empresa agrega:**
- `processes/` — Documentación de los procesos de la empresa
- `meetings/board-reviews/`, `meetings/all-hands/`, `meetings/cross-team/`

---

### `03 Projects/`
Cada proyecto activo tiene su subcarpeta. Cada proyecto tiene un `README.md` como puerta de entrada.

**Estructura típica:**
```
03 Projects/{nombre-del-proyecto}/
├── README.md              — Panorama, estado, próximos pasos
├── research/              — Investigaciones relacionadas
├── specs/                 — Especificaciones y requisitos
├── drafts/                — Borradores de contenido
└── ideas/                 — Lluvia de ideas libre
```

**Cuándo crearla:** cuando el usuario menciona algo que va a durar más de 1 semana de trabajo — eso es un proyecto. Lo suelto se queda en `00 Inbox/` o en `01 Daily/`.

---

### `04 Resources/`
Biblioteca personal reutilizable. Prompts, marcos de trabajo, referencias, plantillas.

**La estructura emerge con el uso:**
```
04 Resources/
├── textos/                — Salidas de /escribir, /linkedin, /newsletter
│   ├── linkedin/
│   ├── newsletter/
│   └── secuencias-email/
├── landing-pages/         — Briefs de /landing-page
├── casos/                 — Salidas de /case-study
├── seo/auditorias/        — Salidas de /seo-pagina
├── ads/google/            — Salidas de /ads-google
├── attachments/           — Imágenes, PDF, adjuntos
└── (otras que tú crees)
```

---

### `05 Archives/`
Contenido terminado, histórico. Cosas que no van a desaparecer, pero que ya no están activas.

**Cuándo usarla:**
- Proyecto terminado → mover de `03 Projects/{nombre}/` a `05 Archives/projects/{nombre}/`
- Edición de newsletter ya publicada → opcional, mover de `04 Resources/textos/newsletter/` a `05 Archives/newsletter/`
- Cliente que se fue → mover sus notas diarias específicas, briefs, etc.

---

### `AIOS/`
Capa portátil. Esta carpeta es el cerebro operativo que no depende de ninguna herramienta.

**Archivos:**
- `index.md` — Catálogo de skills y mapas
- `Vault-Map.md` — Este archivo
- `operating-rules.md` — Cómo debe comportarse la IA
- `knowledge-routing.md` — Hacia dónde enrutar cada tipo de información
- `project-map.md` — Mapa de los proyectos activos
- `blueprint/` — Arquitectura interna del AI OS

---

### `knowledge/`
Knowledge hub que se carga solo en cada sesión.

**Qué va acá:**
- `index.md` — Navegación de los archivos de conocimiento (se carga de primero)
- Dominios de experticia que quieres que la IA tenga siempre (por ejemplo: `copywriting.md`, `seo-fundamentos.md`, `linkedin-strategy.md`)

**Diferencia con `04 Resources/`:**
- `knowledge/` se carga automáticamente en cada sesión (la IA siempre "se acuerda")
- `04 Resources/` es referencia que la IA busca cuando la necesita (no se carga por defecto)

---

## Hub Notes (nodos de conexión)

Usa wikilinks hacia estos archivos siempre que menciones el tema:

| Hub | Para qué sirve |
|---|---|
| `[[02 Context/me]]` | Tú (modo solo) — identidad central |
| `[[02 Context/operator]]` + `[[02 Context/organization]]` | Tú + la empresa (modo empresa) |
| `[[AIOS/index]]` | Comandos y skills disponibles |
| `[[03 Projects/{nombre}/README]]` | Cada proyecto activo |

Conectar con wikilinks hace crecer el grafo de Obsidian — tú ves las conexiones de forma visual.

---

## Enrutamiento rápido

Para saber hacia dónde va una información nueva, consulta [[AIOS/knowledge-routing]].

---

## Conectado a

[[Home]] · [[index]] · [[knowledge-routing]] · [[operating-rules]] · [[project-map]]
