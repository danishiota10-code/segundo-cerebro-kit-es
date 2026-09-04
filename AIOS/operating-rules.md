---
type: map
status: active
date: 2026-05-26
tags: [aios, rules, obsidian, portable]
---

## Operating Rules

Cómo opera la IA en este vault. Portátil — vale en cualquier herramienta que lea este archivo (Claude Code, Cursor, Gemini CLI).

---

### Comportamiento central

1. Leer `knowledge/index.md` y `02 Context/me.md` (o `operator.md` + `organization.md` en modo empresa) al comienzo de la sesión. Leer la última nota en `01 Daily/`. No anunciarlo — solo absorberlo y responder como si ya estuvieras en la conversación.
2. Cuando se haya hecho trabajo relevante, actualizar `01 Daily/YYYY-MM-DD.md`. Solo cuando haya algo digno de registrarse — no en cada mensaje.
3. **Nunca pedir permiso para guardar.** Guardar automáticamente la información relevante en el archivo correcto del vault y reportar qué se guardó.
4. Cuando el usuario corrija a la IA, guardar la corrección como regla permanente en `02 Context/me.md` de inmediato. No preguntar — guardar y confirmar.
5. **Buscar antes de preguntar** — nunca pedir información que se pueda encontrar leyendo archivos del vault. Revisar primero el archivo correspondiente.
6. Cuando el usuario señale confusión ("no entendí"), explicar primero. Nunca tratar la confusión como una aprobación para seguir.

---

### Reglas de escritura en el vault

7. Usar `[[wikilinks]]` para TODA referencia a un proyecto, una persona o una nota, en cualquier archivo del vault. Eso construye el grafo.
8. Nunca usar `[enlaces](de-markdown)` para notas internas del vault.
9. Nunca poner un encabezado `# Título` que duplique el nombre del archivo. Obsidian ya muestra el nombre.
10. Usar frontmatter YAML en toda nota: `type`, `date`, `status`, `tags`, `proyecto` (cuando aplique).
11. Cada nota debe ser autónoma y combinable — como una pieza de Lego.

---

### Enrutamiento de la información

12. Cuando aparezca información, enrutarla de inmediato al archivo correcto (ver `AIOS/knowledge-routing.md`).
13. No acumular todo en `01 Daily/` — el daily es el registro de la sesión, no el destino final del conocimiento permanente.
14. Decisiones con su razonamiento → `03 Intelligence/decisions/`
15. Reuniones → `03 Intelligence/meetings/{tipo}/`
16. Hallazgos sobre competidores → `03 Intelligence/competitors/{nombre}.md`
17. Hallazgos de mercado → `03 Intelligence/market/{tema}.md`

---

### Búsqueda y herramientas

18. Usar `grep` o la búsqueda de Obsidian para escanear archivos — no leer archivos completos cuando se están escaneando varios.
19. Usar el frontmatter para filtrar (ejemplo: `type: meeting AND date > 2026-05-01`).
20. Al extraer contenido de la web, preferir WebFetch o yt-dlp antes que copiar y pegar a mano.
21. Respetar `.claudeignore` si existe — nunca leer archivos listados ahí.

---

### Idioma

22. Todo en el vault en español, a menos que el usuario indique otra cosa.
23. Las claves del frontmatter y los paths quedan en inglés (son técnicos).
24. Los comandos (`/setup`, `/escribir`, etc.) detectan el idioma del mensaje que los invoca y adaptan la salida.

---

### Tono

25. Directo, práctico, sin adornos.
26. Nada de "espero que estés bien", "imagina", "en el mundo de hoy", "vamos allá".
27. Usar la voz de `02 Context/me.md` o `02 Context/brand.md` al escribir contenido.
28. No usar rayas ni guiones largos dentro de las frases. Usar comas, puntos, o reformular.

---

### Antipatrones

NO hagas:
- Preguntar "¿guardo esto?" — simplemente guárdalo
- Escribir nombres de proyectos o personas como texto plano — SIEMPRE `[[wikilinks]]`
- Usar `[enlaces](de-markdown)` para notas internas — siempre wikilinks
- Poner un encabezado `# Título` que duplique el nombre del archivo
- Crear notas huérfanas — siempre enlazarlas desde al menos 1 nota existente
- Leer archivos completos cuando estás escaneando muchos — usa `grep`
- Actualizar el daily por una charla casual — solo cuando haya algo que valga
- Crear tareas como texto plano en las notas — usa el callout `> [!todo]` para que se puedan consultar
- Volcarlo todo en el daily; enrútalo al archivo correcto según el tipo de contenido

---

## Conectado a

[[Home]] · [[index]] · [[Vault-Map]] · [[knowledge-routing]] · [[project-map]]
