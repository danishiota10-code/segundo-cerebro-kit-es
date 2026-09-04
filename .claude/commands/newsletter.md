---
description: Escribe una edición completa de newsletter — líneas de asunto, intro, cuerpo estructurado, cierre, CTA. Reutiliza material de YouTube, blog o una idea.
---

# Newsletter — Edición completa

Vas a producir 1 edición completa de newsletter, lista para enviar, usando la voz y el contexto de `02 Context/me.md`.

---

## Idioma / Language

Detecta el idioma del mensaje y úsalo en todo. Español por defecto.

---

## Antes de empezar

Lee `02 Context/me.md`:
- "Tono de voz"
- "Audiencia" — quién está suscrito a su newsletter
- "Canales" — confirma que la newsletter sea un canal activo

Si existe `02 Context/marca.md`, léelo también — puede tener el nombre de la newsletter, la plataforma (Beehiiv, Substack, etc.) y la frecuencia.

---

## Fase 1 — El material de partida

Pregunta vía AskUserQuestion:

- Pregunta: "¿De dónde sale esta edición?"
- Header: `Fuente`
- Opciones:
  - `Idea en bruto` — "Cuénteme en 2 o 3 frases qué quiere comunicar."
  - `Video de YouTube — enlace` — "Pegue el enlace."
  - `Un post de LinkedIn que funcionó` — "Pegue el post y lo expandimos."
  - `Reflexión de la semana` — "Qué aprendió, qué vio, qué está observando."
  - `Tutorial / cómo hacer algo específico` — "Usted enseña algo paso a paso."
  - `Análisis / opinión` — "Usted tiene una posición fuerte sobre algo."

Después de la elección, pide el material.

---

## Fase 2 — Definir la promesa central

La newsletter necesita UNA promesa clara — qué sabe el lector después de leerla.

Identifica 2 o 3 promesas posibles con base en el material. Preséntalas:

> "Promesas posibles para esta edición:
> 1. {{promesa 1 — formato: 'Después de esta edición usted va a saber X'}}
> 2. {{promesa 2}}
> 3. {{promesa 3}}
>
> ¿Cuál quiere?"

Espera la elección.

---

## Fase 3 — Definir la estructura

Pregunta vía AskUserQuestion:

- Pregunta: "¿Qué formato de edición? (escoja 1 — afecta el tono y la longitud)"
- Header: `Formato`
- Opciones:
  - `Reflexión personal (400-600 palabras)` — "Tono más íntimo, 1 idea central, sin subtítulos."
  - `Enseñanza práctica (800-1200 palabras)` — "Cómo hacer X. Estructura clara, subtítulos, un ejemplo."
  - `Análisis (1000-1500 palabras)` — "Usted defiende una posición con evidencia."
  - `Curaduría (300-500 palabras)` — "Usted junta 3 a 5 cosas útiles de la semana y las comenta."
  - `Tutorial técnico (1200+ palabras)` — "Paso a paso, con código o pantallazos."

---

## Fase 4 — Generar la edición

Estructura estándar (adáptala al formato):

### 1. Línea de asunto (3 variaciones)
Presenta 3 variaciones:

**V1 — Curiosidad:**
{{asunto que crea un vacío de conocimiento}}

**V2 — Beneficio directo:**
{{asunto que entrega valor explícito}}

**V3 — Personal / específico:**
{{asunto que parece un correo de un amigo, no una newsletter}}

Reglas del asunto:
- Lo ideal son 30 a 50 caracteres
- Sin MAYÚSCULAS, sin exceso de emojis
- Sin "Newsletter #42 — ..." (aburridor)

### 2. Preencabezado (1 frase, 60 a 90 caracteres)
{{la frase que complementa el asunto y aparece en la vista previa de la bandeja}}

### 3. Apertura (2 a 4 frases)
Un patrón que funciona:
- Una escena específica, O
- Una confesión, O
- Una pregunta directa al lector

Nada de:
- "Espero que estés bien."
- "Es un placer escribirte."
- "Voy a empezar con una reflexión..."

### 4. La promesa (1 frase explícita)
"En esta edición: {{la promesa de la Fase 2}}."

### 5. Cuerpo (adáptalo al formato)

**Reflexión personal:** 1 idea, 3 o 4 párrafos, sin subtítulos.

**Enseñanza práctica:**
- Preparación (por qué esto importa)
- Los N pasos o componentes (con subtítulos `##`)
- Un ejemplo concreto
- El error común

**Análisis:**
- Tesis clara
- 2 o 3 evidencias
- Contraargumento + respuesta
- Implicación

**Curaduría:**
- Ítem 1: {{título}} — {{1 o 2 frases sobre por qué importa}}
- Ítems 2 al 5: igual

**Tutorial técnico:**
- Requisito previo
- Pasos numerados
- Código / configuración
- Resultado esperado
- Próximo paso

### 6. Cierre (2 o 3 frases)
Vuelve a lo personal. Nombra al lector: "Si usted {{situación}}, {{acción sugerida}}."

### 7. P. D. (opcional, pero recomendada)
Es un bloque aparte. Más informal. Suele ser donde va el CTA secundario.

### 8. Firma
"— {{el primer nombre que está en me.md}}"

---

## Fase 5 — Presentar

Presenta la edición completa en markdown, bien estructurada. Incluye todos los elementos (los 3 asuntos, el preencabezado, el cuerpo, etc.).

Después, pregunta:

- Pregunta: "¿Quiere ajustar algo? Puedo reescribir una sección específica."
- Header: `Ajustes`
- Opciones:
  - `Así está bien` — "Vamos a guardarla."
  - `Cambiar el asunto` — "Genero 3 nuevos."
  - `Reescribir la apertura` — "Pruebo con otro ángulo."
  - `Cambiar el tono` — "Más formal / informal / técnico."

Aplica los ajustes hasta que el usuario apruebe.

---

## Fase 6 — Guardar

Crea la carpeta si no existe:
```bash
mkdir -p "04 Resources/textos/newsletter"
```

Guarda en `04 Resources/textos/newsletter/YYYY-MM-DD-{{slug-del-tema}}.md`:

```yaml
---
type: copy
status: ready-to-send
date: YYYY-MM-DD
tags: [newsletter, edicion]
canal: newsletter
formato: {{el de la Fase 3}}
asunto_escogido: {{cuando el usuario escoja uno, márcalo acá}}
---
```

Debajo, la edición completa.

---

## Fase 7 — Próximos pasos

> "Guardada en `04 Resources/textos/newsletter/{{archivo}}`.
>
> Próximos pasos:
> 1. Escoger 1 de los 3 asuntos (haga una prueba A/B si la plataforma lo permite)
> 2. Subirla a la plataforma ({{el nombre si está en me.md; si no, 'Beehiiv / Substack / ConvertKit'}})
> 3. Enviársela primero a usted como prueba, antes de mandarla a la lista
>
> Para la próxima edición: `/newsletter` otra vez. Para reutilizar esta edición en LinkedIn: `/linkedin`."

---

## Reglas

- La voz de `me.md` no se negocia.
- La longitud tiene que ser la del formato — no rellenes para llegar al conteo.
- El asunto sin "Newsletter #N" ni el nombre de la newsletter al comienzo (aburrido y baja el CTR).
- La P. D. suele ser la parte más leída — úsala bien.
- No inventes suscriptores, número de inscritos ni casos específicos. Usa solo lo que dio el usuario o lo que está en `me.md`.
- Prohibido: "espero que estés bien", "voy a empezar con", "en el mundo de hoy", "imagina", "vamos allá".
