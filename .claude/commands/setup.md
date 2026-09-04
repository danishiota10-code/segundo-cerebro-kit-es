---
description: Configura el AI OS para usted — escoge el modo (solo o empresa), pregunta por el agente, importa contexto de otra IA, hace 8 preguntas, busca contexto en enlaces o archivos, y llena el vault con datos reales
---

# Setup — Personalización del AI OS

Vas a configurar el vault en 7 fases. Ejecútalas en orden. No te saltes ninguna.

---

## Idioma / Language

Detecta el idioma del mensaje que invocó este comando (el mensaje del usuario que disparó `/setup`) y usa ese idioma en TODOS los textos visibles: el mensaje de bienvenida, el `question` y el `header` del AskUserQuestion, cada `label` y `description` de las opciones, los mensajes de estado, y la confirmación final.

- Mensaje en español → español (el estándar de este programa).
- Mensaje en inglés → traduce todas las preguntas, headers, labels y descripciones al inglés equivalente.
- Mensaje en portugués → traduce al portugués.
- Idioma ambiguo → español.

El público principal es hispanohablante, así que el español es el valor por defecto. Pero si alguien lo corre en otro idioma, adáptate por respeto. El contenido de los archivos (`02 Context/me.md`, el frontmatter, `01 Daily/`, los nombres de carpeta) se queda como está en la plantilla — no traduzcas los paths, ni las claves del frontmatter, ni los nombres de archivo.

Acepta las respuestas del usuario por intención, no por texto exacto. Si responde en un idioma distinto al de la pregunta, sigue en el idioma de él.

---

## Fase 1 — Bienvenida

Antes de cualquier pregunta, envía este mensaje corto:

> "Bienvenido. Voy a configurar su AI OS en unos pasos rápidos:
> 1. Saber si es solo o empresa (cambia la estructura)
> 2. Decidir si quiere un agente de IA persistente
> 3. Importar contexto de otra IA (opcional)
> 4. 8 preguntas cortas
> 5. Buscar más contexto en un enlace o un archivo (opcional)
>
> Puede responder 'saltar' en cualquier pregunta. Vamos."

---

## Fase 2 — Modo: solo o empresa

**Esta es la primera pregunta real y la más importante** — define toda la estructura del vault.

Pregunta vía AskUserQuestion:

- Pregunta: "¿Es usted una persona individual, o está montando esto para una empresa o un equipo?"
- Header: `Modo`
- Opciones:
  - `Solo — profesional individual (Recomendado)` — "Mezcla lo laboral y lo personal. Ideal para emprendedores solos, freelance, consultores, creadores y empleados."
  - `Empresa — equipo / organización` — "Estructura organizacional con departamentos, procesos y partes interesadas. Ideal para equipos y empresas."

Guarda la respuesta como `modo: solo | empresa`.

Acepta cualquier señal clara: "solo", "individual", "freelance", "profesional" → `solo`. "empresa", "equipo", "negocio", "organización", "agencia" → `empresa`. Ambiguo o saltado → `solo` (el valor por defecto).

**Este valor afecta todas las fases siguientes:**
- Fase 4 (importar de otra IA): el prompt cambia para un perfil personal o empresarial
- Fase 5 (las 8 preguntas): las preguntas se reformulan según el contexto personal o empresarial
- Fase 7 (construcción): carpetas, plantillas y archivos distintos para cada modo

---

## Fase 3 — Agente de IA

### 3.1 — ¿Quiere agente?

Pregunta vía AskUserQuestion:

- Pregunta: "¿Quiere un agente de IA persistente en este vault? Aprende su contexto, guarda notas automáticamente, maneja las sesiones y corre las revisiones diarias y semanales."
- Header: `Agente de IA`
- Opciones:
  - `Sí — agente completo (Recomendado)` — "Configura el agente completo, con personalización profunda, hooks y automatizaciones."
  - `No — solo la estructura de carpetas` — "Crea la estructura de carpetas sin agente persistente."

Guarda la respuesta como `agente: si | no`.

**Si `agente: no`:** salta directo a la Fase 7 (Construcción). No hagas las Fases 3.2, 4, 5 ni 6. Crea solo la estructura base y el `me.md` (modo solo) o `operator.md` + `organization.md` (modo empresa) en blanco. Avisa al final que el usuario puede volver a correr `/setup` cuando quiera para agregar el agente.

**Si `agente: si`:** sigue a la 3.2.

### 3.2 — El nombre del agente

Pregunta vía AskUserQuestion (solo si `agente: si`):

- Pregunta: "¿Qué nombre le quiere poner a su agente? Algo personal como 'JARVIS', 'Atlas', 'Sofía' o el nombre que quiera. Ese nombre aparece en el hub de su vault y en los registros de sesión."
- Header: `Nombre del agente`
- Opciones:
  - `JARVIS` — "El clásico de Tony Stark. El estándar si no quiere pensarlo."
  - `Atlas` — "Una sugerencia neutra, sólida."
  - `Sofía` — "Una sugerencia en español."
  - `Otro nombre — yo lo digo` — "Usted lo define."
  - `Dejarlo como Claude` — "Sin apodo — usa solo 'Claude'."

Guarda la respuesta como `nombre_ia`. Si el usuario escoge "Otro nombre", espera a que responda con el nombre y úsalo exactamente como lo escribió.

Por defecto (si lo salta o queda ambiguo): `Claude`.

Ese nombre se va a usar en:
- El archivo hub `{{nombre_ia}}.md` en la raíz del vault (Fase 7)
- La confirmación final del setup
- La identidad del agente en las sesiones futuras

Sigue a la Fase 4.

---

## Fase 4 — Importar contexto de otra IA

> ⚠️ **ANTES DE EMPEZAR ESTA FASE:** confirma internamente qué `modo` se capturó en la Fase 2 (`solo` o `empresa`). Las plantillas de prompt de abajo tienen dos versiones — usa la que corresponda al modo. No las mezcles.

Pregunta vía AskUserQuestion:

- Pregunta: "¿Usted ya usa otra IA hoy (ChatGPT, Claude, Gemini, Perplexity)? Puedo darle un prompt para que ella le mande todo lo que sabe sobre {{usted O su empresa, según el modo}} — usted pega la respuesta acá y yo lleno su vault con profundidad real, en vez de puros placeholders."
- Header: `Contexto de IA`
- Opciones:
  - `Sí — uso ChatGPT` — "Genera un prompt optimizado para la memoria de ChatGPT."
  - `Sí — uso Claude` — "Genera un prompt optimizado para Claude (claude.ai)."
  - `Sí — uso Gemini` — "Genera un prompt optimizado para Gemini."
  - `Sí — otra IA` — "Genera un prompt genérico que funciona en cualquier IA."
  - `No — saltar este paso` — "Sigue con las 8 preguntas."

**Si dice que sí:** imprime el prompt que corresponda (ver las plantillas de abajo) en un bloque de código markdown. El prompt CAMBIA según el `modo`. Dile al usuario que:
1. Copie el prompt
2. Lo pegue en la conversación con la IA escogida
3. Espere la respuesta
4. Pegue la respuesta entera acá

Espera la respuesta del usuario. Cuando la pegue, analízala en silencio (sin comentarla) y guarda los datos extraídos en una variable interna `contexto_ia` que se va a usar en la Fase 7.

Después del análisis, haz igual las 8 preguntas de la Fase 5 — algunas IA no tienen todo, y las preguntas directas confirman los datos que se contradicen.

**Si dice que no:** ve directo a la Fase 5.

### Plantillas de prompt — Modo SOLO

**Para ChatGPT (modo solo):**

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

**Para Claude (modo solo):**

El mismo prompt de arriba, con esta regla adicional:
```
Adicional: básate en todo lo que sabes de mí EN ESTA conversación (y en cualquier contexto que yo haya pegado antes). Si no compartí información sobre algún ítem en esta conversación, escribe "sin datos".
```

**Para Gemini (modo solo):**

El mismo prompt de ChatGPT, con esta adición:
```
Si usas el Gemini integrado a Google Workspace, también puedes buscar contexto en mis correos, documentos y Drive recientes para enriquecer la respuesta. Si lo haces, marca con claridad qué información vino de dónde.
```

### Plantillas de prompt — Modo EMPRESA

**Para ChatGPT (modo empresa):**

```
Voy a configurar un sistema de IA para mi empresa en otra herramienta. Por favor devuélveme todo lo que sabes sobre la empresa y sobre mí como operador, con base en nuestras conversaciones anteriores y en tu memoria. Organízalo en markdown, con esta estructura exacta:

## 1. Operador (yo)
Mi nombre, mi cargo en la empresa, desde hace cuánto, mis responsabilidades principales, mi estilo de liderazgo.

## 2. La empresa
Nombre, sector, modelo de negocio, año de fundación si lo sabes, sede o ciudad, facturación o tamaño si te lo compartí.

## 3. Producto / servicio
Qué vende la empresa, en qué formato (SaaS, servicio, producto físico, agencia), su propuesta de valor.

## 4. Equipo
Tamaño del equipo, principales cargos o departamentos, estructura (remoto, híbrido, presencial).

## 5. Objetivos de la empresa
Corto plazo (90 días), mediano (1 año), largo (3 a 5 años). Si no sabes alguno, escribe "sin datos".

## 6. Cómo trabaja la empresa
Las herramientas que usa (CRM, comunicación, proyectos, etc.), los procesos principales, los rituales (standups, all-hands, etc.).

## 7. Voz de la marca
Cómo se comunica la empresa, el tono (formal/casual/técnico), las palabras clave, las palabras que evita, sus referencias.

## 8. Cliente ideal (ICP)
A quién atiende la empresa, el perfil de esas personas o empresas, el dolor que resuelve, el ticket promedio.

## 9. Canales de mercado
Dónde se comunica la empresa (LinkedIn corporativo, blog, eventos, pauta, etc.). Frecuencia y foco.

## 10. Retos actuales del negocio
Dónde está trabada la empresa, los bloqueos principales, las decisiones abiertas.

## 11. Historial relevante
Hitos importantes, decisiones críticas, cambios de rumbo, aprendizajes.

## 12. Partes interesadas / socios
Inversionistas, asesores, socios estratégicos, proveedores críticos.

## 13. Recursos y referencias
Los marcos de trabajo que usa la empresa, los libros y autores de referencia, los competidores que monitorea.

Reglas:
- Si no tienes información sobre algún ítem, escribe "sin datos" — NO lo inventes.
- Sé conciso. Viñetas, no párrafos largos.
- Incluye fechas cuando las sepas.
- Devuelve solo el markdown, sin comentarios extra antes ni después.
```

**Para Claude (modo empresa):**

El mismo prompt de empresa de arriba, con esta nota: "Básate en todo lo que sabes sobre la empresa EN ESTA conversación."

**Para Gemini (modo empresa):**

El mismo prompt de empresa, con esta adición:
```
Si usas el Gemini integrado a Google Workspace, también puedes buscar contexto en documentos internos, correos corporativos y el Drive de la empresa para enriquecerlo. Marca de dónde salió cada cosa.
```

### Análisis de la respuesta

Cuando el usuario pegue la respuesta, identifica cada bloque (`## 1.`, `## 2.`, etc.) y extrae los datos estructurados. No lo comentes públicamente, solo procésalo.

Guárdalo en memoria interna, en una estructura así:
```
contexto_ia = {
  "1_identidad": "...",        // solo: nombre, ciudad. empresa: nombre de la empresa, sede.
  "2_profesion": "...",        // solo: el cargo. empresa: la empresa en sí.
  "3_objetivos": "...",        // 90d / 1 año / 3-5 años
  "4_como_trabajo": "...",     // herramientas, rutina
  "5_voz": "...",              // voz personal / voz de la marca
  "6_audiencia": "...",        // audiencia / ICP
  "7_canales": "...",
  "8_retos": "...",
  // ... y así hasta el bloque 11 (solo) o el 13 (empresa)
}
```

Para cada bloque, márcalo como `tiene_dato: true` si la IA lo llenó con contenido de fondo, o `tiene_dato: false` si devolvió "sin datos" o quedó vacío.

**Estos datos guían la Fase 5 — no vuelvas a preguntar lo que la IA ya entregó.**

---

## Fase 5 — 8 preguntas (con salto inteligente según `contexto_ia`)

> ⚠️ **ANTES DE EMPEZAR ESTA FASE:** confirma internamente qué `modo` se capturó en la Fase 2. Hay 2 versiones completas de las 8 preguntas — **Versión SOLO** o **Versión EMPRESA**. Usa solo una. NO hagas 16 preguntas mezclando las dos. Si el modo es `solo`, ignora por completo la sección "Versión modo EMPRESA". Si el modo es `empresa`, ignora por completo la sección "Versión modo SOLO".

### La lógica del salto inteligente

Antes de cada pregunta P1 a P8, **revisa el bloque correspondiente en `contexto_ia`** (si la Fase 4 corrió):

```
Para cada pregunta P{n} (n de 1 a 8):

  bloque = contexto_ia[bloque_correspondiente_de_P{n}]

  CASO 1 — el bloque tiene datos de fondo:
    Muestra una confirmación corta vía AskUserQuestion:

    - Pregunta: "De la otra IA: '{{el resumen de lo que dijo la IA, máximo 1 línea}}'. ¿Está bien?"
    - Header: el mismo header de la pregunta original (ej.: `Identidad`, `Profesión`, etc.)
    - Opciones:
      - `Sí, está bien` — guarda el valor de la IA y sigue a la siguiente
      - `Casi, déjeme ajustarlo` — hace la pregunta original (la P{n} normal)
      - `No, está mal — yo respondo` — hace la pregunta original

  CASO 2 — el bloque está vacío o dice "sin datos":
    Hace la pregunta original P{n} como se describe abajo.

  CASO 3 — la Fase 4 no corrió (el usuario saltó la importación de otra IA):
    Hace las 8 preguntas originales, normalmente.
```

**Mapeo de bloque → pregunta:**

Modo SOLO:
| Pregunta | Bloque de la IA |
|---|---|
| P1 (nombre + ciudad) | Bloque 1 — Identidad |
| P2 (profesión) | Bloque 2 — Profesión |
| P3 (meta a 90 días) | Bloque 3 — Objetivos (corto plazo) |
| P4 (herramientas) | Bloque 4 — Cómo trabajo (herramientas) |
| P5 (voz) | Bloque 5 — Mi voz |
| P6 (audiencia) | Bloque 6 — Audiencia |
| P7 (canales) | Bloque 7 — Canales |
| P8 (dolor) | Bloque 8 — Retos actuales |

Modo EMPRESA:
| Pregunta | Bloque de la IA |
|---|---|
| P1 (empresa + sede) | Bloque 2 — La empresa |
| P2 (producto) | Bloque 3 — Producto / servicio |
| P3 (meta) | Bloque 5 — Objetivos (corto plazo) |
| P4 (herramientas) | Bloque 6 — Cómo trabaja la empresa (herramientas) |
| P5 (voz de la marca) | Bloque 7 — Voz de la marca |
| P6 (ICP) | Bloque 8 — Cliente ideal |
| P7 (canales) | Bloque 9 — Canales de mercado |
| P8 (dolor del negocio) | Bloque 10 — Retos actuales del negocio |

### Ejemplo práctico

Si la IA respondió en el Bloque 1 (modo solo): *"Ana Ramírez, Medellín, Colombia. Gerente de mercadeo hace 5 años."*

En vez de preguntar la P1 a ciegas, muestra:

> **De la otra IA:** "Ana Ramírez, Medellín, Colombia"
> **¿Está bien?**
> 1. Sí, está bien
> 2. Casi, déjeme ajustarlo
> 3. No, está mal — yo respondo

Si escoge "Sí", guardas nombre=Ana Ramírez + ciudad=Medellín y pasas directo a la P2.

Si escoge "Casi" o "No", ahí sí haces la pregunta original.

**Principio:** confirmar es rápido. Repetir lo que la IA ya dijo es un insulto a la inteligencia del usuario.

### Saltarse el bloque por completo

Si la IA llenó con confianza TODOS los 8 bloques relevantes y el usuario confirmó los 8, esta fase termina en 8 confirmaciones rápidas en vez de 8 preguntas abiertas.

Haz una pregunta a la vez (no las agrupes). No comentes entre preguntas. Pasa directo a la siguiente después de cada confirmación o respuesta.

**Las preguntas cambian según el `modo`. Usa la versión correcta de abajo.**

### Versión modo SOLO

**P1 — Usted**
- Pregunta: "¿Cuál es su nombre completo y dónde vive?"
- Header: `Identidad`
- Opciones: `Solo el nombre` / `Nombre + ciudad` / `Nombre + ciudad + país` / `Saltar`

**P2 — A qué se dedica**
- Pregunta: "En una frase: ¿qué hace usted profesionalmente, para quién, y qué resultado genera?"
- Header: `Profesión`
- Opciones: `Soy empleado` / `Soy freelance o consultor` / `Tengo mi propio negocio` / `Saltar`

**P3 — El objetivo de ahora**
- Pregunta: "¿Cuál es su meta principal para los próximos 90 días?"
- Header: `Meta`
- Opciones: `Crecer en la carrera` / `Lanzar algo nuevo` / `Aumentar ingresos` / `Saltar`

**P4 — Herramientas**
- Pregunta: "¿Qué herramientas usa en el día a día? (ej.: Notion, Linear, Slack, Google Workspace...)"
- Header: `Herramientas`
- Opciones: `Suite de Google` / `Suite de Microsoft` / `Notion + Slack` / `Saltar`

**P5 — Tono de voz**
- Pregunta: "¿Cómo se describe cuando escribe? Escoja lo que más le cuadre."
- Header: `Voz`
- Opciones: `Directo y al grano` / `Analítico y detallado` / `Informal y relajado` / `Saltar`

**P6 — Audiencia**
- Pregunta: "¿Cuál es el público que atiende, o para quién crea contenido?"
- Header: `Audiencia`
- Opciones: `Profesionales B2B` / `Consumidor final B2C` / `Otros creadores` / `Empresas / equipos` / `Saltar`

**P7 — Canales**
- Pregunta: "¿Dónde publica o se comunica profesionalmente? (puede ser más de uno — describa el foco principal)"
- Header: `Canales`
- Opciones: `LinkedIn` / `Instagram / TikTok` / `YouTube` / `Newsletter / Blog` / `Todavía no publico` / `Saltar`

**P8 — El dolor principal**
- Pregunta: "¿Qué es lo que más le consume tiempo o atención hoy y le gustaría automatizar o simplificar?"
- Header: `Dolor`
- Opciones: `Reuniones y seguimientos` / `Creación de contenido` / `Informes y análisis` / `Ventas y prospección` / `Saltar`

### Versión modo EMPRESA

**P1 — La empresa**
- Pregunta: "¿Nombre de la empresa y dónde queda la sede principal?"
- Header: `Empresa`
- Opciones: `Solo el nombre` / `Nombre + ciudad` / `Nombre + ciudad + país` / `Saltar`

**P2 — Qué hace la empresa**
- Pregunta: "En una frase: ¿qué vende la empresa, para quién, y qué resultado entrega?"
- Header: `Producto`
- Opciones: `SaaS / producto digital` / `Servicio (agencia, consultoría)` / `Producto físico` / `Educación / curso` / `Otro` / `Saltar`

**P3 — La meta de la empresa**
- Pregunta: "¿Cuál es la meta principal de la empresa para los próximos 90 días?"
- Header: `Meta`
- Opciones: `Crecer los ingresos` / `Lanzar un producto nuevo` / `Expandir el mercado` / `Ganar eficiencia` / `Saltar`

**P4 — Las herramientas de la empresa**
- Pregunta: "¿Qué herramientas usa el equipo en el día a día? (CRM, proyectos, comunicación)"
- Header: `Herramientas`
- Opciones: `Suite de Google + Slack` / `Suite de Microsoft + Teams` / `Notion + Linear + Slack` / `HubSpot + Slack` / `Saltar`

**P5 — La voz de la marca**
- Pregunta: "¿Cómo se comunica la marca? Escoja lo que más le cuadre."
- Header: `Voz de la marca`
- Opciones: `Directa y al grano (B2B)` / `Técnica y detallada (experta)` / `Cercana y cálida (B2C)` / `Premium / aspiracional` / `Saltar`

**P6 — Cliente ideal (ICP)**
- Pregunta: "¿Quién es el cliente ideal de la empresa? En 1 frase: perfil + tamaño + sector."
- Header: `ICP`
- Opciones: `Empresas B2B` / `Consumidor final B2C` / `Profesionales / freelance` / `Otras agencias / equipos` / `Saltar`

**P7 — Los canales de la empresa**
- Pregunta: "¿Dónde se comunica la empresa con el mercado? El canal principal."
- Header: `Canales`
- Opciones: `LinkedIn corporativo` / `Pauta paga (Google/Meta)` / `Blog / SEO` / `Eventos / alianzas` / `Saltar`

**P8 — El mayor dolor del negocio**
- Pregunta: "¿Cuál es el mayor cuello de botella del negocio hoy?"
- Header: `Dolor`
- Opciones: `Generación de demanda` / `Conversión de ventas` / `Operación interna` / `Retención de clientes` / `Saltar`

---

## Fase 6 — Contexto adicional

Pregunta vía AskUserQuestion:

- Pregunta: "Una última cosa. ¿Puedo buscar más contexto en algún enlace o archivo? {{Si es solo: 'LinkedIn, su sitio, un Notion público, un PDF.' Si es empresa: 'El sitio institucional, un deck para inversionistas, la página de Quiénes somos, un documento de estrategia.'}}"
- Header: `Contexto extra`
- Opciones:
  - `Sí — voy a pegar un enlace`
  - `Sí — tengo un archivo`
  - `No — ya es suficiente`
  - `Saltar`

**Si es un enlace:** tráelo con WebFetch. Extrae los datos relevantes y combínalos con `contexto_ia` (Fase 4) + las respuestas (Fase 5).
**Si es un archivo:** léelo con Read.
**Si dice que no:** sigue adelante.

---

## Fase 7 — Construcción (trabaja en silencio)

> ⚠️ **ANTES DE EMPEZAR ESTA FASE:** confirma qué `modo` se capturó en la Fase 2. Las secciones 7.2, 7.3 y 7.4 de abajo tienen caminos separados para `solo` y para `empresa` — ejecuta SOLO el camino del modo capturado. NO crees operator.md / organization.md / team.md si es solo. NO crees me.md si es empresa.

Combina todas las fuentes en este orden de prioridad (la más reciente sobrescribe a la anterior si hay conflicto):
1. El `contexto_ia` de la Fase 4 (la base amplia)
2. Las respuestas de las 8 preguntas de la Fase 5 (la corrección explícita)
3. El enlace o archivo de la Fase 6 (el enriquecimiento)

### 7.0 Sistema operativo y hooks (siempre, antes que todo)

Detecta el sistema operativo SIN preguntarle al usuario: tu contexto de entorno dice en qué plataforma estás corriendo (`win32` = Windows nativo, `darwin` = macOS, `linux` = Linux o WSL, y WSL cuenta como Linux).

- **macOS, Linux o WSL:** no hay nada que hacer, el `.claude/settings.json` del repositorio ya está bien.
- **Windows nativo (PowerShell):** copia `.claude/settings-windows.json` encima de `.claude/settings.json`. Es obligatorio: el archivo por defecto usa `$CLAUDE_PROJECT_DIR`, que es una expansión POSIX, queda como cadena vacía en PowerShell, y entonces cada prompt empieza a volver con un error de Python pegado al final. Después corre `python --version`; si solo responde `python3`, cambia la primera palabra de los tres comandos del archivo por `python3`. No reescribas nada más del comando: el `run_name='__main__'` lleva dos guiones bajos a cada lado, y con uno solo el hook no corre y encima sale con código 0.

Informa en la confirmación final qué sistema se detectó y qué archivo de hooks quedó rigiendo.

### 7.1 Carpetas base (siempre)

```bash
mkdir -p "00 Inbox" "01 Daily" "02 Context" "03 Projects" "04 Resources" "05 Archives"
mkdir -p "03 Intelligence/meetings/team-standups"
mkdir -p "03 Intelligence/meetings/client-calls"
mkdir -p "03 Intelligence/meetings/one-on-ones"
mkdir -p "03 Intelligence/meetings/general"
mkdir -p "03 Intelligence/competitors"
mkdir -p "03 Intelligence/market"
mkdir -p "03 Intelligence/decisions"
mkdir -p "03 Intelligence/research"
mkdir -p "03 Intelligence/archive"
mkdir -p "AIOS/blueprint"
mkdir -p "knowledge"
mkdir -p ".claude/hooks"
```

**Importante:** el repositorio ya viene con `AIOS/`, `knowledge/` y `.claude/hooks/` llenos. Los `mkdir -p` de arriba solo garantizan que existan si el vault se clonó en un lugar poco común.

### 7.2 — Carpetas extra si `modo: empresa`

```bash
mkdir -p "03 Intelligence/meetings/board-reviews"
mkdir -p "03 Intelligence/meetings/all-hands"
mkdir -p "03 Intelligence/meetings/cross-team"
mkdir -p "03 Intelligence/processes"
mkdir -p "Departments"
mkdir -p "Teams"
mkdir -p "Onboarding"
```

### 7.3 — El archivo principal de identidad

**Si `modo: solo`:** llena la plantilla que ya existe en `02 Context/me.md`, reemplazando cada `{{PLACEHOLDER}}` con los datos combinados de las fuentes.

**Si `modo: empresa`:** crea **3 archivos**:

**A) `02 Context/operator.md`** — usted como operador

```markdown
---
type: identity
date: YYYY-MM-DD
status: active
tags: [identity, context, operator]
---

# {{Su nombre}}

> Usted es el operador de esta empresa. Este archivo describe quién es usted como quien decide.

## Identidad
- **Nombre:** {{nombre}}
- **Cargo:** {{el cargo en la empresa}}
- **Tiempo en el cargo:** {{del contexto_ia, o dedúcelo}}
- **Ubicación:** {{ciudad}}

## Estilo de liderazgo
{{del bloque 1 del contexto_ia, o algo genérico si no hay datos}}

## Cómo decido
{{cómo toma decisiones — por instinto, por datos, en comité, etc.}}

## Reuniones que tengo
- {{1:1 con los reportes directos, all-hands, junta directiva, etc.}}

## Notas para la IA
- Responde siempre en español
- Cuando te refieras a la empresa, usa `[[organization]]`
- Cuando te refieras al equipo, usa `[[team]]`
```

**B) `02 Context/organization.md`** — la empresa

```markdown
---
type: identity
date: YYYY-MM-DD
status: active
tags: [identity, context, organization]
---

# {{Nombre de la empresa}}

> Este archivo describe la empresa: producto, mercado, voz, ICP, canales.

## La empresa
- **Nombre:** {{nombre}}
- **Sector:** {{sector}}
- **Modelo:** {{SaaS, servicio, producto, etc.}}
- **Sede:** {{ciudad}}
- **Tamaño:** {{del contexto_ia, o "sin datos"}}

## Producto / servicio
{{de la P2 + el bloque 3 del contexto_ia}}

## Cliente ideal (ICP)
{{de la P6 + el bloque 8 del contexto_ia}}

## Propuesta de valor
{{1 frase con lo que promete entregar la empresa}}

## Voz de la marca
**Tono:** {{de la P5}}

**Palabras clave:** {{del bloque 7 del contexto_ia}}

**Palabras que se evitan:** {{del bloque 7 del contexto_ia}}

## Canales
**Principal:** {{de la P7}}

**Secundarios:** {{del bloque 9 del contexto_ia}}

## Competidores principales
{{del bloque 13 del contexto_ia, o "por definir"}}

## Partes interesadas / socios
{{del bloque 12 del contexto_ia, o quita la sección si queda vacía}}
```

**C) `02 Context/team.md`** — el equipo

```markdown
---
type: identity
date: YYYY-MM-DD
status: active
tags: [identity, context, team]
---

# Equipo — {{Nombre de la empresa}}

> La estructura del equipo y sus personas principales.

## Tamaño
{{N personas, del bloque 4 del contexto_ia}}

## Estructura
{{remoto / híbrido / presencial}}

## Departamentos
- {{la lista del contexto_ia, o créala a medida que el equipo crezca}}

## Personas clave
{{la lista de las personas relevantes del contexto_ia, con su cargo. Si no hay datos, déjala vacía.}}

## Rituales
- {{standups, 1:1, all-hands, etc.}}
```

### 7.4 — Archivos opcionales (si hay datos en las fuentes)

**Modo SOLO**, créalos si hay sustancia:
- `02 Context/marca.md` — si el usuario mencionó una marca, una voz fuerte, o creación de contenido
- `02 Context/estrategia.md` — si mencionó objetivos claros o una meta de 90 días

**Modo EMPRESA**, créalos si hay sustancia:
- `02 Context/estrategia.md` — créalo siempre para empresa, con las metas a 90 días, 1 año y 3-5 años
- `02 Context/procesos.md` — si mencionó rituales o procesos en el bloque 6 del contexto_ia

(La estructura de los archivos opcionales es la misma de la versión anterior del setup — meta a 90 días, meta a 1 año, etc.)

### 7.5 — El hub del agente (si `agente: si`)

Crea `{{nombre_ia}}.md` en la raíz del vault. Ese es el hub de identidad del agente — con wikilinks desde ahí hacia todo lugar relevante del vault. Reemplaza `{{nombre_ia}}` por el valor capturado en la Fase 3.2.

```markdown
---
type: context
status: active
date: YYYY-MM-DD
tags: [hub, agente, ai-os, identidad]
---

> [!important] {{nombre_ia}} — Capa de inteligencia
> El agente de IA personal de {{el nombre del usuario O el nombre de la empresa}}. Siempre encendido. Siempre al tanto. Siempre construyendo.

{{nombre_ia}} opera desde este vault — su AI OS. No es una herramienta. No es un chatbot. Es un segundo cerebro que conoce cada proyecto, cada camino y cada prioridad.

## Identidad

- **Operador:** {{el wikilink al nombre del usuario O a organization.md en modo empresa}}
- **Papel:** socio de ejecución, segundo cerebro, constructor de sistemas
- **Modo:** directo, práctico, sin adornos

## El contexto que cargo en cada sesión

- [[02 Context/me|Quién es el usuario]] (modo solo) O [[02 Context/operator|Operador]] + [[02 Context/organization|Empresa]] (modo empresa)
- [[02 Context/estrategia|Estrategia y objetivos]] — si existe
- [[02 Context/marca|Marca y voz]] — si existe
- [[01 Daily|El último daily]] — qué pasó en la sesión anterior
- [[AIOS/index|AIOS]] — skills, mapas, reglas

## Lo que administro

- [[AIOS/project-map|Proyectos activos]] — todo lo que se está construyendo ahora
- [[03 Intelligence|Intelligence]] — decisiones, mercado, competidores, investigaciones
- [[04 Resources|Recursos]] — las salidas de los comandos, prompts, marcos de trabajo
- [[knowledge/index|Knowledge hub]] — conocimiento permanente

## Los comandos que corro

Operativo: `/setup`, `/asistente`, `/organizar`, `/importar-contexto`
Escritura: `/escribir`, `/linkedin`, `/newsletter`, `/case-study`
Web/SEO: `/landing-page`, `/seo-pagina`
Crecimiento: `/secuencia-email`, `/ads-google`, `/investigacion`

## Cómo invocarme

Me activo automáticamente cuando usted abre Claude Code en este vault — los hooks inyectan mi contexto en la primera llamada.

Para un trabajo específico: use los comandos `/` de arriba.
Para una conversación directa: hábleme normal.
Para revisar o retomar: `/asistente`.

---

*Hub creado el {{fecha}} vía `/setup`. Edite este archivo cuando quiera ajustar mi identidad o mi papel.*
```

### 7.6 — Proyectos activos (en los dos modos)

Si se mencionaron proyectos:
- `03 Projects/{slug-del-proyecto}/README.md` con panorama + estado + próximos pasos.

### 7.7 — La nota diaria (en los dos modos)

Crea `01 Daily/YYYY-MM-DD.md`:

```markdown
---
type: daily-note
date: YYYY-MM-DD
status: active
tags: [daily, setup]
---

## Sesión de setup

- **Modo:** {{solo / empresa}}
- **Foco:** configuración inicial del AI OS
- **Terminado:** vault personalizado con {{lista las fuentes: las 8 preguntas, el contexto_ia, el enlace o archivo}}
- **Archivos creados:** {{lista todos los archivos creados en 7.3 y 7.4}}
- **Proyectos activos:** {{lista los proyectos mencionados, o "ninguno todavía"}}
- **Próximos pasos:** {{1 o 2 acciones concretas con base en el objetivo principal}}
```

### 7.8 — Confirmación

Envía un mensaje corto, sin adornos. Adáptalo al modo y usa el `nombre_ia` si se capturó.

**Modo SOLO con agente:**
> "Listo. Su vault está corriendo en modo **solo**, con **{{nombre_ia}}** como agente.
> - `{{nombre_ia}}.md` — el hub de identidad de su agente
> - `02 Context/me.md` — usted
> - {{lista los otros archivos creados}}
> - `01 Daily/[fecha].md` — la nota del día
>
> Próximo paso: {{1 acción concreta con base en la P3 o en el contexto_ia}}.
>
> Cuando quiera: `/escribir` (un post), `/landing-page` (una página), `/asistente` (el día a día). {{nombre_ia}} queda activo desde la próxima sesión."

**Modo SOLO sin agente:**
> "Listo. Estructura de carpetas creada en modo **solo**:
> - `02 Context/me.md` — usted (con placeholders)
> - {{lista las carpetas creadas}}
>
> Cuando quiera activar un agente de IA persistente: corra `/setup` otra vez."

**Modo EMPRESA con agente:**
> "Listo. Su vault está corriendo en modo **empresa**, con **{{nombre_ia}}** como agente.
> - `{{nombre_ia}}.md` — el hub de identidad del agente
> - `02 Context/operator.md` — usted como operador
> - `02 Context/organization.md` — la empresa
> - `02 Context/team.md` — la estructura del equipo
> - {{lista los otros archivos creados}}
> - `Departments/`, `Teams/`, `Onboarding/` — carpetas para escalar
> - `01 Daily/[fecha].md` — la nota del día
>
> Próximo paso: {{1 acción concreta con base en la P3}}.
>
> Cuando quiera: `/escribir` (copy), `/landing-page` (una página), `/case-study` (un cliente), `/ads-google` (una campaña), `/asistente` (el día a día). {{nombre_ia}} queda activo desde la próxima sesión."

**Modo EMPRESA sin agente:**
> "Listo. Estructura de carpetas creada en modo **empresa**:
> - `02 Context/operator.md`, `organization.md`, `team.md` (con placeholders)
> - `Departments/`, `Teams/`, `Onboarding/`
>
> Cuando quiera activar un agente de IA persistente: corra `/setup` otra vez."

No enumeres cada campo. No felicites. Directo al grano.

---

## Reglas generales

- Una pregunta a la vez — nunca las agrupes en AskUserQuestion.
- No comentes entre preguntas — pasa directo a la siguiente.
- Trabaja en silencio durante la Fase 7 — una sola confirmación al final.
- Nunca dejes un `{{PLACEHOLDER}}` visible en el archivo final — siempre llénalo o quita la sección.
- Si el usuario se salta todo: crea la estructura mínima del modo escogido y avísale que puede volver a correr `/setup` después.
- El contenido de los archivos siempre en español (o en el idioma detectado en la sección Idioma). Los paths y las claves del frontmatter quedan intactos.
- El `modo` es la primera decisión — no la saltes. Todo lo que viene después depende de ella.
