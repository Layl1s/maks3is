⚙️ Руководство по установке и настройке
📋 Содержание
Предварительные требования

Установка Python

Установка PostgreSQL

Настройка проекта

Настройка базы данных

Запуск приложения

Настройка окружения разработки

Устранение неполадок

🎯 Предварительные требования
Минимальные системные требования
ОС: Windows 10/11, macOS 10.14+, Ubuntu 18.04+

Память: 4 GB RAM

Место на диске: 2 GB свободного места

Необходимое программное обеспечение
Python 3.8+

PostgreSQL 12+

Git (для клонирования репозитория)

Pip (менеджер пакетов Python)

🐍 Установка Python
Проверка установленной версии Python
bash
python --version
# или
python3 --version
Установка на Windows
Скачайте Python с официального сайта

Запустите установщик

ВАЖНО: Отметьте галочку "Add Python to PATH"

Выберите "Install Now"

Проверьте установку:

cmd
python --version
pip --version
Установка на macOS
bash
# Через Homebrew
brew install python

# Или скачайте с официального сайта
Установка на Linux (Ubuntu/Debian)
bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
🐘 Установка PostgreSQL
Установка на Windows
Скачайте установщик с официального сайта

Запустите установщик

Запомните пароль для пользователя postgres

Оставьте порт по умолчанию (5432)

Завершите установку

Установка на macOS
bash
# Через Homebrew
brew install postgresql
brew services start postgresql

# Или через Postgres.app
Установка на Linux (Ubuntu/Debian)
bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
Проверка установки PostgreSQL
bash
psql --version
📥 Настройка проекта
1. Клонирование репозитория
bash
git clone https://github.com/your-username/maks3is.git
cd maks3is
2. Создание виртуального окружения
bash
# Создание виртуального окружения
python -m venv venv

# Активация на Windows
venv\Scripts\activate

# Активация на macOS/Linux
source venv/bin/activate
Примечание: Виртуальное окружение должно быть активировано для всех последующих команд.

3. Установка зависимостей
bash
pip install -r requirements.txt
4. Проверка установки
bash
python -c "import psycopg2; print('✅ psycopg2 установлен')"
python -c "from dotenv import load_dotenv; print('✅ python-dotenv установлен')"
🗄️ Настройка базы данных
1. Подключение к PostgreSQL
bash
# Windows
psql -U postgres

# Linux/macOS
sudo -u postgres psql
2. Создание базы данных
sql
CREATE DATABASE myapp_database;
3. Создание пользователя (опционально)
sql
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE myapp_database TO myuser;
\q
4. Настройка переменных окружения
Создайте файл .env в корне проекта:

env
# Настройки базы данных PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp_database
DB_USER=postgres
DB_PASSWORD=your_password_here

# Дополнительные настройки
DB_SSLMODE=prefer
DB_CONNECTION_TIMEOUT=30
DEBUG=True
ВАЖНО: Никогда не коммитьте файл .env в Git!

5. Настройка .gitignore
Убедитесь, что в файле .gitignore есть следующие строки:

text
.env
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
🚀 Запуск приложения
1. Проверка подключения к базе данных
bash
python -c "
from database import Database
db = Database()
if db.connect():
    print('✅ Подключение к БД успешно')
    db.close()
else:
    print('❌ Ошибка подключения к БД')
"
2. Создание таблиц
bash
python -c "
from database import Database
db = Database()
if db.connect():
    if db.create_tables():
        print('✅ Таблицы созданы успешно')
    db.close()
"
3. Запуск основного приложения
bash
python main.py
Ожидаемый вывод:
text
🚀 Запуск приложения для работы с PostgreSQL
==================================================
✅ Успешное подключение к PostgreSQL!
📋 Создание таблиц...
✅ Таблицы созданы успешно!
📊 Добавление тестовых данных...
✅ Тестовые данные добавлены!

👥 Список пользователей:
  - John Doe (john@example.com)
  - Jane Smith (jane@example.com)

🛍️ Список продуктов:
  - Laptop: $1500.00 - Electronics
  - Mouse: $25.99 - Accessories

📈 Статистика:
  Пользователей: 2
  Продуктов: 2

🎉 Приложение успешно завершило работу!
🔌 Соединение с базой данных закрыто
🧪 Тестирование
Запуск тестов
bash
# Установка pytest (если не установлен)
pip install pytest

# Запуск всех тестов
python -m pytest

# Запуск с подробным выводом
python -m pytest -v

# Запуск конкретного тестового файла
python -m pytest test_database.py -v

# Запуск с покрытием кода
pip install pytest-cov
python -m pytest --cov=database --cov-report=html
🔧 Настройка окружения разработки
Настройка VS Code
Создайте файл .vscode/settings.json:

json
{
    "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true,
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/*.pyc": true
    }
}
Настройка PyCharm
Откройте настройки (File → Settings)

Перейдите в Project → Python Interpreter

Выберите интерпретатор из папки venv

Установите пути к исходному коду

Полезные инструменты разработки
bash
# Установка дополнительных инструментов
pip install black flake8 mypy

# Форматирование кода
black database.py main.py

# Проверка стиля кода
flake8 database.py

# Статическая типизация
mypy database.py
🐛 Устранение неполадок
Ошибка подключения к PostgreSQL
Симптомы: psycopg2.OperationalError: connection to server failed

Решение:

Проверьте, запущен ли сервер PostgreSQL:

bash
# Windows
services.msc  # Ищите "PostgreSQL"

# Linux
sudo systemctl status postgresql

# macOS
brew services list
Проверьте правильность параметров в .env

Проверьте, существует ли база данных:

sql
\l  # Список баз данных
Ошибка аутентификации
Симптомы: password authentication failed for user "postgres"

Решение:

Проверьте пароль в файле .env

Сбросьте пароль PostgreSQL:

sql
ALTER USER postgres WITH PASSWORD 'new_password';
Ошибка импорта модулей
Симптомы: ModuleNotFoundError: No module named 'psycopg2'

Решение:

Активируйте виртуальное окружение

Переустановите зависимости:

bash
pip install -r requirements.txt
Ошибка прав доступа
Симптомы: permission denied for database

Решение:

sql
GRANT ALL PRIVILEGES ON DATABASE myapp_database TO postgres;
📊 Проверка работоспособности
Полный сценарий проверки
bash
# 1. Активация окружения
source venv/bin/activate  # или venv\Scripts\activate на Windows

# 2. Проверка зависимостей
python -c "import psycopg2; print('✅ psycopg2')"
python -c "import pytest; print('✅ pytest')"

# 3. Проверка подключения к БД
python -c "
from database import Database
db = Database()
if db.connect():
    print('✅ БД подключена')
    if db.create_tables():
        print('✅ Таблицы созданы')
    db.close()
"

# 4. Запуск тестов
python -m pytest test_database.py -v

# 5. Запуск приложения
python main.py
🔄 Обновление проекта
Получение последних изменений
bash
git pull origin main
pip install -r requirements.txt
Обновление зависимостей
bash
pip freeze > requirements.txt
📞 Получение помощи
Если у вас возникли проблемы с установкой:

Проверьте логи: Ищите сообщения об ошибках в консоли

Сверьте версии: Убедитесь, что версии Python и PostgreSQL совместимы

Проверьте настройки: Убедитесь, что файл .env настроен правильно

Посмотрите документацию: Изучите docs/ директорию

Полезные команды для диагностики
bash
# Проверка версий
python --version
psql --version

# Проверка установленных пакетов
pip list

# Проверка активности сервисов
# Windows
netstat -an | findstr 5432

# Linux
sudo netstat -tulpn | grep 5432

# Проверка базы данных
psql -U postgres -c "\l"
✅ Установка завершена! Теперь вы можете использовать приложение для работы с PostgreSQL базой данных.
