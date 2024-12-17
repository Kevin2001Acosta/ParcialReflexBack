# ParcialReflexBack
Solución backend para servir a una app front reflex que realiza un crud de Usuarios
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instalación, clonar el repositorio,
crear un ambiente virtual preferiblemente,
python -m venv env
instalar los requirements.txt y otros si hace falta.
pip install -r requirements.txt

La aplicación se trabaja con un orm que permite crear las tablas desde la ejecución de la aplicación.
El backend es ejecutado con FastAPI un framework web de alto rendimiento para construir APIs con Python 3.7+ basado en sugerencias de tipos estándar de Python.
Conexión al a base de datos, en main.py y db/tortoise_config.py en las credenciales de base de datos ingresar los valores de una base de datos local
"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

ejecución: uvicorn src.main:app --reload

