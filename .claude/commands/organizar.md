---
description: Organiza el vault. Encuentra notas huérfanas, las enruta a la estructura correcta, las conecta con wikilinks y archiva lo redundante, sin tocar las carpetas del sistema. Pregunta cuando tiene dudas.
---

# Organizar: limpieza y enrutamiento del vault

Úsalo cuando el grafo se vuelva una sopa: notas sueltas, sin enlaces, tiradas en la raíz o en el Inbox. Este comando enruta todo hacia la estructura que `/setup` ya creó, conecta con wikilinks y archiva lo redundante. Nunca reestructura el vault y nunca borra nada.

---

## Idioma / Language

Detecta el idioma del mensaje que invocó este comando y úsalo en todas las preguntas y mensajes.
Español por defecto. Inglés o portugués si el usuario escribió en ese idioma.
El contenido de los archivos, los paths y las claves del frontmatter quedan intactos. No los traduzcas.

---

## Antes de cualquier cosa

Lee al comienzo, sin anunciarlo:
1. `02 Context/me.md` (quién es el usuario, su voz, sus proyectos) en modo solo, O `02 Context/operator.md` + `organization.md` en modo empresa
2. El archivo más reciente de `01 Daily/`, para tomar el contexto de la última sesión

---

## Reglas duras (NO rompas ninguna)

- **NO renombres, muevas ni borres** las carpetas del sistema: `00 Inbox`, `01 Daily`, `02 Context`, `03 Projects`, `03 Intelligence`, `04 Resources`, `05 Archives`, `AIOS/`, `knowledge/`, `.claude/`. Los hooks usan esas rutas exactas, y tocarlas rompe el agente.
- **NO toques** `README.md`, `CLAUDE.md`, ni ningún archivo `index`. Aparecen sueltos en el grafo pero son estructurales y así están bien. Nunca entran en la lista de huérfanas.
- **NUNCA borres nada.** Lo redundante se va a `05 Archives/`, nunca a la basura.
- **Cierra Obsidian antes de mover archivos** (evita las copias de conflicto tipo "Nota 2.md"). Avísale al usuario antes de ejecutar la Fase 4.
- Usa **wikilinks `[[ ]]`** de Obsidian, nunca enlaces de markdown para notas internas.
- Trabaja en silencio durante la ejecución. La confirmación va solo al final.

---

## Fase 1: mapear (no cambies nada)

1. Lista el árbol de carpetas actual del vault (hasta 2 niveles).
2. Identifica las **notas huérfanas**: archivos `.md` que el usuario creó o pegó y quedaron sueltos. Una nota es huérfana si:
   - no tiene ningún wikilink `[[ ]]` de salida Y ninguna otra nota la enlaza, O
   - está en la raíz del vault o en `00 Inbox/` sin un destino claro.

   **Excluye siempre** `README.md`, `CLAUDE.md`, cualquier `index`, y las notas que ya viven correctamente dentro de una subcarpeta de proyecto o de contexto y ya están enlazadas.
3. Para cada nota huérfana, di en 1 línea qué parece ser.
4. Muéstrale esa lista al usuario. Todavía no cambies nada.

---

## Fase 2: clasificar y preguntar

Clasifica cada nota huérfana con este enrutamiento:

| Tipo de contenido | Destino |
|---|---|
| Identidad, avatar, voz, posicionamiento, promesa, oferta | `02 Context/` |
| Proyecto real (curso, producto, marketplace, cliente) | `03 Projects/{nombre}/` |
| Marco de trabajo, método, swipe, plantilla, prompt reutilizable | `04 Resources/` |
| Investigación de mercado o de competidores, decisión estratégica | `03 Intelligence/` |
| Borrador sin dueño claro | `00 Inbox/` |

**Donde el destino sea obvio, decídelo solo.** Donde NO lo sea, pregunta vía AskUserQuestion, **una pregunta a la vez**, con las carpetas como opciones. Pregunta también cuando:

- **Duplicados:** dos notas parecen lo mismo.
  - Pregunta: "`{{nota A}}` y `{{nota B}}` parecen el mismo contenido. ¿Qué hago?"
  - Header: `Duplicado`
  - Opciones: `Unirlas en una sola` / `Dejar A, archivar B` / `Dejar B, archivar A` / `Dejar las dos`

- **Versiones "CONSOLIDADO":** varios archivos parecen versiones del mismo documento.
  - Pregunta: "Encontré {{N}} versiones de '{{tema}}'. ¿Cuál es la buena? Las otras se van a 05 Archives."
  - Header: `Versión buena`
  - Opciones: lista los archivos como opciones, más `Dejarlas todas`

- **Borrador abandonado:** una nota vieja, vacía o claramente descartada.
  - Pregunta: "`{{nota}}` parece un borrador abandonado. ¿La archivo en 05 Archives?"
  - Header: `¿Archivar?`
  - Opciones: `Sí, archivar` / `No, es importante, dejarla` / `Decide tú dónde va`

- **Destino ambiguo:** no hay forma de saber la carpeta.
  - Pregunta: "¿A dónde va '`{{nota}}`'? Resumen: {{1 línea}}."
  - Header: `Destino`
  - Opciones: `02 Context` / `03 Projects` / `04 Resources` / `03 Intelligence` / `00 Inbox`

Junta todas las dudas y resuélvelas antes de armar el plan. No comentes entre preguntas, pasa directo a la siguiente.

---

## Fase 3: el plan (espera el "dale")

Arma el plan final y PARA:

```
PLAN DE ORGANIZACIÓN

Mover ({{N}}):
- {{nota}} -> {{carpeta destino}}
- ...

Archivar en 05 Archives ({{N}}):
- {{nota}}: motivo
- ...

Wikilinks por crear:
- {{nota}} se conecta con {{nota o hub}}
- ...
```

Pregunta: "¿Puedo ejecutar? (acuérdate de cerrar Obsidian antes)". Solo sigue a la Fase 4 con una aprobación explícita.

---

## Fase 4: ejecutar (solo después de la aprobación)

Trabaja en silencio:

1. **Mover** cada nota a su carpeta de destino. Crea las subcarpetas de proyecto (`03 Projects/{nombre}/`) cuando haga falta.
2. **Frontmatter:** garantiza `type`, `date`, `status`, `tags` en toda nota movida. Llena lo que falte con base en el contenido.
3. **Wikilinks:** conecta cada nota al contexto al que pertenece. Las notas del mismo tema se enlazan entre sí (ejemplo: avatar, promesa y método se referencian y apuntan al hub de `02 Context`). Toda nota debe terminar con al menos 1 enlace de entrada o de salida.
4. **Archivar:** mueve lo redundante a `05 Archives/` (nunca lo borres). Si archivas varias notas de un mismo tema, crea un `05 Archives/{tema}/README.md` corto que diga qué es y por qué.
5. **Index:** actualiza `knowledge/index` con las notas enrutadas, si el archivo existe.

---

## Fase 5: resumen

Un mensaje corto, sin adornos:

> "Organizado.
> - Movidas: {{N}} notas hacia {{carpetas}}
> - Enlazadas: {{N}}
> - Archivadas: {{N}} en 05 Archives
> - Todavía abiertas: {{0 o la lista de lo que no supiste decidir}}
>
> Ya puedes volver a abrir Obsidian. El grafo debería estar conectado ahora."

---

## Reglas

- Guarda siempre en automático. Nunca pidas permiso para guardar, solo para mover en masa (Fase 3).
- Nunca inventes un destino. Si no sabes, pregunta (Fase 2) o déjalo en `00 Inbox`.
- Nunca borres. Todo lo que sale se va a `05 Archives`.
- Nunca toques las carpetas del sistema, ni README, ni CLAUDE, ni los index.
- Si el usuario corrige un enrutamiento, guarda la regla en `02 Context/me.md` para no repetir el error.
