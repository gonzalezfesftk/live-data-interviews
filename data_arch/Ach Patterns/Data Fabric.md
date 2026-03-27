El CIO leyó sobre **"Data Fabric"** en un reporte de Gartner y exigió implementarlo para conectar sistemas **On-Premise, AWS y Azure**.
El equipo de arquitectura propone el siguiente diseño.
Nota: Todo se mueve por ETL a un S3 central y le ponemos una capa semántica encima.
¿Cumplimos con la definición de Data Fabric?

## Notas importantes
Descentralizamos la arquitectura creando dominios, y contratamos a 10 ingenieros ultra-senior como equipo central para que le construyan los Data Products a cada dominio para asegurar la calidad. ¿Qué va a fallar aquí en el peor escenario?


### Fragmento de código

```mermaid
graph TD
    A[Postgres On-Prem] -->|ETL Nocturno| D[(S3 Central Datalake)]
    B[AWS DynamoDB] -->|ETL Nocturno| D
    C[Azure SQL] -->|ETL Nocturno| D
    D --> E[Capa Semántica Única]
    E --> F[Usuarios BI]

    style D fill:#f96,stroke:#333,stroke-width:2px
