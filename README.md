# Сервис DRF для внедрения результата тестов
DRF project with API to send results in DB

## Установка и запуск
1. Склонировать репозиторий с Github
2. Перейти в директорию проекта
3. Запустить команду 
```
pip install poetry
```
4. Запустить команду
```
poetry install
```
5. Запустить 
```
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py runserver
```

***
Маршруты API
```http://127.0.0.1:8000/api/v1/login/ ```- GET запрос без параметров для получение уникального логина
```http://127.0.0.1:8000/api/v1/iq_post/ ```- POST запрос с данными score и login_f для внесения данных IQ теста
```http://127.0.0.1:8000/api/v1/eq_post/ ```- POST запрос с данными result и login_f для внесения данных EQ теста
```http://127.0.0.1:8000/api/v1/get_test/ ```- POST запрос с данными login для получения информации о пройденных тестах и их времени.