from httpx import AsyncClient
import pytest

# валидные шаблоны
form_1_1 = {"birthday": "1997-09-10",
            'num': "+7 123 456 78 90",
            'notification': 'message from user1'}

form_1_2 = {"field_date": "1997-09-10",
            "field_number": "+7 123 456 78 90"}

form_1_3 = {"email": "testuser@mail.com",
            "birthday": "10.09.1997",
            "info": "какой-то текст",
            "user": "+7 098 765 43 21",
            "text": "еще какой-то текст"}

form_1_4 = {"email": "testuser@mail.com",
            "date": "10.09.1997",
            "phone": "+7 098 765 43 21",
            "text": "еще какой-то текст"}

form_1_5 = {"email": "testuser@mail.com",
            "date": "10.09.1997",
            "user": "+7 098 765 43 21",
            "phone": "+7 098 765 43 21",
            "text": "здесь просто текст",
            "birthday": "10.09.1997",
            "notification": "text uvedomleniya"}

# невалидные шаблоны
form_0_1 = {"nonexisting_field": "1997-09-10",  # такого поля нет
            "field_1": "+7 123 456 78 90"}  # такого поля нет

form_0_2 = {"user_email_field": "testuser@mail.com"} # такого поля нет

form_0_3 = {"field_1": "testusermail.com", # почта не соответствует формату - определится как текст
            "phone": "+7 098 7654321", # телефон не соответствует формату - определится как текст
            "message": "текст",
            "date": "1997.09.10"}  # дата не соответствует формату - определится как текст

form_0_4 = {"birthday": "1997.10.09"} # такое поле есть, но дата не соответсвтует формату

form_0_5 = {"day": "1997-10-09"} # поля нет, но дата соответсвтует формату


async def test_form_1_1(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_1_1)
    assert response.status_code == 200
    data = response.json()
    assert data == ["Three Fields Form - Phone & Date & Text",
                    "Date Form",
                    "Text Form"]


async def test_form_1_2(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_1_2)
    assert response.status_code == 200
    data = response.json()
    assert data == ["Two Fields Form - Phone & Date"]


async def test_form_1_3(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_1_3)
    assert response.status_code == 200
    data = response.json()
    assert data == ["Two Fields Form - Text & Phone",
                    "Email Form",
                    "Phone Form",
                    "Date Form"
                    ]

async def test_form_1_4(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_1_4)
    assert response.status_code == 200
    data = response.json()
    assert data == ["Entering Form",
                    "Email Form"
                    ]

async def test_form_1_5(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_1_5)
    assert response.status_code == 200
    data = response.json()
    assert data == ["Entering Form",
                    "Two Fields Form - Text & Phone",
                    "Email Form",
                    "Phone Form",
                    "Date Form",
                    "Text Form"
                    ]

async def test_form_0_1(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_0_1)
    assert response.status_code == 200
    data = response.json()
    assert data == {"nonexisting_field": "date",
                    "field_1": "phone"
                    }

async def test_form_0_2(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_0_2)
    assert response.status_code == 200
    data = response.json()
    assert data == {"user_email_field": "email"
                    }

async def test_form_0_3(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_0_3)
    assert response.status_code == 200
    data = response.json()
    assert data == {"field_1": "text",
                    "phone": "text",
                    "message": "text",
                    "date": "text"
                    }

async def test_form_0_4(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_0_4)
    assert response.status_code == 200
    data = response.json()
    assert data == {"birthday": "text"}


async def test_form_0_5(test_client: AsyncClient):
    response = await test_client.post("/get_form",
                                      params=form_0_5)
    assert response.status_code == 200
    data = response.json()
    assert data == {"day": "date"}