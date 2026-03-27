# Live Coding Interview - Data Team

Bienvenido/a. Esta será una sesión interactiva de Live Coding.

##  Pre-requisitos (MUY IMPORTANTE)
Para no perder tiempo durante la entrevista, completa esto **ANTES** de nuestra llamada:

1. Ten instalado Docker Desktop.
2. Clona este repositorio.
3. Abre tu terminal en la raíz de este repositorio y ejecuta:
   `docker-compose up -d`
   *(La primera vez tardará en descargar la imagen de Spark, por favor hazlo con anticipación).*
4. Verifica que puedas entrar a `http://localhost:8888` en tu navegador. 

No resuelvas nada aún. Durante la sesión, te indicaré qué hacer.
## En caso de no porder instanciar la imagen

Si Docker presenta errores de red o certificados (común en versiones de macOS como la 2019), no pierdas tiempo. Levanta el entorno localmente:

Requisito: Tener instalado Java JDK 11.

Instala las dependencias:

Bash
python3 -m pip install pyspark==3.5.0 duckdb jupyterlab uuid
Lanza Jupyter Lab:

Bash
python3 -m jupyterlab



**Nota legal:** Este material es confidencial y de uso exclusivo para este proceso de entrevistas. Revisa el archivo `LICENSE` para más detalles.
