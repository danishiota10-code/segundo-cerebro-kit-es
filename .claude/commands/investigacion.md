---
description: Investigación profunda multifuente — define la pregunta, planea las fuentes, busca en paralelo, sintetiza con citas, y guarda en el vault en un formato listo para usar
---

# Investigación — Deep research multifuente

Vas a hacer una investigación estructurada sobre cualquier tema — un competidor, un mercado, una tecnología, una persona, un marco de trabajo — y entregar un documento navegable con citas verificables.

---

## Idioma / Language

Detecta el idioma. Español por defecto. Deja las citas en su idioma original (no traduzcas las fuentes).

---

## Fase 1 — Definir la pregunta

La mayoría de las investigaciones falla porque la pregunta es vaga. Refínala antes de buscar.

Pregunta:
> "¿Sobre qué quiere investigar? Cuéntemelo en 1 a 3 frases."

Después de la respuesta, reformula la pregunta en formato de decisión. Presenta 2 o 3 versiones:

> "Posibles encuadres de su investigación:
> 1. {{encuadre 1 — específico, con un criterio de decisión}}
> 2. {{encuadre 2}}
> 3. {{encuadre 3}}
>
> ¿Cuál refleja mejor lo que necesita saber? O escriba su propia versión."

Espera la elección. Confirma la pregunta antes de seguir.

**Ejemplos de una buena pregunta:**
- "¿Cuáles 3 herramientas de email marketing tienen mejor entregabilidad para B2B en Colombia en 2026, y cuál es el sacrificio de cada una?"
- "¿Cómo creció {{la empresa X}} de Y a Z en 18 meses — cuáles fueron los 3 a 5 movimientos principales?"
- "¿Qué marcos de precios funcionan para un SaaS B2B con un ticket por encima de USD 500 al mes?"

**Señales de una pregunta mala:**
- "Cuénteme sobre {{tema}}" — demasiado amplia
- "Todo sobre {{empresa}}" — no tiene criterio
- "¿{{Tema}} es bueno?" — sin una definición de "bueno"

---

## Fase 2 — Plan de investigación

Presenta el plan antes de ejecutarlo:

> "Plan de investigación para '{{la pregunta refinada}}':
>
> **Fuentes que voy a consultar:**
> 1. {{fuente 1 — ej.: 'El sitio oficial y el blog de la empresa'}}
> 2. {{fuente 2 — ej.: 'G2, Capterra, Trustpilot'}}
> 3. {{fuente 3 — ej.: 'Reddit r/Marketing, los hilos relevantes'}}
> 4. {{fuente 4 — ej.: 'Análisis de Forrester / Gartner, si son gratuitos'}}
> 5. {{fuente 5 — ej.: 'Entrevistas de los fundadores en pódcast'}}
>
> **Lo que voy a entregar:**
> - {{entregable 1 — ej.: 'Un comparativo de 3 herramientas'}}
> - {{entregable 2 — ej.: 'Los sacrificios de cada una, explícitos'}}
> - {{entregable 3 — ej.: 'Una recomendación contextualizada a su caso'}}
>
> Me va a tomar unos {{N}} minutos. ¿Sigo?"

Espera un "sí" o un ajuste. No empieces sin confirmación.

---

## Fase 3 — Niveles de fuente

Clasifica las fuentes en 3 niveles. Prioriza el Nivel 1.

**Nivel 1 — Fuentes primarias (alta confianza):**
- El sitio oficial, el blog y la documentación de lo que está investigando
- Entrevistas en video o pódcast con los fundadores
- Documentos públicos (S-1, 10-K, si es una empresa pública)
- Artículos académicos
- Datos de organismos oficiales (Banco de la República, DANE, Invima, Superintendencia Financiera, etc.)

**Nivel 2 — Análisis secundarios confiables:**
- Reseñas en G2, Capterra, Trustpilot, TrustRadius (fíjate en las de 3 y 4 estrellas)
- Análisis de Forrester, Gartner, IDC (una parte es gratuita)
- TechCrunch, The Verge, Stratechery, Lenny's Newsletter (según el tema)
- Casos de uso publicados por el propio cliente

**Nivel 3 — Percepción y contexto:**
- Reddit (hilos específicos, no la publicación principal)
- Discusiones de HackerNews
- Publicaciones de LinkedIn de gente relevante
- Hilos de Twitter de quien trabaja en el sector
- Quora / Stack Exchange

Si un dato aparece solo en el Nivel 3, márcalo como "sin confirmar" en el informe final.

---

## Fase 4 — Ejecutar

Haz WebSearch + WebFetch en paralelo sobre las fuentes definidas. Para cada hallazgo:
- Anota la cita exacta (URL, fecha, autor si lo hay)
- Clasifícalo por nivel
- Marca su relevancia (alta/media/baja) para la pregunta

No inventes. Si no encontraste algo, márcalo como un vacío explícito.

---

## Fase 5 — Sintetizar

Estructura del informe:

```markdown
# Investigación: {{la pregunta refinada}}

**Fecha:** YYYY-MM-DD
**Fuentes consultadas:** {{N}}
**Nivel 1:** {{N}} | **Nivel 2:** {{N}} | **Nivel 3:** {{N}}

---

## En resumen

{{3 a 5 viñetas con los hallazgos principales. Cada una con 1 enlace a su fuente al lado.}}

---

## Respuesta directa

{{2 a 4 párrafos que responden la pregunta de la Fase 1. Citas en línea con el formato [^1], [^2].}}

---

## Análisis detallado

### {{Subtema 1}}

{{Párrafo con el análisis. Citas en línea.}}

**Fuentes consultadas en este subtema:**
- [^1] {{cita 1}}
- [^2] {{cita 2}}

### {{Subtema 2}}

(igual)

### {{Subtema 3}}

(igual)

---

## Comparativo (si aplica)

| Ítem | Criterio A | Criterio B | Criterio C | Fuente |
|---|---|---|---|---|
| {{X}} | ... | ... | ... | [^N] |

---

## Puntos donde las fuentes no coinciden

{{Dónde se contradicen las fuentes. Demuestra que no escogiste solo lo que te convenía. Lista las contradicciones.}}

---

## Vacíos / Lo que no se pudo confirmar

- {{vacío 1}}
- {{vacío 2}}

Cómo llenar esos vacíos: {{sugerencia — ej.: "una entrevista con un cliente de {{X}}", "acceso al informe pago de Forrester"}}

---

## Recomendación

{{2 a 4 párrafos con la recomendación contextualizada para quien pidió la investigación. No te quedes en la mitad — toma posición con base en la evidencia, aunque sea con salvedades.}}

---

## Próximas preguntas

{{2 o 3 preguntas que abrió esta investigación — para el siguiente ciclo, si hace falta}}

---

## Fuentes (todas)

[^1]: {{URL}}, consultada el {{fecha}}. Nivel {{1/2/3}}.
[^2]: {{URL}}, consultada el {{fecha}}. Nivel {{1/2/3}}.
{{etc.}}
```

---

## Fase 6 — Guardar

Crea la carpeta:
```bash
mkdir -p "03 Intelligence/research"
```

Guarda en `03 Intelligence/research/YYYY-MM-DD-{{slug-de-la-pregunta}}.md`.

Frontmatter:
```yaml
---
type: research
status: complete
date: YYYY-MM-DD
tags: [investigacion, {{etiquetas relevantes}}]
pregunta: {{la pregunta refinada}}
fuentes_nivel_1: {{N}}
fuentes_nivel_2: {{N}}
fuentes_nivel_3: {{N}}
---
```

---

## Fase 7 — Confirmación

> "Investigación guardada en `03 Intelligence/research/{{archivo}}`. {{N}} fuentes consultadas.
>
> Hallazgos principales: {{3 viñetas cortas}}
>
> Vacíos identificados: {{N}}.
>
> Para la próxima investigación: `/investigacion` otra vez. Para volver esto contenido: `/escribir` o `/linkedin`."

---

## Reglas

- **Nunca inventes una fuente.** Si no lograste entrar a una URL, márcala como intentada y fallida; no adivines el contenido.
- **Cita todo.** Toda afirmación factual lleva su `[^N]` al lado.
- **Marca el nivel de cada fuente.** El Nivel 3 vale para percepción, no para un hecho.
- **No escojas solo lo que te conviene.** Muestra las divergencias de forma explícita.
- **Toma posición.** La recomendación va al final, con salvedades, pero sin quedarte en la mitad.
- **Los vacíos son honestidad.** No escondas lo que faltó.
- **No traduzcas las citas.** Déjalas en su idioma original — agrega una traducción corta entre paréntesis si ayuda.
- **Investigación actual.** Si el tema es sensible al tiempo (mercado, regulación, producto), prioriza fuentes de menos de 12 meses.
