---
description: Escribe posts de LinkedIn en profundidad — hook fuerte, estructura probada, la voz de me.md, 3 variaciones. Acepta reutilizar material de YouTube, blog o una idea en bruto.
---

# LinkedIn — Post profundo

Vas a producir 1 post de LinkedIn listo para publicar, en 3 variaciones, usando la voz y el contexto de `02 Context/me.md`.

Diferencia con `/escribir`: este es dedicado, más profundo, sabe reutilizar material (YouTube, blog, transcripción) y tiene una biblioteca de hooks probados.

---

## Idioma / Language

Detecta el idioma del mensaje que invocó este comando y úsalo en todo. Español por defecto.

---

## Antes de empezar

Lee `02 Context/me.md`. Usa:
- "Tono de voz" — las palabras que usa y las que evita, sus referencias
- "Audiencia" — para quién habla
- "Canales" — confirma que LinkedIn sea un canal activo (si no, avisa: "vi que no marcaste LinkedIn entre tus canales. ¿Lo ajusto de todas formas?")

Si no existe `me.md`, avisa y sigue con un tono neutro.

---

## Fase 1 — El material de partida

Pregunta vía AskUserQuestion:

- Pregunta: "¿De dónde sale el post? ¿Cuál es la materia prima?"
- Header: `Fuente`
- Opciones:
  - `Idea en bruto — la describo yo` — "Usted dice en 1 o 2 frases qué quiere comunicar."
  - `Video de YouTube — enlace` — "Pega el enlace y yo lo extraigo."
  - `Blog o artículo — enlace` — "Pega el enlace y yo lo leo."
  - `Transcripción / reunión — la pego` — "Pega el texto en bruto y yo lo extraigo."
  - `Hallazgo de un cliente / una conversación` — "Usted describe el hallazgo en texto libre."

Después de la elección:

- **Idea en bruto:** "Cuéntemelo en 1 o 2 frases."
- **YouTube:** "Pegue el enlace." Usa yt-dlp si está disponible; si no, WebFetch.
- **Blog:** "Pegue el enlace." Usa WebFetch.
- **Transcripción:** "Pegue el texto."
- **Hallazgo:** "Describa el hallazgo + el contexto donde apareció."

---

## Fase 2 — Definir el ángulo

Cuando tengas el material, identifica de 3 a 5 ángulos posibles. Preséntalos así:

> "Ya vi su material. Ángulos posibles:
> 1. {{ángulo 1 — frase corta}}
> 2. {{ángulo 2}}
> 3. {{ángulo 3}}
>
> ¿Cuál le llama más? ¿O prefiere otro?"

Espera la respuesta. Acepta la elección por número, por descripción, o una idea nueva.

---

## Fase 3 — Definir el objetivo

Pregunta vía AskUserQuestion:

- Pregunta: "¿Cuál es el objetivo de este post?"
- Header: `Objetivo`
- Opciones:
  - `Conversación — comentarios y discusión` — "Maximizar la conversación."
  - `Autoridad — posicionar conocimiento` — "Mostrar competencia sin vender."
  - `Lead — capturar interés comercial` — "CTA suave hacia un DM o un enlace."
  - `Construir audiencia — que lo guarden o compartan` — "Contenido perenne, útil."

---

## Fase 4 — Estructura (interna, no se la preguntes al usuario)

Usa una de las 4 estructuras probadas, según el objetivo:

### Estructura A — Lección (Autoridad)
1. Hook: una afirmación contraintuitiva o un número específico
2. Preparación: contexto corto (1 párrafo)
3. La lección: de 3 a 5 viñetas, o numerada
4. Cierre: 1 frase de síntesis
5. CTA: una pregunta abierta para la discusión

### Estructura B — Historia (Conversación)
1. Hook: una escena específica, 1 frase
2. Preparación: qué estaba en juego
3. El giro: qué pasó
4. La lección que se saca: 1 o 2 párrafos
5. CTA: una pregunta sobre una experiencia parecida

### Estructura C — Marco de trabajo (Guardado / Compartido)
1. Hook: la promesa de un marco práctico
2. El nombre del marco (memorable)
3. Pasos numerados con una explicación corta
4. Un ejemplo aplicado
5. CTA: una pregunta sobre cómo lo usarían

### Estructura D — Hallazgo de cliente (Lead)
1. Hook: un patrón observado en N clientes
2. El problema
3. Cómo lo resuelve usted de otra manera
4. El resultado tangible
5. CTA: "si le resuena, escríbame por DM" (suave, sin vender)

Escoge automáticamente según el objetivo. No preguntes cuál estructura.

---

## Fase 5 — Biblioteca de hooks

Usa uno de estos patrones en la primera línea (reemplaza los placeholders):

**Número específico:**
- "El {{N}}% de {{público}} comete el mismo error con {{tema}}."
- "En {{tiempo}} de {{actividad}}, vi exactamente {{N}} patrones repetirse."

**Contraintuitivo:**
- "Dejaron de llamarme {{rol}} el día que {{acción inesperada}}."
- "La regla que más he escuchado sobre {{tema}} es la que me costó mi cliente más grande."

**Pregunta filosa:**
- "¿Por qué {{evento común}} sigue funcionando en {{año}}?"
- "Si {{premisa popular}} es cierta, ¿cómo se explica {{contradicción}}?"

**Escena específica:**
- "{{Hora}}, {{lugar}}. {{Persona}} me llama y me dice: {{cita}}."
- "Estaba {{acción rutinaria}} cuando me di cuenta de que {{hallazgo}}."

**Promesa directa:**
- "Le voy a mostrar los {{N}} pasos que uso para {{resultado}} en {{tiempo}}."
- "Si usted {{situación}}, estos son los {{N}} bloqueos."

Nunca uses:
- "Imagina..."
- "En el mundo de hoy..."
- "En tiempos como estos..."
- "Hablemos de..."
- "Hoy quiero compartirles..."

---

## Fase 6 — Generar 3 variaciones

Presenta 3 variaciones distintas:

```markdown
## V1 — {{la estructura escogida + el tono estándar de me.md}}

{{post completo}}

---

## V2 — Otro hook, la misma estructura

{{post con un hook del mismo grupo, pero variado}}

---

## V3 — Estructura alternativa

{{post con una estructura distinta a la de la Fase 4, para dar opción}}
```

Cada variación tiene que estar COMPLETA, lista para pegar en LinkedIn. Usa saltos de línea generosos (cada frase en su propia línea cuando tenga sentido).

Longitud: de 800 a 1.300 caracteres por variación. Los posts más cortos para hook + reflexión. Los más largos para marco de trabajo + ejemplo.

---

## Fase 7 — Guardar

Pregunta vía AskUserQuestion:

- Pregunta: "¿Lo guardo en el vault?"
- Header: `Guardar`
- Opciones:
  - `Sí — las 3 variaciones` — "Crea un archivo único con las 3."
  - `Sí — solo la que escogí` — "Usted me dice cuál."
  - `No — solo usarlo ahora`

Si dice que sí, crea la carpeta si no existe:
```bash
mkdir -p "04 Resources/textos/linkedin"
```

Guarda en `04 Resources/textos/linkedin/YYYY-MM-DD-{{slug-del-tema}}.md`:

```yaml
---
type: copy
status: draft
date: YYYY-MM-DD
tags: [linkedin, post]
canal: linkedin
tema: {{tema}}
fuente: {{idea / youtube / blog / transcripción / hallazgo}}
objetivo: {{el de la P3}}
estructura: {{A / B / C / D}}
---
```

Debajo del frontmatter, guarda las 3 variaciones con sus encabezados.

---

## Fase 8 — Confirmación

Si guardaste:
> "Guardado en `04 Resources/textos/linkedin/{{archivo}}`. Para el próximo post: `/linkedin` otra vez.
>
> Consejo: si lo publica y le va bien, guarde el número en el daily — después lo uso para calibrar."

Si no guardaste:
> "Listo. Para otro: `/linkedin`."

Directo. Sin adornos.

---

## Reglas

- Usa la voz de `me.md` en la V1, con fidelidad.
- Nunca uses las palabras listadas en "NUNCA uso" de `me.md`.
- No inventes números — si el usuario los dio, úsalos; si no, no adivines.
- No inventes clientes ni casos. Si citas un caso, usa las palabras del propio usuario.
- Hashtags solo si son relevantes al nicho (no uses #marketing ni #branding — solo específicos).
- En LinkedIn, la primera línea tiene que frenar el scroll. Ahí se gana o se pierde todo.
