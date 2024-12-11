from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routers.get_form_route import form_router
from .db_connection import startup_db_client, shutdown_db_client


# Определение жизненного цикла для приложения fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Подключение к БД
    await startup_db_client(app)
    yield
    # Отключение от БД
    await shutdown_db_client(app)


app = FastAPI(title="E_Kom_TestTask",
    lifespan=lifespan,)


app.include_router(form_router)