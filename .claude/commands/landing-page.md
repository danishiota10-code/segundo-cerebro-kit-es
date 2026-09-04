---
description: Crea un brief completo de landing page — posicionamiento, titular con 3 variaciones, estructura de secciones y copy sección por sección
---

# Landing Page — Brief completo

Vas a entrevistar al usuario con 6 preguntas cortas y después generar un brief accionable de landing page y guardarlo en el vault.

---

## Idioma / Language

Detecta el idioma del mensaje que invocó este comando y úsalo en todas las preguntas, headers, opciones y en el brief final.
- Español por defecto. Inglés o portugués si el usuario escribió en ese idioma.

---

## Antes de empezar

Lee `02 Context/me.md` si existe. Usa los datos de voz, audiencia y canales para anclar el tono del brief. Si el archivo no existe, sigue con base en las respuestas del usuario.

Si existe, menciónalo en el primer mensaje:
> "Ya vi su `me.md`. Voy a usar su voz y su contexto para anclar la página. Le hago 6 preguntas rápidas — puede saltarse cualquiera."

Si no existe:
> "Le voy a hacer 6 preguntas para armar el brief de la landing page. Puede saltarse cualquiera respondiendo 'saltar'."

---

## 6 preguntas (una a la vez, vía AskUserQuestion)

**P1 — La oferta**
- Pregunta: "¿Qué está vendiendo en esta página? Descríbalo en una frase: producto o servicio, formato, y qué se lleva el cliente."
- Header: `Oferta`
- Opciones: `Servicio (consultoría, agencia)` / `Producto digital (curso, ebook, comunidad)` / `SaaS / app` / `Evento / mentoría` / `Saltar`

**P2 — El público específico**
- Pregunta: "¿Para quién es esta página? Sea específico — no 'empresarios', sino algo como 'el fundador solo de un SaaS B2B con 1 a 5 empleados'."
- Header: `Público`
- Opciones: `Empleado` / `Freelance / consultor` / `Dueño de negocio` / `Otro creador / mentor` / `Saltar`

**P3 — El resultado prometido**
- Pregunta: "¿Qué transformación concreta va a tener el cliente después de comprar? Use un número si se puede (ej.: 'pasar de un CAC de $200.000 a uno de $80.000 en 60 días')."
- Header: `Resultado`
- Opciones: `Resultado financiero (más leads, ventas, ROI)` / `Resultado de tiempo (más rápido, automatizado)` / `Resultado de transformación (habilidad, posicionamiento)` / `Saltar`

**P4 — Las objeciones principales**
- Pregunta: "¿Cuáles son las 2 o 3 objeciones más grandes de ese público? ¿Qué hace que NO compre? (ej.: 'ya intenté algo así y no funcionó', 'no tengo tiempo', 'muy caro')"
- Header: `Objeciones`
- Opciones: `Precio / presupuesto` / `Tiempo / esfuerzo` / `Confianza / riesgo` / `Ya intenté algo parecido` / `Saltar`

**P5 — La fuente de tráfico**
- Pregunta: "¿De dónde va a llegar la mayoría a esta página? Eso cambia el tono del hook."
- Header: `Tráfico`
- Opciones: `Pauta paga (Meta, Google)` / `LinkedIn orgánico` / `Correo / newsletter` / `Referidos / voz a voz` / `Saltar`

**P6 — El CTA principal**
- Pregunta: "¿Cuál es la acción principal que quiere que tome la persona?"
- Header: `CTA`
- Opciones: `Comprar ahora` / `Agendar una llamada o demo` / `Entrar a la lista de espera` / `Descargar / inscribirse gratis` / `Saltar`

---

## Generación del brief

Con las respuestas + el contexto de `me.md` (si existe), genera el brief completo en markdown. Trabaja en silencio, no lo narres.

Estructura del brief:

```markdown
---
type: brief
status: draft
date: YYYY-MM-DD
tags: [landing-page, brief]
proyecto: {{slug-de-la-oferta}}
---

# Landing Page — {{Nombre de la oferta}}

## Posicionamiento
{{1 frase clara: para quién es, qué hace, cuál es el resultado único}}

## Titular (3 variaciones)

**Variación 1 — Resultado claro:**
{{titular enfocado en el resultado tangible}}

**Variación 2 — Dolor + solución:**
{{titular que nombra el dolor y presenta la salida}}

**Variación 3 — Posicionamiento a contracorriente:**
{{titular que va contra el sentido común del mercado}}

## Subtitular
{{1 o 2 frases que expanden el titular con una prueba o con especificidad}}

## Estructura de secciones

### 1. Hero
- Titular + subtitular (arriba)
- CTA primario: "{{el texto del CTA}}"
- Visual sugerido: {{descripción corta de qué mostrar}}

### 2. Dolor / Situación actual
{{2 o 3 párrafos que describen el dolor del público en sus propias palabras. Usa la voz del cliente si está en me.md.}}

### 3. Solución / Cómo funciona
{{Cómo lo resuelve su oferta. 3 viñetas o 3 pasos claros.}}

### 4. Resultado / Transformación
{{Qué cambia en la vida del cliente. Usa los números de la P3.}}

### 5. Prueba social
{{El tipo de prueba que tenga sentido para esta oferta: testimonios, números, logos, antes y después.}}

### 6. Objeciones respondidas
{{Para cada objeción de la P4, escribe la respuesta directa, sin rodeos.}}

### 7. La oferta en detalle
{{Qué está incluido, el formato de entrega, el plazo, la garantía si la hay.}}

### 8. Preguntas frecuentes
{{4 a 6 preguntas que cubran dudas técnicas, del proceso y de la posventa.}}

### 9. CTA final
{{Titular corto + botón. Usa el texto del CTA de la P6.}}

## 3 variaciones de CTA

1. {{CTA directo: "Comprar ahora", "Agendar llamada"}}
2. {{CTA enfocado en el beneficio: "Quiero {{resultado}}"}}
3. {{CTA con urgencia o exclusividad, si tiene sentido}}

## Notas de copy

- **Tono de voz:** {{el de me.md, o inferido de la P5}}
- **Palabras que hay que usar:** {{las de me.md, "palabras que uso"}}
- **Palabras que hay que evitar:** {{las de me.md, "palabras que NUNCA uso"}}
- **Ángulo único:** {{lo que tiene esta oferta que nadie más tiene}}

## Próximos pasos

- [ ] Escoger el titular final (probar A/B si se puede)
- [ ] Escribir el copy completo, sección por sección (puede correr `/escribir` para cada una)
- [ ] Validar los hooks con 3 personas del público antes de publicarla
- [ ] Configurar el tracking (píxel + GA + conversión)
```

---

## Guardar

Guarda en `04 Resources/landing-pages/{{slug-de-la-oferta}}.md`.

Genera el slug a partir del nombre de la oferta: minúsculas, con guiones, sin tildes. Ejemplo: "Mentoría Claude Code" → `mentoria-claude-code.md`.

Si la carpeta no existe, créala:
```bash
mkdir -p "04 Resources/landing-pages"
```

---

## Confirmación final

Un mensaje corto:

> "Brief creado en `04 Resources/landing-pages/{{slug}}.md`.
>
> Para escribir el copy sección por sección: `/escribir`.
> Para revisarlo antes de publicar: abra el archivo y edite lo que no le cuadre."

---

## Reglas

- Usa el lenguaje de `me.md` siempre que se pueda — no inventes una voz.
- Los titulares llevan siempre un número o una especificidad cuando la P3 mencione un resultado cuantificado.
- Si el usuario se saltó todo, genera el brief con placeholders claros y avisa que quedó con datos mínimos.
- Guarda siempre, incluso si quedó incompleto.
