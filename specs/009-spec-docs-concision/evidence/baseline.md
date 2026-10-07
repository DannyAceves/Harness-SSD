# SPEC-009 — Baseline editorial (TASK-001, TEST-001)

Medición previa: `find .spec -type f -name '*.md' -print0 | xargs -0 wc -l`
en el estado aprobado para implementación. Total: **8,672 líneas**, 15
archivos; diez superan 500. Cada archivo debe reducirse y quedar en <=300;
total final <=4,500.

| Archivo | Líneas antes | Secciones que deben conservarse |
|---------|-------------:|----------------------------------|
| `constitution.md` | 375 | Artículos I-XII, Definition of Done, Precedencia |
| `standards/architecture.md` | 288 | 1-14, checklist |
| `standards/coding.md` | 427 | 1-22, checklist |
| `standards/testing.md` | 489 | 1-21, en especial §21 TDD, checklist |
| `standards/security.md` | 504 | 1-24, hallazgos y checklist |
| `commands/specify.md` | 520 | 1-18 |
| `commands/clarify.md` | 552 | 1-19 |
| `commands/plan.md` | 760 | 1-22 |
| `commands/tasks.md` | 754 | 1-22 |
| `commands/implement.md` | 920 | 1-26, en especial §17.1 |
| `commands/validate.md` | 766 | 1-23 |
| `templates/specification.template.md` | 412 | 1-17 y Q-001 |
| `templates/plan.template.md` | 646 | 1-23 |
| `templates/tasks.template.md` | 542 | 1-15 y TASK-001 |
| `templates/validation.template.md` | 717 | 1-27 |

## Contratos y citas vigentes

- `AGENTS.md` y `docs/tdd.md` citan testing §21.
- Artefactos históricos y `docs/reference.md` citan `/implement` §17.1.
- Un artefacto aprobado cita `/specify` §18; conservar su numeración.
- `src/check_harness_state.py` consume `**Estado:**`, `**Estado actual:**`,
  `spec.md`, `plan.md`, `tasks.md`, encabezados de TASK, tabla de orden,
  `SPEC COMPLIANCE: PASS` y `FEATURE STATUS: VALIDATED`.
- `docs/index.md` enlaza los 15 documentos; conservar rutas.

## Matriz de obligaciones para cotejo

| Fuente dueña | Obligación a preservar | Verificación posterior |
|-------------|------------------------|------------------------|
| Constitución I-III, XII | SPEC/PLAN/TASKS aprobados por humano antes de implementar; registro explícito | Comparación de artículos y gates |
| Constitución IV-V, XI | Requisito→AC→PLAN→TASK→cambio→prueba→validación; trabajo revisable | Comparación de artículos y templates |
| Constitución VI-VII | Evidencia y validación final antes de `VALIDATED` | Gate de `/validate` y template |
| Constitución VIII, Precedencia | Cambio en nivel dueño, reevaluación downstream, nueva aprobación si cambia contenido | Comandos y articles |
| Standards architecture/coding | Justificación, alcance mínimo, contratos, errores, compatibilidad, secretos | Control por sección |
| Standards testing §21 | RED real antes del cambio, GREEN, refactor opcional, excepción acotada y BLOCKED de entorno | Sección, comandos y templates |
| Standards security 1-24 | Entradas, permisos, secretos, datos, integraciones, operaciones destructivas, hallazgos | Control por sección |
| Commands specify/clarify | Requisitos verificables, preguntas bloqueantes, propagación y gate humano | Recorrido documental |
| Commands plan/tasks | Cobertura de MUST, decisiones, tests, TDD, dependencias y DoD | Recorrido documental |
| Command implement | Preflight, scope, pruebas, reapertura, evidencia, estados | Recorrido normal y §17.1 |
| Command validate | Coverage, findings, security, gaps, PASS/FAIL/BLOCKED | Recorrido de tres resultados |
| Templates | IDs, campos, estados, aprobaciones, trazabilidad y evidencia | Cotejo de campos |

La columna `Estado` de la tabla de orden de TASKS-009 registra progreso
operativo; los `TODO` junto a cada título describen el estado inicial del
documento aprobado. Esta convención mantiene la huella de la aprobación.

**TEST-001: PASS.** Las 15 rutas, conteos, contratos y controles clave están
inventariados. No se editó `.spec` durante TASK-001.
