LEX CORE / MOTOR PENAL — ARCHIVO MAESTRO DE CONTINUIDAD
Proyecto: Tu-aboga2-Cuba / Lex Core
Repositorio objetivo: https://github.com/Arman2mar/Tu-aboga2-cuba.git
Fecha de reconstrucción: 2026-08-17
Estado: reconstrucción previa al repositado — NO escribir código definitivo hasta cerrar esta memoria.

1. PROPÓSITO
Este archivo conserva la memoria técnica y conceptual necesaria para retomar el motor jurídico superior que se venía diseñando antes de cambiar de pantalla/configuración.

No se trata de un chatbot jurídico convencional.

El objetivo es construir un Motor de Razonamiento Jurídico Auditable, inicialmente especializado en Derecho Penal cubano, pero diseñado desde el principio para crecer hacia Civil, Administrativo, Militar, Mercantil/Empresarial, Laboral, Tributario y otras ramas.

La aplicación Tu-aboga2-cuba debe considerarse una capa de producto/usuario; Lex Core debe ser el núcleo jurídico reutilizable.

2. PRINCIPIO CENTRAL
El sistema no debe limitarse a recuperar textos legales ni a generar respuestas plausibles.

Debe poder representar y relacionar:

HECHO → NORMA → ELEMENTO JURÍDICO → EVIDENCIA → RELACIÓN → REGLA → CALIFICACIÓN → CONSECUENCIA → EXPLICACIÓN

Toda conclusión jurídicamente relevante debe poder remontarse a:

qué hecho fue considerado;
qué evidencia lo respalda;
qué norma/regla se aplicó;
qué elementos jurídicos fueron satisfechos;
qué relaciones fueron inferidas;
qué incertidumbres quedaron;
qué versión/vigencia de la norma se utilizó.
3. ARQUITECTURA SUPERIOR RECORDADA
La arquitectura se apoya en el diseño de Verbum Core / VTS Open Agent Stack.

Contrato operativo:

Agent → Task → Context → Tool → Evidence → Reason → Validate → Result

Lex Core es un dominio especializado dentro de ese runtime.

La IA/LLM NO debe ser la autoridad jurídica final.

Debe poder utilizarse como:

interfaz conversacional;
extracción de hechos;
clasificación;
búsqueda;
ayuda en formulación;
generación de borradores;
explicación.
Pero la determinación jurídica crítica debe poder ejecutarse y validarse mediante estructuras y reglas explícitas.

4. MODELO JURÍDICO NUCLEAR
Entidades conceptuales mínimas:

Norma
identificador
tipo de norma
órgano emisor
fecha
vigencia
versión
jurisdicción
texto/fuente
artículos/incisos/apartados
relaciones con otras normas
derogaciones/modificaciones
Hecho
identificador
descripción
sujeto
fecha/lugar
estado: afirmado / probado / controvertido / desconocido
fuente de origen
Evidencia
identificador
tipo
origen
documento/testimonio/registro/etc.
relación con uno o más hechos
fuerza/estado de validación
trazabilidad
Elemento jurídico
Representa una condición que una norma exige satisfacer.

Ejemplo penal:

conducta
sujeto
objeto
resultado
relación causal
elemento subjetivo
circunstancia
condición especial
Relación
Ejemplos:

norma_modifica_norma
norma_deroga_norma
hecho_satisface_elemento
evidencia_sustenta_hecho
norma_define_delito
hecho_instaura_riesgo
sujeto_participa
consecuencia_deriva_de_regla
Regla
Una condición computable que transforma hechos/evidencias/elementos en una conclusión.

Resultado
Debe contener:

conclusión
fundamentos
evidencia utilizada
normas utilizadas
reglas ejecutadas
incertidumbres
trazabilidad
nivel de confianza/estado, sin convertir una puntuación probabilística en “verdad jurídica”.
5. MOTOR PENAL — PRIMER DOMINIO COMPLETO
La razón de comenzar por Penal es que obliga al motor a manejar una estructura jurídica rigurosa.

Pipeline conceptual:

HECHO → CONDUCTA → TIPO PENAL → ELEMENTOS DEL TIPO → EVIDENCIA → ELEMENTOS OBJETIVOS → ELEMENTOS SUBJETIVOS → ANTIJURIDICIDAD → CULPABILIDAD → GRADO DE PARTICIPACIÓN → TENTATIVA / CONSUMACIÓN → AGRAVANTES / ATENUANTES → CONSECUENCIA JURÍDICA

El motor debe evitar la simplificación de:

“La persona hizo X, por tanto cometió Y.”

Debe comprobar las condiciones necesarias.

Estructura penal general
1. Identificación del hecho

quién
qué
cuándo
dónde
cómo
contra quién/qué
resultado
2. Identificación de posibles tipos

norma aplicable
elementos exigidos
exclusiones
conflictos entre tipos
3. Matching de elementos Cada elemento debe quedar en uno de estos estados:

satisfecho
no satisfecho
parcialmente acreditado
controvertido
desconocido
4. Evidencia Cada afirmación debe poder enlazarse a evidencia.

5. Análisis jurídico El motor ejecuta las reglas aplicables.

6. Validación Busca:

contradicciones
elementos faltantes
norma derogada
norma no vigente
evidencia insuficiente
hechos incompatibles
ambigüedad
7. Resultado No solamente “delito sí/no”.

Debe poder producir:

posible calificación
elementos satisfechos
elementos pendientes
evidencia faltante
normas aplicables
alternativas jurídicas
incertidumbres
siguiente acción recomendada
6. CRECIMIENTO A OTRAS RAMAS
La arquitectura debe ser común.

Penal
hecho → tipo penal → elementos → evidencia → imputación → consecuencia

Civil
hecho → relación jurídica → derecho/obligación → incumplimiento → daño → responsabilidad → reparación

Administrativo
hecho → potestad administrativa → obligación → infracción → procedimiento → sanción

Militar
hecho → condición/sujeto militar → deber jurídico → infracción → régimen especial → consecuencia

Mercantil/Empresarial
acto → sujeto empresarial → contrato/obligación → incumplimiento → responsabilidad → consecuencia

Laboral
relación laboral → obligación → incumplimiento → infracción → consecuencia

Tributario
hecho imponible → sujeto → obligación → incumplimiento → determinación → sanción/consecuencia

La arquitectura común debe evitar duplicar el motor.

Cada rama aporta:

ontología especializada;
tipos de norma;
elementos;
reglas;
procedimientos;
consecuencias.
7. CASOS CUBANOS YA IDENTIFICADOS PARA TESTS
Caso real de referencia
Multa a joven emprendedor/barbero:

fecha: 10/08/2026
talón: 422215
disposición indicada: DL 91
artículo: 12
inciso: B
importe: 16.000 CUP
hecho declarado: ausencia de factura de determinadas mercancías recibidas en paquetes desde el exterior.
Este caso debe servir para probar:

identificación normativa;
hecho vs. fundamento jurídico;
correspondencia artículo/inciso;
evidencia;
cuantía;
trazabilidad;
detección de posibles errores de tipificación.
Caso laboral
Empleo de personas sin contrato.

Referencia ya conservada: bajo DL 91/2024, art. 12-H corresponde la conducta: “Emplear personas sin haber concertado el contrato de trabajo conforme a lo establecido en la legislación laboral vigente”.

Debe mantenerse separado de otros incisos/conductas del mismo artículo.

Caso tributario
Resolución 306/2023 del MFP, publicada en Gaceta Oficial No. 15, edición Ordinaria de 2024 (GOC-2024-15-O5).

Debe utilizarse para probar:

obligaciones tributarias;
sujetos MIPYME;
reglas tributarias/financieras/precios;
vigencia y fuente normativa.
8. AZAN GESTORÍA COMO CASO DE DOMINIO EMPRESARIAL
La publicación de Azan Gestoría proporciona un excelente conjunto de casos de uso reales:

constitución y estructura de MIPYMES;
estatutos;
contratación estratégica;
revisión/auditoría de contratos;
cumplimiento normativo;
evaluación de riesgos;
preparación ante inspecciones;
traspaso de participaciones;
reestructuración corporativa;
educación jurídica preventiva.
Conceptualmente, esto valida una orientación de Legal Preventive / Compliance, no únicamente defensa reactiva.

El motor debe poder pasar de:

“¿Qué pasó y cómo me defiendo?”

a:

“¿Qué debo hacer para no incurrir en el riesgo?”

y posteriormente:

“¿Qué cambió en mi situación jurídica y qué obligaciones/riesgos aparecen ahora?”

9. RELACIÓN CON VERBUM CORE
El motor jurídico debe aprovechar el runtime general:

Task → Context → Tool → Evidence → Reason → Validate → Result

Ejemplo:

TASK
Analizar viabilidad jurídica de una actividad.

CONTEXT
Actividad + sujetos + forma jurídica + hechos + documentos.

EVIDENCE
Normas + documentos aportados + registros.

CLASSIFICATION
Mercantil + tributario + laboral + administrativo.

REASON
Aplicación de reglas.

VALIDATE
Comprobar vigencia, contradicciones y evidencia.

RESULT
Mapa jurídico + obligaciones + riesgos + acciones.

Todo evento relevante debe poder quedar trazado.

10. EVIDENCE GRAPH
La arquitectura debe prever un grafo de evidencia.

Ejemplo:

Evidence E1 → sustenta Fact F1

Fact F1 → satisface Element EL1

Element EL1 → requerido_por Norm N1

Norm N1 → pertenece_a Article A1

Rule R1 → utiliza N1 + EL1 + F1

Rule R1 → produce Conclusion C1

Esto permite reconstruir la cadena de razonamiento.

11. AUDITORÍA Y TRAZABILIDAD
Cada ejecución debería producir un historial/event ledger.

Conceptos ya definidos en Verbum Core:

IDs tipados: EntityID, TaskID, EventID, EvidenceID, SourceID, AgentID.
Eventos:
TASK
CLASSIFY
REQUEST_EVIDENCE
RECEIVE_EVIDENCE
REASON
VALIDATE
RESULT
Debe existir un correlation_id común y una cadena de causation_id.

Esto permite reconstruir cómo se llegó al resultado.

12. REGLA DE ORO DEL PROYECTO
No construir primero la interfaz.

Primero:

modelo jurídico;
normas;
hechos;
evidencia;
elementos;
relaciones;
reglas;
razonamiento;
validación;
trazabilidad;
tests;
API/capa de aplicación.
La interfaz de Tu-aboga2-Cuba se monta después.

13. ESTRUCTURA DE REPOSITORIO PROPUESTA
Pendiente de confirmar contra cualquier trabajo previo recuperable antes de congelarla.

Una dirección conceptual:

Tu-aboga2-cuba/
├── README.md
├── LICENSE
├── docs/
│   ├── ARCHITECTURE.md
│   ├── LEGAL_MODEL.md
│   ├── PENAL_ENGINE.md
│   ├── EVIDENCE_GRAPH.md
│   ├── RULE_ENGINE.md
│   └── ROADMAP.md
├── src/
│   └── lex_core/
│       ├── domain/
│       │   ├── norm.py
│       │   ├── fact.py
│       │   ├── evidence.py
│       │   ├── element.py
│       │   ├── relation.py
│       │   ├── rule.py
│       │   └── result.py
│       ├── reasoning/
│       ├── validation/
│       ├── evidence/
│       ├── branches/
│       │   └── penal/
│       └── runtime/
├── tests/
│   ├── domain/
│   ├── penal/
│   ├── evidence/
│   └── integration/
└── examples/
IMPORTANTE: esta estructura es una propuesta de reconstrucción, NO debe considerarse todavía el estado histórico definitivo hasta completar la búsqueda de material anterior.

14. PRINCIPIOS DE DISEÑO
Determinismo donde sea jurídicamente crítico.
Evidencia antes que afirmación.
Norma versionada.
Vigencia explícita.
Trazabilidad completa.
Separación entre hecho y conclusión.
Separación entre recuperación y razonamiento.
LLM como componente asistivo, no como autoridad.
Arquitectura modular por ramas.
Tests jurídicos reproducibles.
Offline-first cuando sea necesario.
Reutilización sobre Verbum Core.
Posibilidad de sustitución de componentes.
Ninguna conclusión importante sin fundamento recuperable.
Toda incertidumbre debe ser visible.
15. ESTADO DEL REPOSITORIO OBJETIVO
Repositorio: Arman2mar/Tu-aboga2-cuba

Estado comprobado al reconstruir esta memoria:

público;
rama principal: main;
repositorio prácticamente vacío;
sin código/documentación sustantiva visible actualmente;
la conexión GitHub disponible para esta sesión tiene permiso de lectura, no de escritura.
Por tanto:

NO SE DEBE INTERPRETAR EL REPOSITORIO ACTUAL COMO EL ESTADO DEL DISEÑO HISTÓRICO.

La arquitectura histórica debe reconstruirse primero desde conversaciones, archivos y memoria de proyecto.

16. FUENTES INTERNAS RECUPERADAS
Se revisó la búsqueda de archivos de conversación/biblioteca para términos como:

Lex Core
Motor Penal
Tu-aboga2-cuba
evidencia
norma/hecho
arquitectura jurídica
La búsqueda recuperó principalmente documentos generales y no encontró todavía un archivo único que contenga todo el diseño histórico del Motor Penal.

Sí confirmó material relacionado con:

arquitectura modular;
Event Ledger;
expediente digital;
motor de reglas;
evidencia y validaciones;
arquitectura API;
principios de Verbum Core.
Esto significa que este documento es una memoria de reconstrucción, no una afirmación de que se haya recuperado literalmente cada palabra del diseño histórico.

17. PRÓXIMO ESTADO DE TRABAJO
Antes de escribir código en GitHub:

Fase A — Recuperación
localizar todos los documentos específicos de Lex Core;
localizar cualquier documento específico del Motor Penal;
localizar diseños/diagramas;
localizar versiones anteriores del modelo de datos;
localizar cualquier código previo;
localizar decisiones que contradigan la estructura propuesta aquí.
Fase B — Consolidación
Crear una única especificación canónica.

Fase C — Motor Penal
Implementar el primer dominio completo.

Fase D — Tests
Construir casos jurídicos reproducibles.

Fase E — Repositorio
Recién entonces crear estructura y código en Tu-aboga2-cuba.

18. FRASE DE CONTINUIDAD
Cuando se retome este proyecto, la referencia debe ser:

“Retomar Lex Core / Motor Penal desde el Archivo Maestro de Continuidad. No empezar desde cero y no repositar hasta comparar la memoria con todo el material recuperable.”

Estado: MEMORIA MAESTRA PRELIMINAR
Uso: continuidad técnica, jurídica y de repositorio
Última actualización: 2026-08-17
