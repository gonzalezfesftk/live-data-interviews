from pyspark.sql import SparkSession
from pyspark.sql.types import *
import random
import uuid

# 1. Iniciamos Spark
spark = SparkSession.builder \
    .appName("Entrevista_Live") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

print("Generando catálogo de usuarios...")
df_users = spark.createDataFrame([(str(i), f"User_{i}", random.choice(['Premium', 'Free'])) for i in range(1, 101)], ["user_id", "name", "plan"])

print("Generando transacciones con ruido y duplicados...")
tx_data = []
for _ in range(5000):
    uid = str(random.randint(1, 100))
    amount = round(random.uniform(10.0, 500.0), 2) if random.random() > 0.1 else None
    tx_data.append((str(uuid.uuid4()), uid, amount, random.randint(1672531200, 1704067200)))
    if random.random() > 0.8: # Inyectamos duplicados
        tx_data.append(tx_data[-1])

df_tx = spark.createDataFrame(tx_data, ["tx_id", "user_id", "amount", "ts"])
print("✅ Entorno listo. df_users y df_tx disponibles en memoria.")

# RETO EN VIVO:
# Obtén un DataFrame final que contenga, por cada usuario Premium, 
# cuál fue su última transacción válida (amount no nulo) y el monto de esa transacción.
# Elimina los duplicados exactos a nivel sistema.