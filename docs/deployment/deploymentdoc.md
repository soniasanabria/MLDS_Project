Despliegue de modelos

Infraestructura
Nombre del modelo: predicción de incendios forestales 

Plataforma de despliegue: el modelo se desplegó en un servidor local una vez guardado el modelo en un formato pickle y posteriormente usando flask para crear la apliación web del microservicio. Hecho esto, se creo un contenedor e imagen docker.

El modelo fue probado inicialmente en el servidor local ejecutando por el terminal el archivo deploymentAPI.py y posteriomente usando postman para enviar los requerimientos tanto local como web al endpoint predict. /// Más abajo se describe cuál debe ser la estructura de los datos de entradas.

Requisitos técnicos: descritos en el documento requirements

versión de Python: python 3.11.3
Librerias: pandas== 1.5.3
scikit-learn==1.2.2
numpy== 1.22.4
Flask==1.1.4
markupsafe==2.0.1
gunicorn== 20.1.0
Flask-Cors== 4.0.0

Software: windows 10 home, RAM 8

Código de despliegue

Archivo principal: la aplicación diseñada está en el archivo deploymentAPIs.py el cual se encuentra en la raíz del directorio. Para la creación del contenedor e imagen docker se creó el archivo denominado dockerfile, así como el llamado requeriments los cuales también se encuentran en la raíz del directorio

Documentación del despliegue
Instrucciones de uso: el contendedor e imagen docker fueron denominados wild_fire_app

En la terminal:
Para crear el contenedor e imagen se debe ejecutar la operación: docker build -t wild_fire_app
Para correr la imagen docker se debe ejecutar la sentencia docker run -p 8000:8000 wild_fire_app
La exposición de la aplicación se configuró en el puerto 8000

En este caso se descargó y uso en la web la applicación web postman para enviar requerimientos al modelo. Solo se creo un endopoint denominado predict

Datos de entrada:
Los datos de entrada se reciben en formato JSON en los rangos descritos en data summary. Se puede enviar un solo request o una secuencia de ellos en formato JSON. 

ejemplo:
{   "NDVI":"0.4656",
    "LST":"14964.32",
    "BURNED_AREA":"4.812"
}

O una secuencia

[
    {
        "NDVI":"0.4656",
        "LST":"14964.32",
        "BURNED_AREA":"4.812"
    },
    {
        "NDVI":"0.47",
        "LST":"15000.14",
        "BURNED_AREA":"4.79"
    }
]