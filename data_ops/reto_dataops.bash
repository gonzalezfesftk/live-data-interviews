#!/bin/bash
# RETO EN VIVO:
# Este script falla aleatoriamente simulando problemas de red.
# Modifica el código para implementar un mecanismo de reintentos (Retries)
# que intente ejecutar la lógica principal hasta 3 veces con "Exponential Backoff"
# antes de fallar definitivamente con exit 1.

echo "Iniciando despliegue en producción..."

# --- LÓGICA A ENVOLVER EN REINTENTOS ---
if [ $((RANDOM % 10)) -gt 3 ]; then
    echo "ERROR: Fallo de conexión con el cluster remoto."
    exit 1
else
    echo "SUCCESS: Despliegue completado exitosamente."
    exit 0
fi
# ----------------------------------------