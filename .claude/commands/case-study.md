---
description: Crea un caso de estudio completo de un cliente — extrae la narrativa de una transcripción o de notas, la estructura en un formato presentable, y genera markdown listo para volverse PDF o diapositivas
---

# Case Study — Presentación del resultado de un cliente

Vas a construir 1 caso de estudio completo: contexto, problema, enfoque, resultado, lecciones. En un formato que sirva para el sitio web, un sales deck, un post o un PDF.

---

## Idioma / Language

Detecta el idioma y úsalo en todo. Español por defecto.

---

## Antes de empezar

Lee `02 Context/me.md`:
- "A qué me dedico" — para entender qué vende
- "Audiencia" — para quién es el caso (clientes potenciales parecidos)

---

## Fase 1 — El material de partida

Pregunta vía AskUserQuestion:

- Pregunta: "¿De dónde sale el caso?"
- Header: `Fuente`
- Opciones:
  - `Transcripción de una llamada con el cliente` — "Pegue el texto en bruto."
  - `Notas que escribí sobre el proyecto` — "Pegue las notas y yo las organizo."
  - `Se lo cuento ahora — usted pregunta` — "Lo entrevisto por texto, pregunta por pregunta."
  - `Ya tengo un borrador — lo pego` — "Usted lo pega y yo lo reestructuro."

Actúa según la elección:
- Transcripción / Notas / Borrador: pide que pegue el contenido, léelo y sigue a la Fase 2.
- Se lo cuento ahora: ve a la Fase 1b (entrevista guiada).

### Fase 1b — Entrevista guiada (solo si escogió "Se lo cuento ahora")

Haz 8 preguntas, una a la vez, vía AskUserQuestion:

**1. Cliente**
- Pregunta: "¿Quién es el cliente? Nombre (o anonimizado), sector, tamaño de la empresa."

**2. Situación inicial**
- Pregunta: "¿Cuál era su situación antes de que usted entrara? ¿Dónde estaba trabado?"

**3. Intentos anteriores**
- Pregunta: "¿Qué había intentado antes? (importante para mostrar el contraste)"

**4. Por qué lo escogió a usted**
- Pregunta: "¿Por qué lo escogió a usted específicamente? ¿Qué inclinó la contratación?"

**5. Su enfoque**
- Pregunta: "¿Cómo trabajó? ¿Cuáles fueron los pasos, la estrategia, el método?"

**6. Resultado cuantificado**
- Pregunta: "¿Cuál fue el resultado en números? (ingresos, leads, tiempo, eficiencia, etc.) ¿En qué periodo?"

**7. Resultado cualitativo**
- Pregunta: "¿Cómo le cambió el día a día o la vida al cliente? (una cita textual de él, si la tiene, es oro)"

**8. Lección extraída**
- Pregunta: "Una lección de este proyecto que se haya llevado a otros clientes."

---

## Fase 2 — Estructurar

Con el material en la mano, organízalo en la estructura clásica de caso de estudio:

```markdown
# {{Cliente}} — {{el resultado en 1 frase cuantificada}}

> {{Cita corta del cliente, 1 o 2 líneas, si la hay}}

---

## Sobre el cliente

- **Sector:** {{industria}}
- **Tamaño:** {{N empleados / facturación, si es relevante}}
- **Ubicación:** {{ciudad o país, si es relevante}}
- **Foco:** {{el producto o servicio que venden}}

---

## El problema

{{2 o 3 párrafos. Usa las palabras del cliente siempre que se pueda. Muestra un dolor concreto, no genérico. Cuantifícalo si se puede ("se les iban 4 horas al día en X").}}

### Intentos anteriores

{{1 párrafo. Qué intentaron antes y por qué no funcionó. Muestra que el cliente no era ingenuo — ya había buscado solución.}}

---

## Por qué nos escogieron

{{1 o 2 párrafos. Honesto. Qué marcó la diferencia. Puede ser una referencia, un enfoque específico, o el momento justo.}}

---

## El enfoque

{{2 a 4 párrafos O una lista numerada. Cómo trabajó usted. Específico — no "consultoría estratégica", sino "hicimos un taller de 3 horas para mapear X, y después implementamos Y en sprints de 2 semanas".}}

### Decisiones principales

- {{decisión 1 y por qué}}
- {{decisión 2 y por qué}}
- {{decisión 3 y por qué}}

---

## El resultado

### En números

| Métrica | Antes | Después | Variación |
|---|---|---|---|
| {{ej.: CAC}} | {{$200.000}} | {{$80.000}} | {{-60%}} |
| {{ej.: Tiempo de respuesta}} | {{4 h}} | {{15 min}} | {{-94%}} |
| {{ej.: Conversión de la landing}} | {{1,2%}} | {{3,8%}} | {{+217%}} |

**Periodo:** {{cuánto tiempo tomó llegar a ese resultado}}

### En la práctica

{{1 o 2 párrafos. Cómo ese número le cambió el día al cliente. Aterriza el impacto.}}

### Lo que dijo el cliente

> "{{la cita completa del cliente, si la hay}}"
>
> — **{{Nombre del cliente}}**, {{Cargo}} en {{empresa}}

---

## Lecciones del proyecto

{{2 a 4 viñetas. Qué enseñó este proyecto que sirve para otros casos. Muestra que usted aprende y generaliza.}}

---

## ¿Quiere un resultado parecido?

{{1 párrafo corto explicando cómo empezar con usted. CTA suave.}}

**Próximo paso:** {{ej.: "Agende una llamada de 30 minutos — sin costo, sin compromiso. Enlace: ..."}}
```

---

## Fase 3 — Presentar y ajustar

Presenta el caso completo. Después pregunta:

- Pregunta: "¿Cómo quedó? ¿Quiere ajustar algo?"
- Header: `Ajustes`
- Opciones:
  - `Así está bien — vamos a guardarlo`
  - `Más corto — recórtelo a 1 página`
  - `Más técnico — agregue detalles de ejecución`
  - `Más emocional — enfóquese en la transformación del cliente`
  - `Agregar más números`

Aplica los ajustes hasta que lo apruebe.

---

## Fase 4 — Anonimización (si aplica)

Pregunta:
- Pregunta: "¿El cliente autoriza usar su nombre real?"
- Header: `Anonimización`
- Opciones:
  - `Sí — se puede nombrar` — "Se mantiene todo."
  - `Anónimo — solo el sector y el tamaño` — "Cambio 'Acme Inc' por 'un cliente del sector X, con Y empleados'."
  - `Voy a preguntarle antes de publicar` — "Se mantiene el nombre en el borrador y me acuerdo de marcarlo."

Si va anónimo, reemplaza el nombre, la ciudad específica y los números demasiado identificables (la facturación total, por ejemplo).

---

## Fase 5 — Guardar

Crea la carpeta si no existe:
```bash
mkdir -p "04 Resources/casos"
```

El slug del archivo: el nombre del cliente en minúsculas y con guiones, o "anon-{sector}-{N}" si va anónimo.

Guarda en `04 Resources/casos/{{slug}}.md`:

```yaml
---
type: case-study
status: {{draft / approved / public}}
date: YYYY-MM-DD
tags: [caso, {{sector}}, {{tipo-de-resultado}}]
cliente: {{nombre o "anónimo"}}
sector: {{sector}}
metrica_principal: {{el resultado en 1 frase}}
publicable: {{true/false}}
---
```

---

## Fase 6 — Confirmación

> "Caso guardado en `04 Resources/casos/{{archivo}}`.
>
> Estado: {{draft / approved / public}}.
>
> Próximos pasos:
> 1. Si todavía es borrador, mandárselo al cliente para que lo apruebe
> 2. Cuando lo apruebe, marcar `status: approved` en el frontmatter
> 3. Reutilizarlo: correr `/escribir` o `/linkedin` para volverlo un post corto
> 4. Para un deck de ventas: pasar el contenido a diapositivas (Canva, Google Slides, PPT)
>
> Para el próximo caso: `/case-study`."

---

## Reglas

- Nunca inventes un número. Si el usuario no lo dio, marca `{{verificar}}` y sigue.
- La cita del cliente solo va si él la dijo de verdad — no la inventes.
- Si va anónimo, anonimiza de verdad — una descripción genérica del sector.
- Muestra el proceso, no solo el resultado — los clientes potenciales quieren entender CÓMO llegó ahí.
- Los intentos anteriores son clave — diferencian el caso de un "antes vs. después" simplista.
- Las lecciones al final muestran que usted reflexiona, no solo ejecuta.
- Tono: seguro pero honesto. Sin exageraciones tipo "transformamos el negocio en 7 días".
