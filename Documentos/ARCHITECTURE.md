Arquitectura canónica inicial
1. Núcleo
Lex Core vive como dominio jurídico dentro de Verbum Core. La cadena operativa es:

Agent → Task → Context → Tool → Evidence → Reason → Validate → Result

2. Modelo
Norm, Fact, Evidence, Element, Relation, Rule, Result.

3. Regla de oro
Una conclusión crítica no se presenta como verdad jurídica cuando faltan elementos, evidencia, vigencia o validación.

4. Event Ledger
Cada ejecución usa task_id y correlation_id y registra TASK, CLASSIFY, REASON, VALIDATE, RESULT. La implementación se extenderá con REQUEST_EVIDENCE y RECEIVE_EVIDENCE al integrar almacenamiento persistente.

5. Evidencia
El grafo permite reconstruir Evidence → Fact → Element → Norm → Rule → Conclusion.
