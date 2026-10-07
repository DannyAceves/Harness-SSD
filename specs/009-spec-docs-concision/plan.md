# Plan Técnico: Concisión de los documentos `.spec`

**ID:** PLAN-009  
**SPEC relacionada:** SPEC-009 v0.1.0  
**Estado:** APPROVED  
**Versión:** 0.1.0  
**Fecha:** 2026-10-07

# 1. Precondiciones

- [x] SPEC-009 v0.1.0 aprobada y registrada en DECISION-001.
- [x] `python3 src/check_harness_state.py`: PASS.
- [x] Sin aclaraciones bloqueantes; FR/NFR MUST tienen AC.

# 2. Resumen técnico

Editar los 15 Markdown existentes de `.spec` en su ubicación actual. Reducir
texto repetido, ejemplos y espacio vertical; escribir reglas concisas y
remisiones precisas. Conservar los contratos documentales y los identificadores
de secciones usados por el Harness. Verificar contenido, referencias y tamaño.

# 3. Requisitos cubiertos

| Requisito | Cobertura del plan |
|-----------|--------------------|
| FR-001, NFR-001 | Inventario y reducción de los 15 archivos; conteo individual y total |
| FR-002, BR-001 | Comparación por obligación de gates, estados, TDD, seguridad y excepciones |
| FR-003, NFR-002 | Commands operables, standards con controles, templates con campos e IDs |
| FR-004 | Preservar números de sección y comprobar rutas/referencias; checker PASS |

# 4. Contexto técnico existente

- Repositorio SDD documental; herramientas Python 3 estándar en `src/` y
  pruebas `unittest` en `tests/`. Sin framework, BD ni gestor de paquetes
  relevantes para este cambio.
- Baseline: 15 Markdown, 8,672 líneas; diez sobre 500. El mayor es
  `.spec/commands/implement.md` con 920. `architecture.md` tiene 288 y
  también debe reducirse.
- Las secciones numeradas tienen consumidores: `AGENTS.md` y `docs/tdd.md`
  citan testing §21; evidencia histórica cita `/implement` §17.1. El checker
  consume encabezados y campos de estado de SPEC/PLAN/TASKS, y las plantillas
  definen su forma.
- `docs/index.md` enumera los documentos por fase. No hay ADR relevante.

# 5. Decisiones técnicas

## DEC-001 — Preservar anclas y contratos

**Decisión:** Mantener rutas, títulos de secciones numeradas y subapartados
citados, IDs, nombres de campos y literales de estados/gates. Condensar el
contenido dentro de esas secciones. Comparar referencias antes y después.
**Justificación:** FR-002/FR-004, AC-002/AC-004.  
**Alternativas:** Renumerar y corregir todas las citas (más riesgo para
históricos); conservar archivos completos (no resuelve FR-001).  
**Consecuencia:** Algunas secciones serán muy breves, pero localizables.  
**ADR:** NO.

## DEC-002 — Fuente normativa única, remisión precisa

**Decisión:** Para una regla repetida, dejar su formulación completa en el
nivel de autoridad dueño y en el documento de fase conservar la acción local
con una referencia concreta. No sustituir precondiciones, prohibiciones o
transiciones por un enlace genérico. Suprimir ejemplos repetidos y explicaciones
que duplican la regla sin añadir un caso distinto.
**Justificación:** FR-001/FR-002/FR-003, NFR-002.  
**Alternativas:** Recorte lineal por longitud (puede perder normas); mover
todo a otra guía (aumenta navegación y dispersión).  
**Consecuencia:** Es necesario cotejar cada obligación contra la versión
anterior.  
**ADR:** NO.

## DEC-003 — Templates compactas, esquema intacto

**Decisión:** Conservar campos de aprobación, estado, trazabilidad, preguntas,
pruebas y validación de las cuatro templates; usar una instancia breve por
estructura y eliminar ejemplos duplicados y texto didáctico redundante.
Comprobar que los encabezados/campos esperados por `check_harness_state.py`
siguen presentes.
**Justificación:** FR-003/FR-004, AC-003/AC-004.  
**Alternativas:** Template mínima sin campos (artefactos incompletos).  
**Consecuencia:** Las instrucciones de uso quedan en el command de cada fase.
**ADR:** NO.

## DEC-004 — Verificación sin nuevos componentes

**Decisión:** Usar `wc -l`, búsquedas `rg`, diff, el checker y los tests
existentes; registrar una matriz editorial de reglas y resultados en evidencia
de SPEC-009. Hacer recorridos documentales de las seis fases y de los cuatro
templates. No añadir dependencia ni script permanente por una edición puntual.
**Justificación:** AC-001 a AC-004; el repositorio ya tiene controles útiles.  
**Alternativas:** Comprobación solo por líneas (insuficiente para equivalencia);
nuevo validador permanente (alcance no solicitado).  
**Consecuencia:** La equivalencia semántica requiere revisión humana de la
evidencia, además de checks automáticos.  
**ADR:** NO.

# 6. Arquitectura propuesta

No cambia la arquitectura. La Constitución conserva precedencia; standards
conservan políticas transversales; commands describen la fase; templates
aportan campos. `docs/index.md` sigue siendo el índice de entrada.

# 7. Modelo de datos

No hay persistencia ni migraciones. El formato documental de estados,
aprobaciones y trazabilidad se conserva. `decisions.json` de esta feature
registra aprobaciones según el protocolo existente.

# 8. Interfaces y contratos

Los contratos afectados son Markdown: rutas y secciones citadas, IDs de
requisitos/AC/tareas/pruebas, campos de los cuatro artefactos, y literales que
consume el checker (`**Estado:**`, `**Estado actual:**`, `APPROVED`,
`COMPLETED`, `SPEC COMPLIANCE: PASS`, `FEATURE STATUS: VALIDATED`). No API.

# 9. Validación de entradas

No hay entrada de usuario nueva. Los cambios se cotejarán con el inventario
de 15 rutas y con las referencias existentes para evitar omisiones.

# 10. Seguridad

Conservar todos los controles de `.spec/standards/security.md`, en especial
secretos, permisos, límites de confianza, operaciones destructivas, seguridad
de agentes y hallazgos. No registrar secretos en la evidencia ni introducir
integraciones o dependencias.

# 11. Estrategia de pruebas

| Criterio | Verificación prevista |
|----------|-----------------------|
| AC-001 | `wc -l` antes/después por los 15 archivos y total |
| AC-002 | Matriz de reglas previas/nuevas por sección; revisión de diff y gates |
| AC-003 | Recorrido documental de seis commands y cuatro templates con artefactos existentes como casos |
| AC-004 | `rg` de rutas/secciones/campos; checker; suite existente de estado/adopción |

## 11.1 Estrategia TDD

No cambia comportamiento ejecutable ni código productivo; el resultado es
documentación normativa. RED/GREEN no aplica a la prosa. Si durante TASKS se
define una comprobación automatizable nueva, se realizará RED antes del cambio
correspondiente según testing §21. Las verificaciones anteriores y la revisión
de equivalencia son la alternativa para este alcance documental.

# 12. Observabilidad

No aplica logging, métricas ni health checks. La evidencia tendrá conteos,
comandos ejecutados, resultados y referencias a las secciones revisadas.

# 13. Impacto en el repositorio

| Acción | Archivos |
|--------|----------|
| MODIFY | Los 15 Markdown actuales de `.spec` |
| MODIFY si una cita queda rota | Solo referencia vigente afectada en `AGENTS.md` o `docs/`; preservar históricos aprobados |
| REUSE | `docs/index.md`, `src/check_harness_state.py`, `tests/` y comandos existentes |
| CREATE durante implementación | Evidencia de SPEC-009 bajo `specs/009-spec-docs-concision/evidence/` |
| REMOVE | Ninguno |

La lista cerrada comprende 1 Constitución, 6 commands, 4 standards y 4
templates. No se modificarán `src/` ni `tests/` por esta feature.

# 14. Dependencias

Ninguna nueva. Solo Python estándar, `rg`, `wc`, `git` y herramientas ya
presentes.

# 15. Configuración

Ningún cambio de configuración ni variable de entorno.

# 16. Migración y compatibilidad

**Breaking changes:** NO. Conservar las rutas, encabezados con citas, campos
y valores de estado. Si una compactación exige cambiar un contrato, detener
el trabajo afectado y reevaluar SPEC/PLAN y sus gates.

# 17. Manejo de errores

- Regla ambigua o perdida: restaurar su formulación y revisar equivalencia.
- Referencia rota: conservar el ancla o corregir solo la cita vigente afectada.
- Límite de 300/4,500 incompatible con FR-002: detener el recorte afectado,
  documentar la excepción y revisar la SPEC; nunca omitir una obligación.
- Checker o pruebas en FAIL: identificar el contrato roto y corregirlo antes
  de cerrar la tarea; no relajar tests para obtener PASS.

# 18. Riesgos técnicos

## RISK-001 — Pérdida de norma al abreviar

**Impacto:** HIGH. **Probabilidad:** MEDIUM. **Mitigación:** cotejo por
sección/regla, diff y revisión de fuerza normativa antes de medir líneas.

## RISK-002 — Referencia o parser roto

**Impacto:** MEDIUM. **Probabilidad:** MEDIUM. **Mitigación:** conservar anclas,
campos y literales; buscar referencias y ejecutar checker/suite existente.

## RISK-003 — Presupuesto de líneas demasiado estricto

**Impacto:** MEDIUM. **Probabilidad:** MEDIUM. **Mitigación:** reducir ejemplos y
duplicaciones primero; si persiste conflicto, activar revisión de SPEC.

# 19. Aclaraciones técnicas

No hay `Q-TECH` bloqueantes. Las decisiones editoriales locales se resuelven
con DEC-001 a DEC-004 y la precedencia vigente.

# 20. ADR requeridos

Ninguno: no cambia arquitectura ni tecnología.

# 21. Orden de implementación

1. Congelar inventario y reglas/citas vigentes para comparación.
2. Compactar Constitución y standards, cotejando controles.
3. Compactar commands siguiendo el flujo SDD y preservando secciones.
4. Compactar templates con campos y ejemplos mínimos.
5. Revisar citas, recorridos documentales, conteos, checker y tests; registrar
   evidencia y corregir discrepancias dentro del alcance aprobado.

# 22. Criterios para avanzar a Tasks

- [x] SPEC aprobada, todos los MUST cubiertos y 15 rutas identificadas.
- [x] Estrategia de seguridad, verificación y compatibilidad definida.
- [x] Sin dependencias nuevas, migraciones, ADR o aclaraciones bloqueantes.
- [x] Aprobación humana explícita y registro durable del PLAN.

# 23. Estado del plan

**Estado actual:** APPROVED  
**Aprobado por:** Usuario responsable del proyecto  
**Fecha de aprobación:** 2026-10-07  
**Decisión explícita y alcance:** "Aprobado" en respuesta a la solicitud de
aprobación de PLAN-009 v0.1.0; autoriza preparar TASKS-009 para la reducción
documental de SPEC-009.  
**Registro durable:** `decisions.json`, DECISION-002.
