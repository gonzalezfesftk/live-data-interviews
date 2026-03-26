# Caso: Implementación de Data Mesh con Equipo Centralizado

La organización cuenta con **50 unidades de negocio**.  
Para implementar una arquitectura **Data Mesh**, decidió crear un equipo central llamado **“Ingenieros de Data Mesh”**.

---

## Enfoque adoptado

- Se definen **dominios de negocio** (Ventas, HR, Logística, etc.).
- Cada dominio **no construye** sus propios Data Products.
- Cuando un dominio necesita un Data Product:
  - **Levanta un ticket** al equipo central de Data Mesh.
  - El **equipo central escribe el código y despliega** el Data Product correspondiente.
- El equipo central está compuesto por **10 ingenieros ultra-senior**, con el objetivo de:
  - Asegurar la calidad
  - Estandarizar prácticas
  - Acelerar el delivery

## Pregunta
Descentralizamos la arquitectura creando dominios, y contratamos a 10 ingenieros ultra-senior como equipo central para que le construyan los Data Products a cada dominio para asegurar la calidad.
¿Qué va a fallar aquí en el peor escenario
---

## Diagrama de flujo (estado real)

```mermaid
graph TD
    A[Dominio Ventas] -.-> |Levanta Ticket| B(Equipo Central Data Mesh)
    C[Dominio HR] -.-> |Levanta Ticket| B
    D[Dominio Logística] -.-> |Levanta Ticket| B

    B --> |Escribe código y despliega| E[Data Product Ventas]
    B --> |Escribe código y despliega| F[Data Product HR]
    B --> |Escribe código y despliega| G[Data Product Logística]

    style B fill:#f66,stroke:#333,stroke-width:3px