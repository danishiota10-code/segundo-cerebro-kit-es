# Projects — Reglas de esta carpeta

Una subcarpeta por proyecto activo. Cada proyecto tiene un `README.md` como puerta de entrada.

## Estructura de un proyecto

```
03 Projects/
└── Nombre del Proyecto/
    ├── README.md          ← estado, próximos pasos, enlaces
    ├── research/          ← investigaciones, referencias, análisis
    ├── drafts/            ← borradores de contenido o documentos
    └── notes/             ← notas de trabajo, scratchpad
```

## Cuándo crear subcarpetas
- Créalas solo si ya hay contenido para poner adentro — no crees carpetas vacías
- `research/` → cuando haya una investigación o un análisis hecho
- `drafts/` → cuando haya un borrador real
- `notes/` → para notas de trabajo sueltas

## README.md estándar
```markdown
---
type: project
status: active
date: YYYY-MM-DD
tags: [project]
---

## Panorama
{{qué es este proyecto y por qué existe}}

## Estado actual
{{dónde va ahora}}

## Próximos pasos
- [ ] {{acción 1}}
- [ ] {{acción 2}}
```

## Reglas
- Cuando el usuario mencione un proyecto: enrútalo a `03 Projects/{nombre}/README.md`
- Proyectos terminados: muévelos a `04 Resources/archivo/` o bórralos
- Usa wikilinks para conectar los proyectos con las notas diarias y con el contexto

---

Navegación: vuelve al hub en [[Home]]. Hay un modelo listo en [[ejemplo-proyecto]] y el historial de trabajo se registra en [[01 Daily/CLAUDE|Daily]].
