/*
RETO EN VIVO: MODELADO DIMENSIONAL
A continuación tienes un payload JSON representativo de nuestra API transaccional actual.
Tu objetivo es diseñar las sentencias DDL (CREATE TABLE) para un modelo analítico 
tipo Estrella (Star Schema) optimizado para tableros de BI.

Considera llaves primarias, foráneas y tipos de datos.

PAYLOAD DE EJEMPLO:
{
  "order_id": "ORD-9921",
  "timestamp": "2026-03-25T14:30:00Z",
  "customer": {
    "id": "CUST-402",
    "name": "Juan Perez",
    "region": "LATAM",
    "signup_date": "2024-01-15"
  },
  "items": [
    {"product_id": "P-10", "category": "Electronics", "price": 299.99, "qty": 1},
    {"product_id": "P-45", "category": "Accessories", "price": 15.50, "qty": 2}
  ],
  "payment": {
    "method": "Credit Card",
    "status": "Cleared"
  }
}
*/

-- Escribe tu DDL aquí abajo: