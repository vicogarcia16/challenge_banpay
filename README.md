# Challenge Banpay :bank:

## Pre requisitos :pushpin:

* Clonar o descargar el repositorio en el directorio deseado:  
  **`git clone https://github.com/vicogarcia16/challenge_banpay`**

## Base de Datos :dvd:

* El proyecto utiliza **PostgreSQL** como sistema de gestión de base de datos.
* La base de datos se maneja mediante **SQLAlchemy**, que permite realizar operaciones CRUD para los usuarios.

## Instalación 🔧

### Local

1. Crear un entorno virtual en Python:
   * Ejecutar `pipenv install` para instalar las dependencias desde el `Pipfile`.

### Docker

1. Si deseas ejecutar el proyecto en Docker, ejecuta el siguiente comando en una ventana de terminal:
   ```bash
   docker-compose up -d

## Variables de entorno
1. El archivo .env.example es un ejemplo de como se debe configurar el archivo .env.
2. Recuerda que para la imagen Docker (depende de docker-compose.yml): 
    ```bash
    DB_HOST:db
    DB_PORT:5432
## Ejecución del Software ⚙️
### Local
1. El archivo principal es main.py
2. Para iniciar el servidor, ejecuta el siguiente comando:
    ```bash 
    pipenv run server
3. Accede a la aplicación a través de la URL por defecto: http://127.0.0.1:8000.
* Comandos adicionales:
    * test: Ejecuta las pruebas unitarias.
    * coverage: Muestra la cobertura de las pruebas.
    * coverage_erase: Resetea la cobertura de pruebas.
    * coverage_report: Muestra un reporte de cobertura en la terminal.
    * coverage_html: Genera un reporte de cobertura en formato HTML.
    * coverage_open: Abre el reporte de cobertura en formato HTML.
### Docker
1. Si has construido la imagen Docker, ejecuta el contenedor creado llamado "micro-service-fastapi".
2. Luego, abre el navegador y accede a la URL: http://localhost:8000

## Tecnologías Utilizadas 🛠️
* [Python](https://www.python.org/) - Lenguaje de programación
* [PostgreSQL](https://www.postgresql.org/) - Base de datos
* [FastAPI](https://fastapi.tiangolo.com/) - Framework Web
* [SQL Alchemy](https://www.sqlalchemy.org/) - Kit de herramientas SQL para Python
## Autor ✒️
* **Víctor García** [vicogarcia16](https://github.com/vicogarcia16) 

