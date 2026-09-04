---
type: map
status: active
date: 2026-05-26
tags: [aios, projects, map]
---

# Project Map

Lista de todos los proyectos activos. Actualízala a medida que entra o sale un proyecto.

La IA consulta este archivo cuando mencionas un proyecto por su nombre — para saber cuál es, dónde está el README y cuál es el estado actual.

---

## Estructura

Cada proyecto tiene una entrada con 4 campos:

| Campo | Qué es |
|---|---|
| **Nombre** | Cómo te refieres al proyecto en la conversación |
| **README** | Wikilink a `03 Projects/{nombre}/README.md` |
| **Estado** | `active`, `paused`, `completed`, `archived` |
| **Próximo paso** | 1 frase con la acción inmediata pendiente |

---

## Proyectos activos

> Cuando corras `/setup`, esta sección se llena con los proyectos que hayas mencionado. Puedes editarla a mano cuando quieras.

<!--

Ejemplo de formato — llenar a medida que aparezcan:

### Lanzamiento Newsletter

- **README:** [[03 Projects/Lanzamiento Newsletter/README]]
- **Estado:** active
- **Próximo paso:** Subir la landing page de captación

### Cliente Acme — Consultoría

- **README:** [[03 Projects/Cliente Acme/README]]
- **Estado:** active
- **Próximo paso:** Presentar el diagnóstico el lunes

-->

---

## Proyectos pausados

> Proyectos que existen pero en los que no se está trabajando ahora. Se mantienen acá como referencia.

<!-- El mismo formato de los activos. -->

---

## Proyectos terminados

> Terminados hace poco. Cuando pasen 30 días, moverlos a `05 Archives/projects/`.

<!-- El mismo formato. Agregar el campo "Terminado el: YYYY-MM-DD". -->

---

## Cómo se usa

**Agregar un proyecto:** cuando mencionas algo que va a durar más de 1 semana, la IA crea `03 Projects/{nombre}/README.md` y lo agrega acá.

**Actualizar el estado:** cuando dices que cambió de fase ("pausado", "terminado"), la IA lo mueve entre las secciones de este archivo.

**Consultar:** cuando dices "¿cómo va el proyecto X?", la IA lee este archivo + el README del proyecto para darte el estado actual.

**Archivar:** los proyectos terminados se quedan acá 30 días y después se mueven a `05 Archives/projects/`.

---

## Principios

- Un proyecto = una carpeta en `03 Projects/{nombre}/`
- El README es la puerta de entrada — panorama + estado + próximos pasos
- Las subcarpetas (research, specs, drafts, ideas, notes, feedback) aparecen a medida que emergen los tipos de contenido
- Cuando algo dura menos de 1 semana, no es un proyecto: va en el daily o en el inbox

---

## Conectado a

[[Home]] · [[index]] · [[Vault-Map]] · [[knowledge-routing]] · [[operating-rules]]
