---
description: Crea una secuencia de correos automatizada — bienvenida, nutrición, recuperación, onboarding o preventa. Define la cadencia y escribe cada correo con la voz de me.md.
---

# Secuencia de correos — Campaña automatizada

Vas a construir una secuencia completa de correos automatizada, lista para subir a cualquier plataforma (ActiveCampaign, ConvertKit, Beehiiv, Mailchimp, Mautic, MailerLite, etc.).

---

## Idioma / Language

Detecta el idioma y úsalo en todo. Español por defecto.

---

## Antes de empezar

Lee `02 Context/me.md`:
- "Tono de voz"
- "Audiencia"
- "A qué me dedico" — qué ofrece

Si existe `02 Context/marca.md`, léelo. Si hay un proyecto activo relacionado, lee su README.

---

## Fase 1 — Tipo de secuencia

Pregunta vía AskUserQuestion:

- Pregunta: "¿Qué tipo de secuencia quiere crear?"
- Header: `Tipo`
- Opciones:
  - `Bienvenida — se acaba de suscribir` — "5 a 7 correos. Bienvenida, contexto, primera oferta suave."
  - `Onboarding — compró y hay que activarlo` — "3 a 5 correos. Asegurar el uso y el resultado en los primeros días."
  - `Nutrición — leads que todavía no compran` — "4 a 8 correos. Educar y construir confianza hasta la decisión."
  - `Recuperación — clientes o leads inactivos` — "3 a 4 correos. Volver a enganchar a quien desapareció."
  - `Preventa / lanzamiento — cuenta regresiva hasta la apertura` — "5 a 7 correos. Construir deseo y anticipación."
  - `Posventa — después de la compra` — "3 a 4 correos. Reforzar el valor, pedir una reseña, ofrecer una mejora."

---

## Fase 2 — El contexto de la oferta

Pregunta:
> "Cuénteme en 2 o 3 frases:
> 1. Qué está vendiendo o promoviendo
> 2. Quién es la persona que entra en esta secuencia (de dónde viene: pauta, lead magnet, referido)
> 3. Cuál es la acción principal que quiere al final"

Espera la respuesta. Si falta información, pregunta por lo que falte.

---

## Fase 3 — Cadencia

Pregunta vía AskUserQuestion:

- Pregunta: "¿Qué cadencia?"
- Header: `Cadencia`
- Opciones:
  - `Diaria (1 correo al día)` — "Buena para una bienvenida corta y para un lanzamiento de 5 a 7 días."
  - `Cada 2 días` — "El estándar para nutrición y recuperación. Menos invasiva."
  - `Semanal` — "Para nutrición larga, B2B con decisión lenta."
  - `A la medida — yo la digo` — "Usted la define."

---

## Fase 4 — Generar la secuencia

Estructura por tipo:

### Bienvenida (5 correos estándar)

**Correo 1 — Inmediato (después de suscribirse)**
- Asunto: confirma + entrega lo prometido (el lead magnet, etc.)
- Contenido: el enlace o archivo + 1 frase sobre qué esperar los próximos días
- CTA: ninguno fuerte (ya entregó)

**Correo 2 — Día 1**
- Asunto: personal (que parezca un correo de un amigo)
- Contenido: su historia corta — por qué hace lo que hace, a quién atiende
- CTA: responder el correo (crea relación)

**Correo 3 — Día 3**
- Asunto: un hallazgo práctico
- Contenido: 1 concepto que le cambia la perspectiva al lector
- CTA: un artículo o video relacionado

**Correo 4 — Día 5**
- Asunto: un caso corto
- Contenido: un cliente o una situación real que ilustre su valor
- CTA: una pregunta abierta (que responda)

**Correo 5 — Día 7**
- Asunto: una invitación suave
- Contenido: la oferta principal, sin venta dura — explica qué es y para quién
- CTA: enlace a la página de la oferta

### Onboarding (4 correos estándar)

**Correo 1 — Inmediato**
- Asunto: bienvenida + próximos pasos
- Contenido: qué acaba de comprar, qué va a pasar, cómo acceder
- CTA: entrar / hacer la primera acción

**Correo 2 — Día 1**
- Asunto: la primera victoria rápida
- Contenido: le enseña a hacer algo simple que da resultado en los primeros minutos
- CTA: hacer esa acción

**Correo 3 — Día 3**
- Asunto: el error común que hay que evitar
- Contenido: lo que el 80% de los clientes hace mal al principio
- CTA: corregirlo o validarlo

**Correo 4 — Día 7**
- Asunto: ¿cómo va todo?
- Contenido: un check-in, pide comentarios, ofrece ayuda
- CTA: responder (le indica quién necesita soporte)

### Nutrición (6 correos estándar, cada 2 o 3 días)

**Correo 1** — Identifica el dolor principal
**Correo 2** — Muestra que el dolor tiene solución (esperanza)
**Correo 3** — Presenta el método (su enfoque)
**Correo 4** — Prueba social / un caso
**Correo 5** — Rompe la objeción (la más grande)
**Correo 6** — Invitación a la acción (llamada, demo, compra)

### Recuperación (3 correos)

**Correo 1 — "Lo he extrañado"**
- Asunto: personal, todavía sin descuento
- Contenido: usted desapareció, ¿todo bien?
- CTA: responder o hacer clic para continuar

**Correo 2 — Valor renovado**
- Asunto: qué ha cambiado desde la última vez
- Contenido: novedades, mejoras, casos nuevos
- CTA: ver más

**Correo 3 — Última oportunidad / descuento**
- Asunto: una oferta específica de regreso
- Contenido: condición especial, plazo corto
- CTA: claro y directo

### Preventa / lanzamiento (5 correos, que van subiendo de intensidad)

**Correo 1 — 5 días antes** — El anuncio + el porqué (el problema que resuelve)
**Correo 2 — 3 días antes** — Los detalles + para quién es
**Correo 3 — 1 día antes** — Última vista previa + las objeciones respondidas
**Correo 4 — El día, con la apertura** — "Ya está abierto"
**Correo 5 — El penúltimo o el último día** — El cierre es inminente

### Posventa (3 correos)

**Correo 1 — Día 7** — ¿Cómo lo está usando?
**Correo 2 — Día 14** — Pide una reseña o un testimonio si está satisfecho
**Correo 3 — Día 30** — Mejora / próximo paso

---

## Fase 5 — Escribir cada correo

Para cada correo de la secuencia, genera:

```markdown
## Correo N — {{título interno del correo}}

**Envío:** {{cuándo — ej.: "Inmediato después de suscribirse" o "Día 3, 9 a. m."}}
**Asunto (3 variaciones):**
1. {{variación 1}}
2. {{variación 2}}
3. {{variación 3}}

**Preencabezado:** {{1 frase, 60 a 90 caracteres}}

**Cuerpo:**

{{el texto completo del correo — usa la voz de me.md, párrafos cortos, saltos generosos}}

**CTA principal:** {{el texto del botón o del enlace}}
**CTA secundario (P. D.):** {{si aplica}}
```

Cada correo: de 150 a 400 palabras en el cuerpo (los cortos funcionan mejor en una secuencia).

---

## Fase 6 — Guardar

Crea la carpeta:
```bash
mkdir -p "04 Resources/textos/secuencias-email"
```

Guarda en `04 Resources/textos/secuencias-email/YYYY-MM-DD-{{tipo}}-{{slug-de-la-oferta}}.md`.

Frontmatter:
```yaml
---
type: email-sequence
status: draft
date: YYYY-MM-DD
tags: [email, secuencia, {{tipo}}]
tipo: {{bienvenida / onboarding / nutricion / etc.}}
oferta: {{nombre corto}}
cadencia: {{la de la Fase 3}}
total_correos: {{N}}
---
```

---

## Fase 7 — Confirmación

> "Secuencia de {{tipo}} guardada en `04 Resources/textos/secuencias-email/{{archivo}}`. {{N}} correos, cadencia {{X}}.
>
> Próximos pasos:
> 1. Revisar cada correo — si alguno le suena genérico, ajústelo
> 2. Escoger 1 asunto por correo (haga una prueba A/B si la plataforma lo permite)
> 3. Subirlos a la plataforma de correo
> 4. Configurar el disparador y la cadencia
>
> Para otra secuencia: `/secuencia-email` otra vez. Para adaptar 1 correo a LinkedIn: `/linkedin`, pegando el contenido."

---

## Reglas

- Cada correo es independiente — el lector puede leer 1 sin haber leído el anterior
- El asunto siempre humano, nunca "Newsletter #N" ni el nombre de la empresa al comienzo
- La P. D. es la parte más leída — úsala con estrategia
- Un CTA principal explícito, 1 solo por correo (no lo diluyas)
- La voz de `me.md`, y nunca "espero que estés bien"
- En la bienvenida, NUNCA intentes vender en el correo 1 — ahí solo se entrega
- En la recuperación, NUNCA arranques con un descuento — arranca por lo personal
