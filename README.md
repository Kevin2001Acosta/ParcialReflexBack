# ParcialReflexBack
Solución backend para servir a una app front reflex que realiza un crud de Usuarios
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instalación, clonar el repositorio,
crear un ambiente virtual preferiblemente,
instalar los requirements.txt y otros si hace falta.
pip install -r requirements.txt


Conexión al a base de datos, en main.py y db/tortoise_config.py en las credenciales de base de datos ingresar los valores de una base de datos local
"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

ejecución: uvicorn src.main:app --reload

