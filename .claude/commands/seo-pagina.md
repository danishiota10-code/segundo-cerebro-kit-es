---
description: Análisis SEO completo de una URL — on-page, meta tags, schema, contenido, enlaces internos, alt text, rendimiento básico. Genera un informe con prioridades.
---

# SEO Página — Análisis profundo de una URL

Auditoría de SEO sobre una página específica. Identifica problemas críticos, medios y bajos, con la corrección sugerida para cada uno.

---

## Idioma / Language

Detecta el idioma del mensaje y úsalo en el informe final. Español por defecto.

---

## Fase 1 — URL y contexto

Pregunta (si no te lo dieron ya):
> "Pegue la URL que quiere auditar. Si quiere, cuénteme el objetivo de la página en 1 frase (ventas, captación, autoridad) — ayuda a calibrar."

Si el usuario solo pegó la URL, sigue adelante. El objetivo es opcional.

---

## Fase 2 — Traer la página

Usa WebFetch para traer el HTML. Captura:
- `<title>`
- `<meta name="description">`
- `<meta property="og:*">`
- `<meta name="twitter:*">`
- Las etiquetas `<h1>`, `<h2>`, `<h3>` (en orden)
- El texto visible (el contenido)
- Los enlaces internos (del mismo dominio)
- Los enlaces externos
- Las imágenes (`<img>` con su alt)
- El schema JSON-LD (`<script type="application/ld+json">`)
- `<link rel="canonical">`
- La meta robots
- El idioma declarado (`<html lang="...">`)

Si WebFetch falla (muro de pago, sitio solo con JS, bloqueo), avísale al usuario y pídele que pegue el HTML a mano o que use otra herramienta.

---

## Fase 3 — Análisis por categoría

Evalúa cada categoría. Marca cada ítem como ✓ (bien), ⚠️ (advertencia), ❌ (crítico).

### 3.1 — Title tag
- ✓ Existe
- ✓ Tiene entre 50 y 60 caracteres
- ✓ Contiene la palabra clave principal (pídele al usuario la palabra clave objetivo si no la sabes, o dedúcela del contenido)
- ✓ Aparece la marca (opcional, pero común al final)
- ❌ No tiene texto genérico ("Inicio | Sitio") sin contexto

### 3.2 — Meta description
- ✓ Existe
- ✓ Tiene entre 140 y 160 caracteres
- ✓ Contiene la palabra clave
- ✓ Tiene un CTA implícito o explícito
- ✓ No duplica el title

### 3.3 — Open Graph
- ✓ `og:title` existe
- ✓ `og:description` existe
- ✓ `og:image` existe y mide por lo menos 1200x630
- ✓ `og:url` existe
- ✓ `og:type` apropiado (website, article, product)

### 3.4 — Twitter Card
- ✓ `twitter:card` (summary, summary_large_image)
- ✓ `twitter:title`, `twitter:description`, `twitter:image`

### 3.5 — Jerarquía de encabezados
- ❌ Exactamente 1 `<h1>` en la página
- ✓ El H1 contiene la palabra clave principal
- ✓ Los H2 organizan las secciones, en orden lógico
- ❌ Los H3 anidados dentro de un H2 (no se salta ningún nivel)
- ⚠️ H2 y H3 con palabras relacionadas con la palabra clave

### 3.6 — Contenido
- ✓ Mínimo 600 palabras (artículos largos: 1.500+)
- ✓ La palabra clave principal aparece en el primer párrafo
- ⚠️ Densidad de la palabra clave entre 0,5% y 2% (no la fuerces)
- ✓ Contenido único, no copiado
- ✓ Frases cortas (promedio de menos de 20 palabras)
- ✓ Párrafos cortos (4 líneas como máximo)
- ⚠️ Listas y viñetas usadas cuando ayudan
- ⚠️ Imágenes con pies de foto explicativos

### 3.7 — Enlaces
**Internos:**
- ✓ Por lo menos 3 enlaces internos relevantes
- ✓ Texto ancla descriptivo (nunca "haga clic aquí")
- ✓ Sin enlaces rotos (revisa una muestra)

**Externos:**
- ✓ Enlaces externos hacia fuentes con autoridad cuando se hace una afirmación
- ⚠️ `rel="noopener"` o `rel="nofollow"` según corresponda
- ✓ Se abren en una pestaña nueva cuando tiene sentido

### 3.8 — Imágenes
- ❌ Toda imagen tiene `alt` (vacío solo se acepta en las decorativas)
- ✓ Alt descriptivo, sin relleno de palabras clave
- ⚠️ Formato moderno (WebP, AVIF) si se puede
- ⚠️ Carga diferida en las imágenes que están fuera de la primera pantalla

### 3.9 — Schema (JSON-LD)
- ⚠️ El schema apropiado al tipo de página:
  - Artículo → `Article` o `BlogPosting`
  - Producto → `Product`
  - Negocio local → `LocalBusiness`
  - Preguntas frecuentes → `FAQPage`
  - Persona → `Person`
  - Receta → `Recipe`
- ✓ Schema validado (sin errores)

### 3.10 — Técnico básico
- ✓ El canonical apunta a la URL correcta
- ✓ La meta robots no bloquea la indexación (sin `noindex`)
- ✓ `<html lang="...">` declarado correctamente
- ⚠️ URL limpia, sin parámetros innecesarios
- ⚠️ HTTPS habilitado

---

## Fase 4 — Informe

Genera el informe en markdown, con 4 secciones:

```markdown
# Auditoría SEO — {{URL}}

**Fecha:** YYYY-MM-DD
**Objetivo de la página:** {{el del usuario, o "no informado"}}
**Palabra clave principal:** {{la informada o la deducida}}

---

## Puntaje general

- ✓ {{N}} puntos bien
- ⚠️ {{N}} puntos con advertencia
- ❌ {{N}} puntos críticos

**Puntaje:** {{bien}}/{{total}} = {{porcentaje}}%

---

## Críticos (corregir ya)

{{La lista de cada ítem ❌ con:
- Qué está mal
- Cómo está hoy (cita el contenido actual)
- Cómo debería quedar
- Por qué importa}}

---

## Advertencias (corregir después)

{{La lista de cada ⚠️ en el mismo formato}}

---

## Bien (mantener)

{{Una lista corta de los ✓ relevantes}}

---

## Plan de acción (priorizado)

1. {{acción concreta 1}}
2. {{acción concreta 2}}
3. {{acción concreta 3}}
... (máximo 7)

---

## Próximos pasos sugeridos

- Volver a auditar después de los cambios: `/seo-pagina` con la misma URL
- Para las otras páginas del sitio: correrlo en cada URL importante
- Para la estrategia de contenido: definir la investigación de palabras clave y los grupos temáticos
```

---

## Fase 5 — Guardar

Crea la carpeta si no existe:
```bash
mkdir -p "04 Resources/seo/auditorias"
```

Guarda en `04 Resources/seo/auditorias/YYYY-MM-DD-{{slug-del-dominio}}-{{slug-de-la-pagina}}.md`.

El slug del dominio: extráelo de la URL, quítale el `www.` y el `.com.co`. Ejemplo: `https://www.ejemplo.com.co/blog/post-1` → dominio `ejemplo`, página `blog-post-1`.

Frontmatter:
```yaml
---
type: audit
status: complete
date: YYYY-MM-DD
tags: [seo, auditoria]
url: {{la URL completa}}
puntaje: {{porcentaje}}
criticos: {{N}}
---
```

---

## Confirmación

> "Auditoría guardada en `04 Resources/seo/auditorias/{{archivo}}`.
>
> Puntaje: {{porcentaje}}%. {{N}} puntos críticos.
>
> Próximo paso: empezar por los críticos de la lista. Cuando los ajuste, corra `/seo-pagina` otra vez sobre la misma URL para ver la diferencia."

---

## Reglas

- Nunca inventes el contenido de la página — si no lograste traerlo, pídele al usuario que lo pegue.
- Si no sabes cuál es la palabra clave principal, dedúcela del título + el H1, o pregúntala explícitamente.
- No infles la nota — sé honesto sobre lo que está mal.
- No comentes cada ítem que está bien — solo los que importan.
- Usa lenguaje práctico, no jerga de SEO. El usuario puede ser principiante.
