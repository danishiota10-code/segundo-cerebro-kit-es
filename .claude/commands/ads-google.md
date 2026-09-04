---
description: Google Ads — auditoría, estructura de cuenta, planeación de campaña, copy de anuncio, elección de puja. Funciona con Search, PMax, YouTube, Display y Shopping.
---

# Google Ads — Auditar, construir, optimizar

Vas a trabajar Google Ads en 4 modos: **auditar** (analizar una cuenta), **construir** (planear una cuenta nueva), **optimizar** (mejorar una cuenta que ya corre) o **copy** (escribir el anuncio).

---

## Idioma / Language

Detecta el idioma y úsalo en todo. Español por defecto.

---

## Fase 1 — El modo

Pregunta vía AskUserQuestion:

- Pregunta: "¿Qué quiere hacer con Google Ads?"
- Header: `Modo`
- Opciones:
  - `Auditar — analizar una cuenta existente` — "Usted pega los datos o exporta un CSV, y yo diagnostico."
  - `Construir — montar una cuenta nueva` — "Defino la estrategia, la estructura y la primera campaña."
  - `Optimizar — mejorar una cuenta que ya corre` — "Identifico dónde se está desangrando o dónde se puede escalar."
  - `Copy — escribir los anuncios` — "RSA listos para subir."

Cada modo es independiente. Salta directo a la fase que corresponda.

---

## Modo: Auditar

### Auditar 1 — Requisitos previos

Pregunta:
> "Para auditar necesito datos. ¿Qué puede compartirme?"
> 1. Pantallazos de la cuenta — panorama, campañas, conversiones
> 2. Un export en CSV de las campañas de los últimos 30 a 90 días
> 3. Acceso de lectura a la cuenta (comparta el correo)
> 4. Solo los números clave (gasto, conversiones, CPA, ROAS)"

Acepta lo que el usuario ofrezca. Entre más datos, mejor el diagnóstico.

### Auditar 2 — Lista de verificación crítica

Evalúa cada ítem. Marca ✓ / ⚠️ / ❌:

**Medición de conversiones**
- ✓ El píxel o la etiqueta está bien instalado
- ✓ Las conversiones marcadas como "primary" (no "secondary")
- ✓ Las conversiones importantes son las que cuentan (compra o lead, no clics de botón)
- ✓ Enhanced conversions activado
- ✓ Modelo de atribución apropiado (data-driven, si se puede)

**Estructura**
- ⚠️ Campañas separadas por intención (search vs. PMax vs. YouTube)
- ⚠️ Grupos de anuncios con un tema único (no un "mercadeo general" que amontona 50 palabras clave)
- ⚠️ Tipos de concordancia apropiados (la amplia solo con Smart Bidding)
- ❌ Palabras clave negativas aplicadas (una lista que crece)

**Palabras clave (Search)**
- ⚠️ Quality Score promedio por encima de 6
- ⚠️ Cuota de impresiones — que no se esté perdiendo por presupuesto ni por ranking
- ❌ Términos de búsqueda revisados cada semana
- ⚠️ Grupos de anuncios de una sola palabra clave (SKAG) solo donde se justifique

**Performance Max**
- ⚠️ Grupos de recursos bien segmentados (no 1 solo para toda la cuenta)
- ⚠️ Señales de audiencia aplicadas (no dejar que PMax adivine)
- ✓ La expansión de URL final bien configurada
- ⚠️ Listas de exclusión de marca activadas (si aplica)

**Puja**
- ⚠️ La estrategia de puja compatible con el volumen de conversiones (mínimo 30 a 50 al mes para Smart Bidding)
- ❌ CPA o ROAS objetivo realista (no un 50% por debajo del promedio actual)
- ⚠️ Estrategias de puja de portafolio usadas cuando tengan sentido

**Anuncios (RSA)**
- ✓ 15 titulares y 4 descripciones por anuncio
- ⚠️ Eficacia del anuncio en "Buena" o "Excelente"
- ❌ Titulares duplicados eliminados
- ⚠️ El fijado usado con cuidado (le limita el margen al aprendizaje automático)
- ⚠️ Extensiones activas: sitelinks, textos destacados, fragmentos estructurados, formularios de lead, ubicación

**Presupuesto y ritmo**
- ⚠️ Presupuesto diario proporcional al CPA objetivo
- ❌ Que las campañas que pierden cuota de impresiones por presupuesto sean las importantes
- ⚠️ Ritmo de gasto — que sea uniforme y no se agote en la primera semana

**Landing pages**
- ❌ Coincidencia entre el anuncio y la landing (el titular de la landing refleja la palabra clave)
- ⚠️ La landing carga en menos de 3 segundos en móvil
- ⚠️ El formulario en la primera pantalla, o un CTA fuerte
- ⚠️ El Quality Score sufre si la landing es genérica

### Auditar 3 — Gasto desperdiciado

Identifica dónde se está desangrando:
1. Palabras clave con un CPA de más del doble del promedio y sin conversiones en los últimos 30 días
2. Términos de búsqueda irrelevantes (por ejemplo, palabras clave genéricas que traen a gente que no compra)
3. Ubicaciones que gastan pero no convierten
4. Dispositivos que gastan pero no convierten
5. Audiencias negativas que deberían estar y no están
6. Días y horas con CPA alto y sin ajuste

### Auditar 4 — Informe

Genera el informe:

```markdown
# Auditoría de Google Ads — {{Cliente / Cuenta}}

**Fecha:** YYYY-MM-DD
**Periodo analizado:** {{fechas}}
**Gasto:** ${{valor}}
**Conversiones:** {{N}}
**CPA actual:** ${{valor}}
**ROAS actual:** {{N}}x

---

## Puntaje por categoría

| Categoría | Estado |
|---|---|
| Medición de conversiones | ✓ / ⚠️ / ❌ |
| Estructura | ... |
| Palabras clave | ... |
| Performance Max | ... |
| Puja | ... |
| Anuncios | ... |
| Presupuesto | ... |
| Landing pages | ... |

---

## Críticos (corregir esta semana)

{{La lista, con la corrección sugerida para cada uno}}

---

## Gasto desperdiciado identificado

- {{Ítem}} — ${{X}} al mes que se ahorran si se corrige
- {{Ítem}} — ${{Y}} al mes

**Ahorro potencial total:** ${{suma}} al mes

---

## Oportunidades de escala

{{Dónde se puede invertir más con confianza}}

---

## Plan de acción — 30 días

**Semana 1:**
- {{acción}}

**Semana 2:**
- {{acción}}

**Semanas 3 y 4:**
- {{acción}}
```

---

## Modo: Construir

### Construir 1 — Trabajo previo

Haz 4 preguntas, una a la vez:

**1. Objetivo de negocio**
- Pregunta: "¿Cuál es el objetivo concreto? No 'tráfico', sino algo como 'X leads al mes a un CPA de $Y' o 'un ROAS de Z en ventas'."

**2. El embudo**
- Pregunta: "Mapee el camino: clic en el anuncio → ... → conversión. ¿Dónde empieza, dónde termina? ¿Cuál es el evento principal (compra, lead calificado, demo)?"

**3. Presupuesto mensual**
- Pregunta: "¿Cuánto piensa invertir al mes? (define si el Smart Bidding funciona — necesita unas 30 a 50 conversiones mensuales por campaña para salir del aprendizaje)"

**4. Competencia**
- Pregunta: "¿Quiénes son sus principales competidores en Google? (lo voy a usar para Auction Insights y para la estructura de palabras clave negativas)"

### Construir 2 — Escoger el tipo de campaña

| Objetivo | Tipo recomendado | Por qué |
|---|---|---|
| Capturar demanda existente (alguien ya busca el problema) | **Search** | Mayor intención, mejor control |
| Vender un producto físico en e-commerce | **PMax + Shopping** | Cobertura total de las superficies de Google |
| Construir awareness en una audiencia específica | **YouTube** (Demand Gen o TrueView) | Video + segmentación |
| Ventas de e-commerce sin un catálogo grande | **Shopping** (manual) | Control del feed |
| Remarketing a quien ya visitó el sitio | **Display + PMax** | Cobertura barata |
| Ventas B2B con ticket alto | **Search + LinkedIn Ads** (combinados) | Search captura la demanda y LinkedIn apunta al perfil |

Recomienda según las respuestas. Justifícalo.

### Construir 3 — Estructura

Define:
- Cuántas campañas (el mínimo necesario, no maximizar)
- Cuántos grupos de anuncios por campaña (3 a 5 es lo estándar)
- Los tipos de concordancia
- La estructura de palabras clave (SKAG vs. grupos temáticos)
- Las audiencias por aplicar (señales en PMax, observación en Search)
- Las listas de palabras clave negativas

### Construir 4 — La puja

Escoge según el volumen esperado:

| Conversiones al mes | Estrategia |
|---|---|
| 0 a 15 | Maximizar conversiones (sin CPA objetivo) |
| 15 a 30 | Maximizar conversiones + un CPA objetivo suave |
| 30 o más | CPA objetivo |
| 50 o más con ingresos variables | ROAS objetivo |

### Construir 5 — Plan de los primeros 30 días

Semana 1: montar la cuenta + 1 campaña piloto
Semana 2: evaluar el Quality Score, ajustar concordancias, ampliar palabras clave
Semana 3: agregar la 2ª campaña, ampliar
Semana 4: evaluar las conversiones, ajustar la puja

Guarda el plan completo en `04 Resources/ads/google/{{slug}}-plan-construccion.md`.

---

## Modo: Optimizar

Pregunta:
> "¿Quiere optimizar para bajar el CPA, para escalar volumen, o para mejorar el ROAS?"

Cada uno tiene su camino:

**Bajar el CPA:** gasto desperdiciado, palabras clave / ubicaciones / dispositivos malos, ajustar la puja a algo más conservador, más negativas.

**Escalar volumen:** presupuesto, expansión (concordancia amplia con Smart Bidding), audiencias nuevas, tipos de campaña nuevos (Display o YouTube de apoyo).

**Mejorar el ROAS:** enfocarse en los productos o SKU más rentables, ajustar el feed, las audiencias que más compran, pujas diferenciadas por categoría.

El diagnóstico sale de los datos que comparta el usuario.

---

## Modo: Copy

### Copy 1 — Briefing

Haz 4 preguntas:

**1. Producto / oferta**
- Pregunta: "¿Qué está anunciando? En 1 frase."

**2. Público**
- Pregunta: "¿Quién busca esto? ¿Qué habrá escrito probablemente en Google para ver su anuncio?"

**3. Diferencial**
- Pregunta: "¿Qué tiene usted que nadie más tiene? (O: qué hace que alguien le haga clic al SUYO en vez del de la competencia)"

**4. CTA**
- Pregunta: "¿Qué quiere que haga la persona? ¿Comprar, agendar, descargar, llamar?"

### Copy 2 — Generar el RSA completo

Estructura del RSA: 15 titulares (30 caracteres cada uno), 4 descripciones (90 caracteres cada una).

```markdown
## Anuncio — {{producto / campaña}}

### Titulares (15)

**Fijados en la posición 1 (3 titulares con la palabra clave principal):**
1. {{titular con la palabra clave}}
2. {{titular con la palabra clave}}
3. {{titular con la palabra clave}}

**Sin fijar (12 titulares variados):**
4. {{el beneficio principal}}
5. {{prueba / número}}
6. {{CTA directo}}
7. {{urgencia / escasez, si aplica}}
8. {{contra la competencia / el diferencial}}
9. {{garantía}}
10. {{prueba social}}
11. {{el público objetivo, explícito}}
12. {{pregunta provocadora}}
13. {{beneficio secundario}}
14. {{característica única}}
15. {{variación del llamado a la acción}}

### Descripciones (4)

1. {{descripción completa de lo que entrega + CTA}}
2. {{descripción enfocada en la prueba o el resultado}}
3. {{descripción enfocada en para quién es}}
4. {{descripción con una objeción respondida + CTA}}

### Extensiones sugeridas

**Sitelinks (4 a 6):**
- {{enlace}} — {{descripción}}

**Textos destacados (5 a 8):**
- {{beneficio corto}}

**Fragmentos estructurados:**
- Encabezado: {{Tipos / Marcas / Cursos / etc.}}
- Valores: {{lista}}

**Formulario de lead (si aplica):**
- Titular + descripción
- Campos: {{la lista mínima}}
```

---

## Guardar (en todos los modos)

Crea la carpeta:
```bash
mkdir -p "04 Resources/ads/google"
```

Guarda en `04 Resources/ads/google/YYYY-MM-DD-{{modo}}-{{slug}}.md`.

Frontmatter:
```yaml
---
type: ads-google
modo: {{auditar / construir / optimizar / copy}}
status: complete
date: YYYY-MM-DD
tags: [ads, google, {{modo}}]
---
```

---

## Confirmación

> "Guardado en `04 Resources/ads/google/{{archivo}}`.
>
> Próximos pasos:
> {{varían según el modo}}
>
> Para Meta Ads: corra `/ads-meta` (todavía no está en este kit — pídalo para la próxima versión si lo necesita).
> Para reutilizar el anuncio en LinkedIn: `/linkedin`."

---

## Reglas

- No inventes números. Si el usuario no los dio, pídelos o marca `{{verificar}}`.
- El Smart Bidding necesita volumen — no recomiendes CPA objetivo para una cuenta con 5 conversiones al mes.
- El Quality Score es un indicador indirecto, no la meta — la meta es el CPA o el ROAS.
- Ten siempre en cuenta la landing — un buen anuncio + una mala landing = plata perdida.
- No digas "siga las mejores prácticas" — di cuál práctica y por qué.
