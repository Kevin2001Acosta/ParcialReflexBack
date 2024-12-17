from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.routes import user_routes

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

register_tortoise(
    app,
    db_url="postgres://postgres:Acos306254@localhost:5433/reflex",
    modules={"models": ["src.models.item_model", "src.models.user_model"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# postgres://u6iawsuum6yppwl8gw8m:enYnJ28FMHOPaoND8fOB8Ej2II3Wso@bqa4ibsgbo0rtl9xv3la-postgresql.services.clever-cloud.com:50013/bqa4ibsgbo0rtl9xv3la