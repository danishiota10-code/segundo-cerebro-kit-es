---
type: guide
status: active
date: 2026-05-26
tags: [guide, archives]
---

# Archives — Guía de esta carpeta

Contenido terminado, histórico. Cosas que no van a desaparecer, pero que ya no están activas.

---

## Cuándo mover algo para acá

- **Proyecto terminado** → `03 Projects/{nombre}/` pasa a `05 Archives/projects/{nombre}/`
- **Newsletter publicada hace más de 30 días** → de `04 Resources/textos/newsletter/` a `05 Archives/newsletter/`
- **Cliente que se fue** → sus notas diarias específicas, briefs y casos van a `05 Archives/clients/{nombre}/`
- **Documentación obsoleta pero histórica** → `05 Archives/docs/`
- **Versiones anteriores de me.md, brand.md, strategy.md** → cuando actualices, guarda la versión vieja acá antes de sobrescribir
- **Decisiones revocadas** → de `03 Intelligence/decisions/` a `05 Archives/decisions/`

---

## Estructura sugerida

```
05 Archives/
├── projects/        — Proyectos terminados (hace más de 30 días)
├── newsletter/      — Ediciones ya publicadas y viejas
├── clients/         — Clientes que se fueron
├── decisions/       — Decisiones revocadas
├── docs/            — Documentación obsoleta
└── context/         — Versiones viejas de me.md, brand.md, etc.
```

Crea las subcarpetas a medida que aparezca el contenido. No las crees vacías por adelantado.

---

## Cómo NO usarla

- **No es la basura.** Lo que va acá se mantiene como referencia futura, no para olvidarlo.
- **No es un cajón para sacarse cosas de encima.** Si no lo vas a usar más y no necesitas recordarlo, bórralo. El archivo es para el histórico que sí importa.
- **No es un cajón de sastre.** Si es contenido activo, se queda en su lugar (`Projects/`, `Intelligence/`, `Resources/`).

---

## Política de archivado automático

Regla sugerida:

- Proyecto terminado + 30 días sin actividad → se mueve a `05 Archives/projects/`
- Nota diaria de hace más de 1 año → se queda igual en `01 Daily/` (es registro histórico por naturaleza)
- Newsletter publicada + 6 meses → considerar moverla (si estás produciendo mucho, la carpeta principal crece)
- Decisión revisada → la versión vieja va a `archives/decisions/`, la nueva se queda en `Intelligence/decisions/`

Puedes correr `/asistente` en modo "memoria" o pedirle a la IA "archiva lo que lleva más de 30 días quieto" para automatizarlo.

---

Navegación: vuelve al hub en [[Home]]. Las decisiones revocadas llegan acá desde [[03 Intelligence/decisions/README|Decisions]], y los proyectos jubilados salen de [[03 Projects/CLAUDE|Projects]].
