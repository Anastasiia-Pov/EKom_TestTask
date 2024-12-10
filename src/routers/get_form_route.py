from fastapi import APIRouter, status, Request
from db_models.validators import ValidateForm
from db_models.form_model import FormTemplates


form_router = APIRouter(prefix="",
                        tags=["Forms"],)


@form_router.post("/get_form",
                  status_code=status.HTTP_200_OK,
                  summary='Соответствие форм',
                  )
async def get_form(request: Request):
    # получаем параметры из query-запроса и преобразуем в словарь
    data = dict(request.query_params)
    # валидируем входящие данные, получаем словарь с провалидированными входными данными
    validator = ValidateForm()
    valid_data = validator.main_validator(data)
    # получаем множество ключей входной формы
    incoming_keys = set(valid_data.keys())
    # отбираем из имеющихся шаблонов только те, в которых есть ключи и соответствует тип значения из пришедшей формы
    existing_keys_values = [{key: {"$exists": True, "$eq": value['type']}} for key, value in valid_data.items()]
    docs = await FormTemplates.find({"$or": existing_keys_values}).to_list()
    # перебираем отобранные документы
    docs_names = []
    for doc in docs:
        # получаем множество ключей документа и проверяем его на подмножество относительно пришедшей формы
        template_keys = set(doc.model_dump().keys())
        # исключаем поля id и name из множества
        template_keys.remove("id")
        template_keys.remove("name")
        # если ключи шаблона являются подмножеством пришедшей формы - извлекаем имя документа
        if template_keys.issubset(incoming_keys):
            docs_names.append(doc.name)
    if not docs_names:
        return {k: v['type'] for k, v in valid_data.items()}
    return docs_names
