# Technical Interview Exercise — Data Vault 2.0 (Hub Customer)

## Contexto

Aquí tienes un **DataFrame de PySpark** que simula la llegada de **clientes nuevos** desde un sistema fuente.

Tu objetivo es **generar el Hub de Clientes (`Hub_Customer`)** siguiendo **estrictamente el estándar de Data Vault 2.0**.

---

## Datos de origen (simulados)

```python
data = [
    ("CUST_001", "2026-03-25T10:00:00Z", "CRM_SALESFORCE"),
    ("CUST_002", "2026-03-25T10:05:00Z", "CRM_SALESFORCE")
]

df_raw = spark.createDataFrame(
    data,
    ["business_key", "load_date", "record_source"]
)