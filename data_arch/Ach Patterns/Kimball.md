# Technical Interview Exercise — Dimensional Modeling (Kimball)

## Contexto

El equipo de **BI** se queja de que los tableros en **Tableau tardan ~15 minutos en cargar**.

Al revisar el modelo dimensional de ventas diseñado por un **arquitecto anterior**, encuentras el siguiente diagrama.  
El equipo actual defiende el diseño argumentando que:

- Está en **Tercera Forma Normal (3NF)**
- Ahorra mucho espacio de almacenamiento
- No existe redundancia de datos

---
## Preguntas
- ¿Cómo se llama este antipatrón dentro de la metodología Kimball?
- ¿Por qué este diseño impacta tan negativamente el performance de herramientas BI como Tableau o Power BI?
- ¿Cuál es la solución exacta propuesta por Kimball para este problema?
- ¿Qué cambio específico harías tú en este modelo para mejorar el rendimiento?
- ¿Por qué este diseño puede ser correcto desde un punto de vista OLTP / 3NF, pero incorrecto para analytics?
## Modelo Actual de Ventas

```mermaid
graph TD
    A[Fact_Ventas] --> B(Dim_Producto)
    A --> C(Dim_Tiempo)
    A --> D(Dim_Tienda)

    B --> E(Dim_Categoria)
    E --> F(Dim_SubCategoria)
    F --> G(Dim_Marca)

    D --> H(Dim_Ciudad)
    H --> I(Dim_Estado)
    I --> J(Dim_Pais)

    style A fill:#f9f,stroke:#333,stroke-width:2px

