---
type: index
status: active
date: 2026-05-26
tags: [index, navigation, knowledge]
---

# Knowledge Index — Tu AI OS

> **Se carga solo en cada sesión.** Este es el primer archivo que lee la IA. Úsalo para anclar conocimiento permanente — los dominios que quieres que la IA SIEMPRE sepa sin que tengas que reexplicárselos.

---

## Hub

Volver al hub central del vault: [[Home]].

---

## Cómo funciona

Cuando abres Claude Code (u otra herramienta) dentro de este vault, el hook `session-start.py` inyecta este archivo en el contexto inicial. Todo lo que esté listado acá, o enlazado desde acá, queda disponible para la IA de inmediato.

**Diferencia con `04 Resources/`:**
- `knowledge/` = siempre cargado (cabe poco, prioridad alta)
- `04 Resources/` = consultado bajo demanda (cabe todo, prioridad baja)

**Qué va en knowledge:**
- Los conceptos centrales de tu trabajo (copywriting, growth, SEO, etc.)
- Los marcos de trabajo que usas una y otra vez
- La visión estratégica que orienta tus decisiones
- El vocabulario y las definiciones propias de tu nicho

**Qué NO va en knowledge:**
- Las salidas de los comandos (textos, briefs) → `04 Resources/`
- Las decisiones puntuales → `03 Intelligence/decisions/`
- Las notas de reunión → `03 Intelligence/meetings/`
- Las ideas sueltas → `00 Inbox/`

---

## Dominios de conocimiento

Los archivos de abajo son plantillas para que tú las llenes según lo que exija tu trabajo. Borra las que no uses, edita las que sí, y agrega nuevas cuando aparezca un dominio recurrente.

| Archivo | Cuándo lo necesitas |
|---|---|
| [[knowledge/copywriting]] | Para escribir cualquier texto comercial (LinkedIn, correo, landing, ads) |
| [[knowledge/content-strategy]] | Para planear contenido recurrente (newsletter, blog, redes) |
| [[knowledge/personal-brand]] | Para construir reputación en línea como persona |
| [[knowledge/growth-marketing]] | Para hacer crecer audiencia, leads e ingresos |
| [[knowledge/seo-fundamentos]] | Para posicionar contenido en Google y en las IA |

---

## Cómo agregar un archivo de knowledge nuevo

1. Crea `knowledge/{dominio}.md`
2. Frontmatter:
   ```yaml
   ---
   type: knowledge
   domain: {dominio}
   status: active
   date: YYYY-MM-DD
   tags: [knowledge, {dominio}]
   ---
   ```
3. Contenido: principios + marcos de trabajo + vocabulario + referencias del dominio
4. Agrega un enlace en la tabla de arriba
5. La IA empieza a usarlo automáticamente en la próxima sesión

---

## Principios para los archivos de knowledge

- **Conciso** — el knowledge es peso permanente en el contexto. Cada palabra cuenta.
- **Principios > ejemplos** — si un principio ocupa 1 línea y un ejemplo ocupa 10, prefiere el principio.
- **Propio > genérico** — lo que TÚ crees sobre el dominio, no lo que dice un libro de mercadeo.
- **Actualizable** — cuando tu pensamiento cambie, edita el archivo. No es un texto sagrado.
- **Enlazado** — wikilinks a otros archivos de knowledge cuando haya conexión.

---

## Próximos pasos

1. Abrir cada archivo de knowledge de la lista de arriba
2. Editarlo con tu conocimiento real (borra lo genérico, deja lo que es tuyo)
3. Agregar archivos nuevos para los dominios que no ves listados pero sí usas
4. En la próxima sesión de la IA, notar que ella "sabe" de tu trabajo sin que se lo expliques

---

## Navegación

Dominios de conocimiento: [[copywriting]], [[content-strategy]], [[personal-brand]], [[growth-marketing]], [[seo-fundamentos]].

Volver al [[Home|hub central]].
