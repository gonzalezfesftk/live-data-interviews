from pyspark.sql import SparkSession
from pyspark.sql.types import *
import random
import uuid

# 1. Iniciamos el motor
spark = SparkSession.builder \
    .appName("Entrevista_Live_SQL") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

print("Generando tablas en memoria (Users y Transactions)...")
df_users = spark.createDataFrame([(str(i), f"User_{i}", random.choice(['Premium', 'Free'])) for i in range(1, 101)], ["user_id", "name", "plan"])

tx_data = []
for _ in range(5000):
    uid = str(random.randint(1, 100))
    amount = round(random.uniform(10.0, 500.0), 2) if random.random() > 0.1 else None
    tx_data.append((str(uuid.uuid4()), uid, amount, random.randint(1672531200, 1704067200)))
    if random.random() > 0.8: # Ruido y duplicados
        tx_data.append(tx_data[-1])

df_tx = spark.createDataFrame(tx_data, ["tx_id", "user_id", "amount", "ts"])

# 2. MAGIA PARA EL LIVE CODING: Exponemos los DataFrames como tablas SQL
df_users.createOrReplaceTempView("users")
df_tx.createOrReplaceTempView("transactions")

print("✅ Tablas 'users' y 'transactions' listas. Usa spark.sql() para consultarlas.")

# ==========================================
# ESPACIO DE TRABAJO DEL CANDIDATO
# ==========================================

# Escribe tus queries aquí adentro y usa .show() para ver el resultado:
# spark.sql(""" SELECT * FROM users LIMIT 5 """).show()

#=================== Reto 1 ===================
#Usando un CTE, calcula el monto total gastado por cada usuario. 
#Luego, en la consulta principal, trae el user_id y name de los usuarios que no tienen 
# ninguna transacción registrada o cuyo total es nulo.


#=================== Reto 2 ===================
# La tabla transactions tiene transacciones duplicadas exactamente iguales y algunas con montos nulos.
#  Usando Window Functions, escribe un query que devuelva 
# un listado limpio con la última transacción válida (sin nulos) por usuario.

#=================== Reto 3 ===================
#Calcula el promedio móvil (rolling average) del monto de las últimas 3 
# transacciones de cada usuario, ordenado cronológicamente por ts. 
# Ignora los nulos.


#=================== Reto 4 ===================
# No lo vas a ejecutar, pero escríbeme aquí abajo cómo estructurarías el archivo .sql de un modelo dbt.
# Quiero que configures este modelo para que no se materialice en la base de datos (que sea efímero) y 
# quiero que uses una variable/macro de Jinja para inyectar dinámicamente el esquema de origen