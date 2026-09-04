# Prompt 02, Notas de reunión

**Cuándo usarlo:** apenas termine una reunión, mientras la memoria está fresca.

---

## Prompt

```
Acabo de salir de una reunión. Necesito que me la proceses.

Datos de la reunión:
- Tipo: {{1:1 / equipo / cliente / presentación / otro}}
- Participantes: {{NOMBRES}}
- Duración: {{TIEMPO}}
- Objetivo de la reunión: {{QUÉ SE IBA A DECIDIR O DISCUTIR}}

Qué pasó:
{{DESCRIBA EN TEXTO LIBRE LO QUE SE HABLÓ; puede ser desordenado, después lo proceso}}

Con base en eso:
1. Crea una nota de reunión estructurada en 03 Intelligence/meetings/{{TIPO}}/YYYY-MM-DD-{{slug}}.md (usa la subcarpeta correcta según el tipo: client-calls, one-on-ones, team-standups o general)
2. Extrae los compromisos, con responsable y plazo (si se mencionaron)
3. Resalta las decisiones tomadas
4. Si hay seguimientos que me tocan a mí, agrégalos como tareas
5. Dime si identificas algún riesgo o algún punto que quedó abierto
```

---

## Qué esperar

Una nota limpia con: resumen ejecutivo, decisiones, compromisos por persona y próximos pasos. No se pierde nada y no hay que reformatear nada a mano.

---

Ver el [[prompts/README|Índice de prompts]] o volver al [[Home]].
