import psycopg2
from psycopg2.extras import RealDictCursor

def test_connection_direct():
    print("🧪 Прямое тестирование подключения")
    print("=" * 40)
    
    try:
        # Прямое подключение без .env
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            database="mydatabase",
            user="postgres",
            password="1111",  # ЗАМЕНИТЕ НА РЕАЛЬНЫЙ ПАРОЛЬ
            cursor_factory=RealDictCursor
        )
        
        print("✅ Подключение успешно!")
        
        # Проверим версию PostgreSQL
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"📋 Версия PostgreSQL: {version['version']}")
        
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        print("\nВозможные причины:")
        print("1. Неправильный пароль")
        print("2. PostgreSQL не запущен")
        print("3. База данных не существует")
        print("4. Проблемы с сетью")

if __name__ == "__main__":
    test_connection_direct()