El CIO leyó sobre **"Data Fabric"** en un reporte de Gartner y exigió implementarlo para conectar sistemas **On-Premise, AWS y Azure**.
El equipo de arquitectura propone el siguiente diseño.
Nota: Todo se mueve por ETL a un S3 central y le ponemos una capa semántica encima.
¿Cumplimos con la definición de Data Fabric?

## Notas importantes
Descentralizamos la arquitectura creando dominios, y contratamos a 10 ingenieros ultra-senior como equipo central para que le construyan los Data Products a cada dominio para asegurar la calidad. ¿Qué va a fallar aquí en el peor escenario?

## Preguntas
1. ¿Por qué se eligió ETL batch nocturno en lugar de virtualización, CDC o streaming?
2. ¿Qué tan actualizados estarán los datos para los usuarios BI?
3. ¿Qué pasa si un sistema requiere consumo en tiempo real?
4. ¿Cuántas copias de los datos existirán y dónde?
5. ¿Qué impacto tiene este diseño en costos de transferencia y almacenamiento?
6. ¿La capa semántica es única y centralizada o depende de una herramienta BI específica?
7. ¿Cómo se versiona y gobierna la capa semántica?
8. ¿Qué ocurre si otro dominio necesita una semántica diferente?
9. ¿Cómo se garantiza consistencia semántica entre equipos?
10. ¿La capa semántica se puede consumir vía APIs y no solo BI?
11. ¿Dónde se definen y ejecutan las políticas de seguridad?
12. ¿El control de acceso es centralizado o heredado de cada fuente?
13. ¿Cómo se maneja el data lineage extremo a extremo?
14. ¿Qué pasa con datos sensibles (PII) provenientes de distintas plataformas?
15. ¿Cómo se audita quién consumió qué datos y cuándo?
### Fragmento de código

```mermaid
graph TD
    A[Postgres On-Prem] -->|ETL Nocturno| D[(S3 Central Datalake)]
    B[AWS DynamoDB] -->|ETL Nocturno| D
    C[Azure SQL] -->|ETL Nocturno| D
    D --> E[Capa Semántica Única]
    E --> F[Usuarios BI]

    style D fill:#f96,stroke:#333,stroke-width:2px