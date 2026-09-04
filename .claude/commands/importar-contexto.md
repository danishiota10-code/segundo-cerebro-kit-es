---
description: Importa el contexto de otra IA (ChatGPT, Claude, Gemini) — genera un prompt para que usted lo pegue allá, usted pega la respuesta de vuelta, y el vault se actualiza con profundidad real
---

# Importar contexto — De otra IA a su vault

Úselo cuando quiera actualizar su vault con el contexto que otra IA ya tiene sobre usted. También funciona después de `/setup` — entre más contexto, mejor.

---

## Idioma / Language

Detecta el idioma del mensaje que invocó este comando y úsalo en todas las preguntas y mensajes.

Español por defecto. Inglés o portugués si el usuario escribió en ese idioma.

---

## Fase 1 — Escoger la IA de origen

Pregunta vía AskUserQuestion:

- Pregunta: "¿De cuál IA quiere importar el contexto?"
- Header: `IA de origen`
- Opciones:
  - `ChatGPT` — "Tiene memoria activa entre conversaciones, si usted la prendió."
  - `Claude (claude.ai)` — "Sin memoria persistente — usa el contexto de esa conversación."
  - `Gemini` — "Puede buscar en el correo y en Drive si es Workspace."
  - `Perplexity` — "Tiene 'spaces' con contexto persistente."
  - `Otra IA` — "Un prompt genérico que funciona en cualquiera."

Guarda la elección.

---

## Fase 2 — Generar el prompt

Imprime el prompt correspondiente en un bloque de código markdown bien destacado. Antes del bloque, escribe:

> "Copie el prompt de abajo, péguelo en su conversación con {{la IA escogida}} y espere a que responda. Cuando tenga la respuesta completa, péguela acá y yo la proceso."

### Prompt — ChatGPT

```
Voy a configurar un sistema de IA personal en otra herramienta. Por favor devuélveme todo lo que sabes sobre mí, con base en nuestras conversaciones anteriores y en tu memoria. Organízalo en markdown, con esta estructura exacta:

## 1. Identidad
Nombre, edad (si la sabes), ubicación, contexto personal relevante.

## 2. Profesión
Cargo actual, empresa, sector, desde hace cuánto, responsabilidades principales, clientes o partes interesadas.

## 3. Objetivos
Corto plazo (90 días), mediano (1 año), largo (3 a 5 años). Si no sabes alguno, escribe "sin datos".

## 4. Cómo trabajo
Rutina, herramientas que uso (Notion, Linear, Slack, etc.), estilo, preferencias, horarios productivos.

## 5. Mi voz
Cómo escribo, palabras que uso, palabras que evito, tono (formal/casual/técnico), referencias de estilo.

## 6. Audiencia
A quién atiendo profesionalmente, quién es mi público si creo contenido, el perfil de esas personas.

## 7. Canales
Dónde publico o me comunico (LinkedIn, Instagram, YouTube, newsletter, blog, etc.). Frecuencia y foco de cada canal.

## 8. Retos actuales
Qué me está preocupando, dónde estoy trabado, cuáles son mis principales dolores o bloqueos.

## 9. Historial relevante
Decisiones importantes que tomé, proyectos que importan, aprendizajes marcantes.

## 10. Red
Personas importantes en mi vida profesional (mentores, socios, colaboradores frecuentes).

## 11. Recursos
Libros, creadores, marcos de trabajo y herramientas que sigo o uso como referencia.

Reglas:
- Si no tienes información sobre algún ítem, escribe "sin datos" — NO lo inventes.
- Sé conciso. Viñetas, no párrafos largos.
- Incluye fechas cuando las sepas.
- Devuelve solo el markdown, sin comentarios extra antes ni después.
```

### Prompt — Claude (claude.ai)

```
Voy a configurar un sistema de IA personal en otra herramienta. Con base en todo lo que sabes de mí EN ESTA conversación (y cualquier contexto que yo haya pegado antes), devuélveme un resumen completo en markdown, con la estructura de abajo:

## 1. Identidad
Nombre, edad (si la sabes), ubicación, contexto personal relevante.

## 2. Profesión
Cargo actual, empresa, sector, desde hace cuánto, responsabilidades principales, clientes o partes interesadas.

## 3. Objetivos
Corto plazo (90 días), mediano (1 año), largo (3 a 5 años). Si no sabes alguno, escribe "sin datos".

## 4. Cómo trabajo
Rutina, herramientas que uso (Notion, Linear, Slack, etc.), estilo, preferencias, horarios productivos.

## 5. Mi voz
Cómo escribo, palabras que uso, palabras que evito, tono (formal/casual/técnico), referencias de estilo.

## 6. Audiencia
A quién atiendo profesionalmente, quién es mi público si creo contenido, el perfil de esas personas.

## 7. Canales
Dónde publico o me comunico (LinkedIn, Instagram, YouTube, newsletter, blog, etc.). Frecuencia y foco de cada canal.

## 8. Retos actuales
Qué me está preocupando, dónde estoy trabado, cuáles son mis principales dolores o bloqueos.

## 9. Historial relevante
Decisiones importantes que tomé, proyectos que importan, aprendizajes marcantes.

## 10. Red
Personas importantes en mi vida profesional (mentores, socios, colaboradores frecuentes).

## 11. Recursos
Libros, creadores, marcos de trabajo y herramientas que sigo o uso como referencia.

Reglas:
- Si no compartí información sobre algún ítem en esta conversación, escribe "sin datos".
- No inventes. No adivines. Solo lo que esté explícito en nuestro historial acá.
- Sé conciso. Viñetas, no párrafos.
- Devuelve solo el markdown.
```

### Prompt — Gemini

Usa el prompt de ChatGPT de arriba, más este párrafo al final:

```
Si usas el Gemini integrado a Google Workspace, también puedes buscar contexto en mis correos, documentos y Drive recientes para enriquecer la respuesta. Si lo haces, marca con claridad qué información vino de dónde (ej.: "[del Drive: Plan Q1 2026]").
```

### Prompt — Perplexity u otra IA

Usa el prompt de ChatGPT sin modificaciones.

---

## Fase 3 — Esperar la respuesta

Dile al usuario:
> "Quedo esperando a que pegue la respuesta acá. Puede ser todo de una vez."

Espera el siguiente mensaje del usuario. Cuando lo pegue:
- Identifica cada bloque numerado (`## 1. Identidad`, `## 2. Profesión`, etc.)
- Extrae los datos de cada bloque
- Ignora los "sin datos" — no intentes llenar esos campos

---

## Fase 4 — Actualizar el vault

Trabaja en silencio. No narres cada archivo.

### 4.1 — `02 Context/me.md`

Lee el archivo actual. Si existe:
- Si tiene placeholders (`{{...}}`): reemplázalos con los datos extraídos
- Si ya tiene contenido real: **agrega** los datos nuevos, no sobrescribas (combina)
- Si hay conflicto, deja lo que ya está en el archivo (es más confiable) y agrega el resto como complemento

Si `me.md` no existe, créalo con la plantilla estándar y llénalo con los datos.

Mapea los bloques de la IA a las secciones de me.md:
- Bloque 1 (Identidad) → sección "Identidad"
- Bloque 2 (Profesión) → sección "Identidad" (el campo profesional) + "Contexto profesional"
- Bloque 3 (Objetivos) → sección "Objetivos actuales"
- Bloque 4 (Cómo trabajo) → sección "Cómo trabajo"
- Bloque 5 (Voz) → sección "Tono de voz"
- Bloque 6 (Audiencia) → sección "Audiencia"
- Bloque 7 (Canales) → sección "Canales"
- Bloque 8 (Retos) → sección "Contexto profesional" (el campo del reto)

### 4.2 — Archivos derivados

**Si el bloque 3 (Objetivos) trae sustancia → crea o actualiza `02 Context/estrategia.md`:**

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [estrategia, objetivos]
---

# Estrategia

## Meta a 90 días
{{del bloque 3}}

## Meta a 1 año
{{del bloque 3}}

## Meta a 3-5 años
{{del bloque 3}}
```

**Si los bloques 5, 6 y 7 (voz, audiencia, canales) traen sustancia → crea o actualiza `02 Context/marca.md`:**

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [marca, voz]
---

# Marca y voz

## Audiencia
{{bloque 6}}

## Canales
{{bloque 7}}

## Voz y tono
{{bloque 5}}
```

**Si el bloque 11 (Recursos) trae libros, marcos o herramientas → guárdalo en `04 Resources/referencias-personales.md`:**

```markdown
---
type: reference
status: active
date: YYYY-MM-DD
tags: [referencias, recursos]
---

# Referencias y recursos

{{el contenido del bloque 11, organizado por categoría: libros, creadores, marcos de trabajo, herramientas}}
```

### 4.3 — La nota diaria

Agrega al daily de hoy (`01 Daily/YYYY-MM-DD.md`), o créalo si no existe:

```markdown
## Importación de contexto — {{la IA usada}}

- **Fuente:** {{ChatGPT / Claude / Gemini / etc.}}
- **Actualizado:** {{la lista de archivos actualizados o creados}}
- **Próximos pasos:** revisar `me.md` y ajustar si algo de la IA no cuadra con la realidad.
```

---

## Fase 5 — Confirmación

Un mensaje corto:

> "Contexto importado de {{la IA usada}}. Actualicé:
> - `02 Context/me.md`
> - {{la lista de los otros archivos creados o actualizados}}
>
> Le recomiendo abrir el `me.md` y revisarlo — las IA se equivocan en algunos detalles, sobre todo en fechas y nombres.
>
> Para escribir con la voz nueva: `/escribir`. Para un brief de landing: `/landing-page`."

---

## Reglas

- Nunca sobrescribas datos reales de `me.md` con datos de la IA — agrégalos o complétalos.
- Si la IA respondió "sin datos" en un bloque, deja la sección como está en la plantilla (o quítala si queda vacía).
- Confirma las fechas — las IA suelen equivocarse con el año y los plazos. Si algo suena raro, márcalo con `{{verificar}}` en la nota del daily.
- No inventes. Si la IA no lo dijo, no lo llenes.
- Usa las palabras exactas del usuario (las que vienen de la IA) cuando se pueda — no parafrasees el tono de voz.
