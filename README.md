# EKom_TestTask

## Виртуальная среда
Необходимые для установки пакеты представлены в файле [requirements.txt](https://github.com/Anastasiia-Pov/EKom_TestTask/blob/main/requirements.txt). 
Установка зависимостей осуществляется командой `pip install -r requirements.txt`.

## Файл .env - переменные среды
Пример файла .env представлен в [.env.example](https://github.com/Anastasiia-Pov/EKom_TestTask/blob/main/.env.example).
Перед запуском основного приложения необходимо заполнить данные поля в соответствии с указанными типами.

## Запуск основного приложения
Находясь в родительской директории проекта выполните в консоле команду `uvicorn src.main:app --reload`.
При успешном запуске появятся логи и сообщения о готовности БД и загрузке в нее тестовых шаблонов форм.

## Запуск скрипта для тестовых запросов
Скрипт для запуска тестовых запросов - [script.py](https://github.com/Anastasiia-Pov/EKom_TestTask/blob/main/script_for_auto_requests/script.py).
После того как запущена основная программа приложения (пункт выше), запустите файл `script`.
В данном файле реализовано консольное приложение с помощью `sys.stdin`: пользователь вводит в каждой новой строке `поле:значение`.
Если необходимо остановить ввод - comand+D.

## Запуск тестов
Тесты реализованы в файле [test_requests.py](https://github.com/Anastasiia-Pov/EKom_TestTask/blob/main/tests/test_requests.py).
Запуск тестов осуществляется из родительской директории командой `pytest`.
В общей сложности реализовано 11 тестов (6 для валидных форм и 5 невалидных форм: проверена валидация данных, соответствия полей и их типов).

## Запуск Docker-контейнера
В родительской директории сборка и запуск docker-контейнера осуществляется командой `docker-compose -f docker-compose.yaml up -d`.

## Структура проекта
```
EKom_Test_Task                              # родительская директория приложения/у вас может быть другое название
├─ src/                                     # корневая директория приложения                           
│  ├─ __init__.py                           
│  ├─ main.py                               # корень проекта, точка запуска приложения
│  ├─ db_connetion.py                       # подключение MongoDB
│  ├─ config.py                             # переменные env
│  ├─ routers/                              # руты по ендпоинту /get_form
│  │  ├─ __init__.py                        
│  │  ├─ get_form_route.py                  # /get_form рут 
│  ├─ forms_templates/                      # формы шаблонов для запуска БД
│  │  ├─ __init__.py                                                   
│  │  ├─ start_up_templates.py              # файл с тестовой базой, содержащей шаблоны форм
│  ├─ db_models/                            # python-package с моделями БД
│  │  ├─ __init__.py                                                   
│  │  ├─ form_model.py                      # файл с моделью для добалвения форм шаблона при запуске приложения
│  │  ├─ validators.py                      # файл для валидации входящих данных
├─ tests/                                   # тесты
│  ├─ __init__.py                           
│  ├─ conftest.py                           # конфигурационный файл pytest
│  ├─ test_requests.py                      # тестирование /get_form-запроса с различными параметрами
├─ script_for_auto_requests/                # директория со скриптом для запуска запросов
│  ├─ __init__.py
│  ├─ script.py                             # скрипт для отправки запросов
├─ .env.example                             # пример файла env с переменными среды
├─ pytest.ini                               # pytest конфигурационный файл
├─ requirements.txt                         # необходимые пакеты
├─ .env.docker                              # файла env с переменными среды для запуска docker-контейнера
├─ Dockerfile                               
├─ docker-compose.yaml                      
```
