from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:Acos306154@localhost:5433/reflex"
    },
    "apps": {
        "models": {
            "models": ["src.models.item_model","src.models.user_model", "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()