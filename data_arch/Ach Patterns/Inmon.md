# Adopción de la Metodología Bill Inmon (Corporate Information Factory)

La empresa decidió adoptar la **metodología de Bill Inmon (Corporate Information Factory)**.  
El equipo de ingeniería construyó esta solución con el objetivo de **entregar valor rápido** a los equipos de **Marketing** y **Finanzas**.

## Preguntas
1. ¿Este enfoque respeta realmente los principios de la metodología Inmon?
2. ¿Tiene sentido construir Data Marts antes del EDW en una arquitectura Inmon?
3. ¿Qué riesgos existen al considerar la consolidación hacia el EDW como una actividad secundaria?
4. ¿Cómo se garantiza la calidad e integración de datos si los Data Marts son la primera capa de consumo?
5. ¿Qué impacto puede tener esta decisión en la gobernanza y trazabilidad de la información?
6. ¿Este diseño podría generar dependencias difíciles de revertir en el futuro?
7. ¿En qué escenarios este enfoque híbrido podría estar justificado?
8. ¿Qué alternativas arquitectónicas podrían alinearse mejor con la necesidad de entrega rápida sin comprometer el modelo corporativo?

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