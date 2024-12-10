from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_HOST, MONGO_PORT, MONGO_DB
from db_models.form_model import FormTemplates
from forms_templates.start_up_templates import FORMS_TEMPLATES


DATABASE_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"


# добавление шаблонов в БД
async def insert_start_up_data(data: list[dict]):
    for f_t in data:
        existing_template_name = await FormTemplates.find_one(FormTemplates.name == f_t['name'])
        if not existing_template_name:
            template = FormTemplates(**f_t)
            await template.insert()
    print("Стартовые шаблоны внесены")


# подключение к БД
async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(DATABASE_URL)
    app.mongodb = app.mongodb_client.get_database(MONGO_DB)
    await init_beanie(database=app.mongodb, document_models=[FormTemplates])
    print("MongoDB подключена.")
    await insert_start_up_data(FORMS_TEMPLATES)
    print('MongoDB готова к работе.')


# Метод для отсоединения подключения к БД
async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("MongoDB отключена.")