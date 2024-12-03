# Challenge Banpay :bank:
Creación e implementación de una REST API que expone un CRUD de usuarios. Los usuarios deben tener un rol (admin, films, people, locations, 
species, vehicles) y se consumen datos con un GET de Studio Ghibli API, de acuerdo a su rol.

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
4. Comandos adicionales usados como  `pipenv run [comando]`:
    * test: Ejecuta las pruebas unitarias.
    * coverage: Muestra la cobertura de las pruebas.
    * coverage_erase: Resetea la cobertura de pruebas.
    * coverage_report: Muestra un reporte de cobertura en la terminal.
    * coverage_html: Genera un reporte de cobertura en formato HTML.
    * coverage_open: Abre el reporte de cobertura en formato HTML.
### Docker
1. Si has construido la imagen Docker, ejecuta el contenedor creado llamado "fastapi-app".
2. Luego, abre el navegador y accede a la URL: http://localhost:8000
### Autenticación
### Autenticación
* Para tener autorización sobre los endpoints protegidos 🧷:, se debe registrar un usuario y posteriormente loguearse.
![Endpoints protegidos](https://github.com/vicogarcia16/challenge_banpay/blob/main/images/protegidos.jpeg)
* Esto se realiza, para recibir el token de acceso (Nota: Dicho access token caduca a los 10 minutos y el refresh token caduca en 7 días)
![Login](https://github.com/vicogarcia16/challenge_banpay/blob/main/images/auth.jpeg)
* Con ello, se registra el token en [Authorize] de la documentación Swagger UI para poder hacer usos de los endpoints protegidos.
![Token](https://github.com/vicogarcia16/challenge_banpay/blob/main/images/token.jpeg)
* Si se quiere ejecutar los endpoints con Postman o Imsomnia. Insertar el token en Authorization.
![Postman](https://github.com/vicogarcia16/challenge_banpay/blob/main/images/postman.jpeg)

## Endpoints

Los endpoints en la siguiente imagen, se describen a continuacion:
![Listado de funciones](https://github.com/vicogarcia16/challenge_banpay/blob/main/images/endpoints.jpeg)
* authentication
   * POST
     * /login/ - Recibe un nombre de usuario y una contraseña y devuelve un token de acceso si el usuario existe en la base de datos.
     * /refresh/ - Recibe un refresh token y devuelve un nuevo access token si el refresh token es válido.
* user
  * POST
    * /user/ - Crea un nuevo usuario en la base de datos.
  * GET
    * /user/all/ - Obtiene todos los usuarios de la base de datos.
    * /user/{id}/ - Obtiene un usuario de la base de datos mediante su ID
  * PUT
    * /user/{id}/ - Actualiza un usuario de la base de datos mediante su ID.
  * DELETE
    * /user/{id}/ - Elimina un usuario de la base de datos mediante su ID.
* ghibli
  * GET
    * /ghibli/{username} - Obtiene los datos de Studio Ghibli según el rol del usuario:
                           (username: Nombre de usuario utilizado para identificar al usuario en la base de datos.
                            - Si el rol del usuario no es 'admin', se obtienen los datos específicos del rol (films, people, locations, species, vehicles).
                            - Si el rol del usuario es 'admin', se obtienen los datos de todos los roles combinados.

## Coverage

La cobertura del codigo que comprende las pruebas unitarias, se ha realizado al tiempo que se actualiza esta información. Nota: Para mas detalle, ir a la seccion Ejecucion del Software y ejecutar de manera local, el comando a elegir para mostrar el reporte.
![Coverage](https://github.com/vicogarcia16/challenge_banpay/blob/main/images/coverage.jpeg)

## Demostración de funcionalidad



## Tecnologías Utilizadas 🛠️
* [Python](https://www.python.org/) - Lenguaje de programación
* [PostgreSQL](https://www.postgresql.org/) - Base de datos
* [FastAPI](https://fastapi.tiangolo.com/) - Framework Web
* [SQL Alchemy](https://www.sqlalchemy.org/) - Kit de herramientas SQL para Python
* [JWT](https://jwt.io/) - Verificación de acceso con tokens
* [Pytest](https://docs.pytest.org/en/stable/) - Pruebas unitarias
## Autor ✒️
* **Víctor García** [vicogarcia16](https://github.com/vicogarcia16) 

