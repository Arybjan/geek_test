# geek_test

Простой REST API для управления задачами на Django REST Framework.

Стек
```
- Python
- Django
- Django REST Framework
- django-environ
- PostgreSQL / SQLite
```
Возможности
```
- создание задачи
- получение списка задач
- получение одной задачи
- обновление задачи
- удаление задачи
- фильтрация по completed
- поиск по title
- сортировка по дате создания
```
Запуск проекта
1. Клонирование
``` bash
git clone https://github.com/Arybjan/geek_test.git
cd geek_test
```

2. Установка зависимостей
``` bash
poetry install
```
3. Создание .env
``` .env
SECRET_KEY=django-insecure-test-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```
4. Миграции
``` python
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
5. Запуск
``` python
poetry run python manage.py runserver
```
API
Список задач
GET /api/task/
<img width="1392" height="912" alt="Снимок экрана 2026-03-21 в 18 04 07" src="https://github.com/user-attachments/assets/695d45f6-2d64-49f1-b2d4-2a108899a7db" />

Создать задачу
POST /api/task/
<img width="1392" height="912" alt="Снимок экрана 2026-03-21 в 18 03 51" src="https://github.com/user-attachments/assets/a94c7c95-d1bc-4ea2-b14f-d26df4052ccb" />

Пример body:
``` json
{
  "title": "Сделать тестовое",
  "description": "Доделать Django API",
  "completed": false
}
```

Получить одну задачу
GET /api/task/1/

Обновить задачу
PATCH /api/task/1/

Удалить задачу
DELETE /api/task/1/

Фильтрация и поиск
Только выполненные
GET /api/task/?completed=true

Поиск по названию
GET /api/task/?search=тест

Сортировка
GET /api/task/?ordering=-created_at
