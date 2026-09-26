---
type: index
status: active
date: 2026-05-26
tags: [aios, skills, maps, portable]
---

> Mapas: [[02 Context/me|me.md]] · [[Vault-Map]] · [[knowledge/index|Knowledge Index]]

## AIOS — Capa portátil de operación

Esta carpeta es la capa portátil entre tu vault y cualquier herramienta de IA.

Los archivos que están acá son markdown puro — viajan a Claude Code, Cursor, Gemini CLI, o cualquier herramienta que lea texto.

**Filosofía:** File over AI. El conocimiento le pertenece al vault, no a la herramienta.

---

## Cómo funciona

Cuando abres Claude Code (u otra herramienta de IA) dentro de este vault:

1. **Arranca la sesión.** El hook `session-start.py` inyecta en el contexto tu identidad (`02 Context/me.md`, u `operator.md` más `organization.md` en el modo empresa) y el último daily. Este archivo, `AIOS/operating-rules.md`, `AIOS/knowledge-routing.md` y `knowledge/index.md` entran como **punteros**, no como contenido: la IA los lee cuando la tarea lo pide. Es a propósito. Contexto que entra en toda sesión sin usarse cuesta tokens y estorba.
2. **La IA ya te conoce.** Sin que tengas que explicarle quién eres, cómo trabajas ni qué estás haciendo.
3. **Corre el trabajo.** Tú invocas comandos, haces preguntas, ella ejecuta.
4. **Termina el turno.** El hook `session-capture.py` corre en el evento `Stop` y le pide a la IA guardar la sesión en el daily antes de terminar. Se queda callado si la nota de hoy ya se escribió en los últimos 20 minutos.

Por eso `01 Daily/YYYY-MM-DD.md` siempre se lee en la sesión siguiente — se vuelve memoria persistente entre conversaciones.

---

## Comandos disponibles

### Operativo

| Comando | Qué hace |
|---|---|
| `/setup` | Personalización inicial completa del vault |
| `/asistente` | Operación diaria, resumen de sesión, revisiones, tareas, memoria |
| `/organizar` | Limpia el vault: enruta notas huérfanas, conecta con wikilinks, archiva lo redundante |
| `/importar-contexto` | Traer al vault el contexto de otra IA |

### Escritura y contenido

| Comando | Qué hace |
|---|---|
| `/escribir` | Texto corto en tu voz — 3 variaciones |
| `/linkedin` | Post de LinkedIn dedicado, con hooks y estructuras |
| `/newsletter` | Edición completa de newsletter |
| `/case-study` | Caso de estudio de cliente, estructurado |

### Web y SEO

| Comando | Qué hace |
|---|---|
| `/landing-page` | Brief completo de landing page |
| `/seo-pagina` | Auditoría SEO de una URL |

### Crecimiento

| Comando | Qué hace |
|---|---|
| `/secuencia-email` | Campaña de correos automatizada |
| `/ads-google` | Google Ads (auditar/construir/optimizar/copy) |
| `/investigacion` | Investigación profunda multifuente |

---

## Mapas hermanos

Cada archivo de abajo responde una pregunta distinta:

| Archivo | Pregunta |
|---|---|
| [[AIOS/Vault-Map]] | ¿Dónde queda cada cosa en este vault? |
| [[AIOS/operating-rules]] | ¿Cómo debe comportarse la IA? |
| [[AIOS/knowledge-routing]] | ¿Para dónde va cada tipo de información? |
| [[AIOS/project-map]] | ¿Qué proyectos tengo activos? |
| [[02 Context/me]] | ¿Quién opera este vault? |
| [[CLAUDE.md]] | ¿Cómo se usa esto en la práctica? |

---

## Principios de la capa portátil

1. **Markdown puro**, nada de formatos propietarios
2. **Sin código en los archivos de contexto**, solo texto que cualquier IA entiende
3. **Rutas relativas**, funciona en cualquier máquina
4. **Self-describing**, cada archivo tiene frontmatter que explica qué es
5. **Actualizable por la IA**, cuando algo cambia, la IA actualiza este archivo automáticamente

---

## Conectado a

[[Home]] · [[Vault-Map]] · [[knowledge-routing]] · [[operating-rules]] · [[project-map]]
