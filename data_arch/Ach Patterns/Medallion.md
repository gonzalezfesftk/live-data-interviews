# Caso: Revisión de Pipeline Lakehouse con Arquitectura Medallón

Estás revisando un pipeline de un **Lakehouse en Databricks** que utiliza la arquitectura **Medallón** con capas **Bronze, Silver y Gold**.

---
## Pregunta 
Extraemos datos diarios de una API.
Para ahorrar almacenamiento en el Lakehouse, nuestro pipeline hace un UPSERT (Merge) directamente en la capa Bronze, manteniendo solo la imagen más reciente de cada cliente.
Luego limpiamos en Silver y agregamos en Gold.
Detecta el error catastrófico
## Contexto del Pipeline

- Los datos se extraen **diariamente desde una API externa**.
- Para **ahorrar almacenamiento**, el pipeline:
  - Realiza un **UPSERT (MERGE)** directamente en la capa **Bronze**.
  - Mantiene **solo la imagen más reciente de cada cliente**.
- Posteriormente:
  - En **Silver**, se limpian nulos y se formatea la información.
  - En **Gold**, se realizan **agregaciones de negocio** para consumo analítico.

---

## Diagrama de flujo (estado actual)

```mermaid
graph LR
    API[API Externa] -->|Sobreescribe Diario / UPSERT| BRONZE[(Capa Bronze)]
    BRONZE -->|Limpia nulos y formatea| SILVER[(Capa Silver)]
    SILVER -->|Agregaciones de Negocio| GOLD[(Capa Gold)]

    style BRONZE fill:#cd7f32,stroke:#333
    style SILVER fill:#c0c0c0,stroke:#333
    style GOLD fill:#ffd700,stroke:#333