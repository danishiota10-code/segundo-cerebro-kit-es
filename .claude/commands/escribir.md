---
description: Escribe cualquier texto corto usando tu voz guardada en me.md — post de LinkedIn, correo, titular, caption, biografía, descripción. Genera 3 variaciones.
---

# Escribir — Texto corto con tu voz

Vas a producir 3 variaciones de un texto corto, usando la voz y el contexto del usuario que están en `02 Context/me.md`.

---

## Idioma / Language

Detecta el idioma del mensaje que invocó este comando y úsalo en todas las preguntas y en las variaciones generadas.

Español por defecto. Inglés o portugués si el usuario escribió en ese idioma.

---

## Antes de empezar

Lee `02 Context/me.md`. Extrae:
- La sección "Tono de voz" — la voz, las palabras que usa, las que evita, la referencia de estilo
- La sección "Audiencia" — quién es el público
- La sección "Canales" — dónde publica (eso define el formato)

Si `me.md` no existe o todavía tiene los placeholders, avisa:
> "No encontré contexto de voz en `me.md`. Voy a usar un tono neutro. Para un mejor resultado, corre `/setup` antes."

Y continúa de todos modos.

---

## Preguntas (una a la vez, vía AskUserQuestion)

**P1 — Tipo**
- Pregunta: "¿Qué tipo de texto quieres escribir?"
- Header: `Tipo`
- Opciones:
  - `Post de LinkedIn` — "Texto largo, hook fuerte, cierre con un CTA suave."
  - `Correo` — "Asunto + cuerpo, tono directo."
  - `Titular / hook` — "1 o 2 frases para un anuncio, una portada, un hero."
  - `Caption de Instagram` — "Corto, con saltos de línea, espacio para los hashtags."
  - `Biografía / descripción corta` — "Biografía de perfil, descripción de producto, quiénes somos."
  - `Otro — lo describo yo` — "Cuéntame qué necesitas y lo adapto."

**P2 — Tema y ángulo**
- Pregunta: "¿Sobre qué? Descríbelo en 1 o 2 frases: el tema principal y cuál es tu ángulo. Puedes pegar una referencia si la tienes."
- Header: `Tema`
- Opciones: (deja `Saltar` como una de las opciones; las demás dependen del contexto — puedes pasar una lista vacía si el usuario solo necesita espacio para escribir)

**P3 — Objetivo**
- Pregunta: "¿Cuál es el objetivo? ¿Qué quieres que la persona haga o piense después de leerlo?"
- Header: `Objetivo`
- Opciones:
  - `Informar / educar` — "Compartir conocimiento, sin un CTA fuerte."
  - `Generar conversación` — "Provocar una respuesta, un comentario, que lo compartan."
  - `Vender / convertir` — "Llevar a una acción comercial (una llamada, una compra, una inscripción)."
  - `Construir autoridad` — "Posicionarte a ti como referencia."
  - `Saltar`

**P4 — Longitud (pregúntalo solo si P1 = Post de LinkedIn o Correo)**
- Pregunta: "¿De qué largo?"
- Header: `Tamaño`
- Opciones: `Corto (1 párrafo)` / `Medio (3 o 4 párrafos)` / `Largo (5 o más párrafos, con historia)` / `Saltar`

---

## Generación

Con los datos recogidos + la voz de `me.md`, genera 3 variaciones distintas.

Cada variación debe tener un ángulo diferente:
- **V1 — El estándar de la voz del usuario**: replica fielmente el estilo de `me.md`
- **V2 — Más provocadora / a contracorriente**: usa un hook que va contra el sentido común
- **V3 — Más narrativa**: arranca con una escena, una microhistoria o una observación concreta

Preséntalas en markdown, separadas por `---`:

```markdown
## V1 — {{etiqueta corta}}

{{texto de la variación 1}}

---

## V2 — {{etiqueta corta}}

{{texto de la variación 2}}

---

## V3 — {{etiqueta corta}}

{{texto de la variación 3}}
```

Para el **post de LinkedIn**: usa saltos de línea generosos, el hook en la primera línea, sin hashtags genéricos.

Para el **correo**: incluye `Asunto:` antes del cuerpo.

Para el **titular**: entrega solo la frase, sin rodeos.

Para el **caption de Instagram**: usa saltos con un `.` en líneas aisladas para crear respiro. Termina con 3 a 5 hashtags relevantes (no genéricos como #marketing — específicos del nicho).

Para la **biografía**: máximo 150 caracteres por variación.

---

## Guardar

Después de generarlas, pregunta:

- Pregunta: "¿Quieres guardarlo en el vault?"
- Header: `Guardar`
- Opciones:
  - `Sí — guardar las 3 variaciones` — "Crea un archivo en 04 Resources/textos/."
  - `Sí — solo la que escogí` — "Tú me dices cuál y guardo solo esa."
  - `No` — "Solo usarlo ahora."

Si dice que sí, crea la carpeta si no existe:
```bash
mkdir -p "04 Resources/textos"
```

Guarda en `04 Resources/textos/YYYY-MM-DD-{{tipo}}-{{slug-del-tema}}.md` con este frontmatter:

```yaml
---
type: copy
status: draft
date: YYYY-MM-DD
tags: [{{tipo}}, escritura]
canal: {{tipo}}
tema: {{tema corto}}
---
```

---

## Confirmación

Si guardaste:
> "Guardado en `04 Resources/textos/{{nombre-del-archivo}}`. Para escribir otro, corre `/escribir` de nuevo."

Si no guardaste:
> "Listo. Para escribir otro, corre `/escribir` de nuevo."

Directo al grano, sin adornos.

---

## Reglas

- Usa siempre la voz de `me.md` en la V1. Las variaciones 2 y 3 pueden alejarse para abrir espacio de prueba.
- Nunca uses palabras que `me.md` liste como "NUNCA uso".
- No inventes prueba social (números, testimonios) si el usuario no la dio.
- Si el usuario pegó una referencia en la P2, refleja su estructura, no copies su texto.
- No uses las muletillas típicas de IA: "imagina", "en el mundo de hoy", "en un escenario", "game-changer", "lleva tu X al siguiente nivel".
