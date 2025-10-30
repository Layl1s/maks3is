напиши документацию для файла api.md на русском
🌐 Документация API
📋 Обзор
API предоставляет RESTful endpoints для управления пользователями и товарами в приложении PostgreSQL. API следует принципам REST и возвращает ответы в формате JSON.

🔗 Базовый URL
text
http://localhost:8000/api/v1
🔐 Аутентификация
Аутентификация по API ключу
Добавьте ваш API ключ в заголовки запроса:

http
X-API-Key: ваш-секретный-api-ключ
Пример с curl:
bash
curl -H "X-API-Key: ваш-секретный-api-ключ" \
  http://localhost:8000/api/v1/users
📊 Формат ответов
Успешный ответ
json
{
  "status": "success",
  "data": { ... },
  "message": "Операция выполнена успешно",
  "timestamp": "2024-01-15T10:30:00Z"
}
Ответ с ошибкой
json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Неверные входные данные",
    "details": { ... }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
👥 Endpoints для пользователей
Получить всех пользователей
Получить список всех пользователей.

http
GET /users
Параметры запроса:

page (необязательный) - номер страницы (по умолчанию: 1)

limit (необязательный) - количество записей на странице (по умолчанию: 10)

search (необязательный) - поиск по имени или email

Пример запроса:

http
GET /users?page=1&limit=5&search=john
Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "users": [
      {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "full_name": "John Doe",
        "created_at": "2024-01-01T10:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 5,
      "total": 15,
      "pages": 3
    }
  }
}
Получить пользователя по ID
Получить информацию о конкретном пользователе.

http
GET /users/{id}
Параметры пути:

id (обязательный) - ID пользователя

Пример запроса:

http
GET /users/1
Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "user": {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com",
      "full_name": "John Doe",
      "created_at": "2024-01-01T10:00:00Z"
    }
  }
}
Ошибки:

404 Not Found - пользователь не найден

Создать пользователя
Создать нового пользователя.

http
POST /users
Тело запроса:

json
{
  "username": "new_user",
  "email": "new@example.com",
  "full_name": "Новый Пользователь"
}
Валидация:

username - обязательно, уникально, 3-50 символов

email - обязательно, валидный email, уникально

full_name - необязательно, максимум 100 символов

Пример запроса:

http
POST /users
Content-Type: application/json

{
  "username": "alex_ivanov",
  "email": "alex@example.com",
  "full_name": "Алексей Иванов"
}
Успешный ответ (201):

json
{
  "status": "success",
  "data": {
    "user": {
      "id": 3,
      "username": "alex_ivanov",
      "email": "alex@example.com",
      "full_name": "Алексей Иванов",
      "created_at": "2024-01-15T10:30:00Z"
    }
  },
  "message": "Пользователь успешно создан"
}
Ошибки:

400 Bad Request - неверные данные

409 Conflict - пользователь с таким username или email уже существует

Обновить пользователя
Обновить информацию о пользователе.

http
PUT /users/{id}
Параметры пути:

id (обязательный) - ID пользователя

Тело запроса:

json
{
  "username": "updated_user",
  "full_name": "Обновленное Имя"
}
Пример запроса:

http
PUT /users/1
Content-Type: application/json

{
  "full_name": "Иван Петров",
  "username": "ivan_petrov"
}
Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "user": {
      "id": 1,
      "username": "ivan_petrov",
      "email": "john@example.com",
      "full_name": "Иван Петров",
      "created_at": "2024-01-01T10:00:00Z"
    }
  },
  "message": "Пользователь успешно обновлен"
}
Удалить пользователя
Удалить пользователя.

http
DELETE /users/{id}
Параметры пути:

id (обязательный) - ID пользователя

Пример запроса:

http
DELETE /users/1
Успешный ответ (200):

json
{
  "status": "success",
  "message": "Пользователь успешно удален"
}
🛍️ Endpoints для товаров
Получить все товары
Получить список всех товаров.

http
GET /products
Параметры запроса:

category (необязательный) - фильтр по категории

min_price (необязательный) - минимальная цена

max_price (необязательный) - максимальная цена

page (необязательный) - номер страницы

limit (необязательный) - количество записей на странице

sort (необязательный) - сортировка (price_asc, price_desc, name)

Пример запроса:

http
GET /products?category=Electronics&min_price=100&max_price=1000&sort=price_asc
Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "products": [
      {
        "id": 1,
        "name": "Ноутбук",
        "description": "Игровой ноутбук 16GB RAM",
        "price": 1500.00,
        "category": "Электроника",
        "created_at": "2024-01-01T10:00:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 25,
      "pages": 3
    }
  }
}
Получить товар по ID
Получить информацию о конкретном товаре.

http
GET /products/{id}
Параметры пути:

id (обязательный) - ID товара

Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "product": {
      "id": 1,
      "name": "Ноутбук",
      "description": "Игровой ноутбук 16GB RAM",
      "price": 1500.00,
      "category": "Электроника",
      "created_at": "2024-01-01T10:00:00Z"
    }
  }
}
Создать товар
Создать новый товар.

http
POST /products
Тело запроса:

json
{
  "name": "Новый товар",
  "description": "Описание товара",
  "price": 99.99,
  "category": "Категория"
}
Валидация:

name - обязательно, 1-100 символов

description - необязательно

price - обязательно, положительное число

category - необязательно, 1-50 символов

Пример запроса:

http
POST /products
Content-Type: application/json

{
  "name": "Смартфон",
  "description": "Флагманский смартфон",
  "price": 799.99,
  "category": "Электроника"
}
Успешный ответ (201):

json
{
  "status": "success",
  "data": {
    "product": {
      "id": 3,
      "name": "Смартфон",
      "description": "Флагманский смартфон",
      "price": 799.99,
      "category": "Электроника",
      "created_at": "2024-01-15T10:30:00Z"
    }
  },
  "message": "Товар успешно создан"
}
Обновить товар
Обновить информацию о товаре.

http
PUT /products/{id}
Параметры пути:

id (обязательный) - ID товара

Тело запроса:

json
{
  "name": "Обновленное название",
  "price": 89.99
}
Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "product": {
      "id": 1,
      "name": "Обновленное название",
      "description": "Игровой ноутбук 16GB RAM",
      "price": 89.99,
      "category": "Электроника",
      "created_at": "2024-01-01T10:00:00Z"
    }
  },
  "message": "Товар успешно обновлен"
}
Удалить товар
Удалить товар.

http
DELETE /products/{id}
Параметры пути:

id (обязательный) - ID товара

Успешный ответ (200):

json
{
  "status": "success",
  "message": "Товар успешно удален"
}
📈 Статистика
Получить статистику
Получить общую статистику системы.

http
GET /stats
Успешный ответ (200):

json
{
  "status": "success",
  "data": {
    "users_count": 15,
    "products_count": 25,
    "categories": [
      {
        "name": "Электроника",
        "count": 10,
        "avg_price": 450.50
      },
      {
        "name": "Аксессуары",
        "count": 5,
        "avg_price": 25.99
      }
    ],
    "total_value": 11250.75
  }
}
🚨 Коды ошибок
Код	Сообщение	Описание
400	BAD_REQUEST	Неверный формат запроса
401	UNAUTHORIZED	Неверный API ключ
403	FORBIDDEN	Доступ запрещен
404	NOT_FOUND	Ресурс не найден
409	CONFLICT	Конфликт данных
422	VALIDATION_ERROR	Ошибка валидации
500	INTERNAL_ERROR	Внутренняя ошибка сервера
💡 Примеры использования
Пример с Python requests:
python
import requests

API_BASE = "http://localhost:8000/api/v1"
API_KEY = "your-secret-api-key"

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

# Получить всех пользователей
response = requests.get(f"{API_BASE}/users", headers=headers)
users = response.json()

