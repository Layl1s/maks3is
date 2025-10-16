import psycopg2
import os
from dotenv import load_dotenv

print("🧪 ТЕСТИРОВАНИЕ ПОДКЛЮЧЕНИЯ С .env")
print("=" * 50)

# Загружаем .env
load_dotenv()

# Получаем параметры
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

print("🔧 Параметры из .env:")
print(f"  Host: {host}")
print(f"  Port: {port}")
print(f"  Database: {database}")
print(f"  User: {user}")
print(f"  Password: {'*' * len(password) if password else 'НЕТ'}")

try:
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    print("\n✅ ПОДКЛЮЧЕНИЕ УСПЕШНО!")
    
    # Проверяем версию PostgreSQL
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"📋 Версия PostgreSQL: {version[0]}")
    
    # Проверяем существование базы данных
    cursor.execute("SELECT datname FROM pg_database WHERE datname = %s;", (database,))
    db_exists = cursor.fetchone()
    
    if db_exists:
        print(f"✅ База данных '{database}' существует")
    else:
        print(f"❌ База данных '{database}' не существует")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ ОШИБКА ПОДКЛЮЧЕНИЯ: {e}")
    print("\n🔧 Возможные решения:")
    print("1. Проверьте что PostgreSQL запущен")
    print("2. Убедитесь что база данных существует")
    print("3. Проверьте пароль в .env файле")