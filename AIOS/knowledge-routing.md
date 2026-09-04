---
type: map
status: active
date: 2026-05-26
tags: [aios, routing, knowledge, portable]
---

## Knowledge Routing

Cada pedazo de información tiene su casa. Enrútalo hacia allá, nunca hacia un cajón de sastre.

---

### Tabla de enrutamiento

| Tipo de contenido | Va a |
|---|---|
| Preferencias personales, estilo, hábitos | `02 Context/me.md` (solo) o `02 Context/operator.md` (empresa) |
| Estrategia y objetivos | `02 Context/strategy.md` o `02 Context/estrategia.md` |
| Voz y tono de la marca | `02 Context/brand.md` o `02 Context/marca.md` |
| Sobre la empresa (modo empresa) | `02 Context/organization.md` |
| Sobre el equipo (modo empresa) | `02 Context/team.md` |
| Decisión con su razonamiento | `03 Intelligence/decisions/YYYY-MM-DD-{slug}.md` |
| Notas de reunión | `03 Intelligence/meetings/{tipo}/YYYY-MM-DD-{slug}.md` |
| Hallazgo sobre un competidor | `03 Intelligence/competitors/{nombre}.md` |
| Hallazgo de mercado | `03 Intelligence/market/{tema}.md` |
| Resultado de una investigación profunda | `03 Intelligence/research/YYYY-MM-DD-{slug}.md` |
| Información de un proyecto activo | `03 Projects/{nombre}/README.md` o una subcarpeta |
| Investigación relacionada con un proyecto | `03 Projects/{nombre}/research/{tema}.md` |
| Especificación o requisito de un proyecto | `03 Projects/{nombre}/specs/{nombre}.md` |
| Borrador de contenido de un proyecto | `03 Projects/{nombre}/drafts/{nombre}.md` |
| Texto producido (post, correo, etc.) | `04 Resources/textos/{canal}/YYYY-MM-DD-{slug}.md` |
| Brief de landing page | `04 Resources/landing-pages/{slug}.md` |
| Caso de estudio | `04 Resources/casos/{cliente}.md` |
| Auditoría SEO | `04 Resources/seo/auditorias/YYYY-MM-DD-{sitio}.md` |
| Salida de Google Ads | `04 Resources/ads/google/YYYY-MM-DD-{modo}-{slug}.md` |
| Recursos reutilizables (prompts, marcos) | `04 Resources/` |
| Captura rápida sin procesar | `00 Inbox/` |
| Contenido terminado o archivado | `05 Archives/` |
| Dominio de conocimiento (auto-cargado) | `knowledge/{dominio}.md` |
| Reglas de comportamiento de la IA | `02 Context/me.md` (sección Reglas) |

---

### Sub-enrutamiento de proyectos

Cuando aparece información sobre un proyecto, analízala y enrútala a la subcarpeta correcta:

| Tipo de contenido | Subcarpeta |
|---|---|
| Estado, fecha límite, panorama | `03 Projects/{nombre}/README.md` |
| Investigación, análisis de un competidor | `03 Projects/{nombre}/research/{tema}.md` |
| Especificación, requisito, brief | `03 Projects/{nombre}/specs/{nombre}.md` |
| Borrador, guion, contenido escrito | `03 Projects/{nombre}/drafts/{nombre}.md` |
| Idea, lluvia de ideas | `03 Projects/{nombre}/ideas/{nombre}.md` |
| Notas de trabajo | `03 Projects/{nombre}/notes/{nombre}.md` |
| Comentarios, revisión | `03 Projects/{nombre}/feedback/{nombre}.md` |

**Subcarpetas sobre la marcha:** no crees carpetas vacías por adelantado. Cuando llegue contenido que necesite una subcarpeta, créala en ese momento.

**El README como índice:** el README.md es la puerta de entrada, con panorama + estado + próximos pasos + enlaces a las subcarpetas. No dupliques en el README el contenido de las subcarpetas.

**Ciclo de vida:** proyecto nuevo = solo README.md → las subcarpetas aparecen a medida que emergen los tipos de contenido → el proyecto terminado migra a `05 Archives/projects/{nombre}/`.

---

### Sub-enrutamiento de reuniones

Al procesar la transcripción o las notas de una reunión, enrútala por tipo:

| Tipo | Carpeta |
|---|---|
| Llamada con cliente | `03 Intelligence/meetings/client-calls/` |
| 1:1 con un colaborador | `03 Intelligence/meetings/one-on-ones/` |
| Standup del equipo | `03 Intelligence/meetings/team-standups/` |
| Reunión suelta | `03 Intelligence/meetings/general/` |
| Board review (modo empresa) | `03 Intelligence/meetings/board-reviews/` |
| All-hands (modo empresa) | `03 Intelligence/meetings/all-hands/` |
| Cross-team (modo empresa) | `03 Intelligence/meetings/cross-team/` |

Formato del nombre del archivo: `YYYY-MM-DD-{slug-de-la-reunion}.md`.

---

### Sub-enrutamiento de las salidas de los comandos

Cada comando guarda en una carpeta consistente:

| Comando | Guarda en |
|---|---|
| `/escribir` | `04 Resources/textos/YYYY-MM-DD-{tipo}-{slug}.md` |
| `/linkedin` | `04 Resources/textos/linkedin/YYYY-MM-DD-{slug}.md` |
| `/newsletter` | `04 Resources/textos/newsletter/YYYY-MM-DD-{slug}.md` |
| `/secuencia-email` | `04 Resources/textos/secuencias-email/YYYY-MM-DD-{tipo}-{slug}.md` |
| `/landing-page` | `04 Resources/landing-pages/{slug}.md` |
| `/case-study` | `04 Resources/casos/{cliente-slug}.md` |
| `/seo-pagina` | `04 Resources/seo/auditorias/YYYY-MM-DD-{sitio}-{pagina}.md` |
| `/ads-google` | `04 Resources/ads/google/YYYY-MM-DD-{modo}-{slug}.md` |
| `/investigacion` | `03 Intelligence/research/YYYY-MM-DD-{slug}.md` |

---

### La regla de oro

**Antes de guardar cualquier cosa, pregúntate:**
1. ¿Esto es sobre el usuario o sobre la empresa? → `02 Context/`
2. ¿Esto es una decisión, una reunión o un hallazgo sobre el mundo externo? → `03 Intelligence/`
3. ¿Esto es sobre un proyecto específico? → `03 Projects/{nombre}/`
4. ¿Esto es la salida de un comando? → `04 Resources/` (la subcarpeta del comando)
5. ¿Esto es conocimiento permanente que la IA siempre debe saber? → `knowledge/`
6. ¿Todavía no estoy seguro? → `00 Inbox/`

Cuando dudes, escoge el lugar más específico posible. `00 Inbox/` es el último recurso, no el primero.

---

## Conectado a

[[Home]] · [[index]] · [[Vault-Map]] · [[operating-rules]] · [[project-map]]
