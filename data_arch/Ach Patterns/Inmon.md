# Adopción de la Metodología Bill Inmon (Corporate Information Factory)

La empresa decidió adoptar la **metodología de Bill Inmon (Corporate Information Factory)**.  
El equipo de ingeniería construyó esta solución con el objetivo de **entregar valor rápido** a los equipos de **Marketing** y **Finanzas**.

## Preguntas


## Arquitectura Implementada

El flujo de datos sigue el siguiente patrón:

```mermaid
graph LR
    S1[(CRM)] --> ST[Staging Area]
    S2[(ERP)] --> ST
    ST --> DM1[(Data Mart Mkt)]
    ST --> DM2[(Data Mart Finanzas)]
    DM1 --> EDW[(Enterprise Data Warehouse 3NF)]
    DM2 --> EDW

    style ST fill:#ff9,stroke:#333
    style EDW fill:#bbf,stroke:#333
    ```
