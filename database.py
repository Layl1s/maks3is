import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        """Подключение к PostgreSQL"""
        try:
            self.connection = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                cursor_factory=RealDictCursor
            )
            print("✅ Успешное подключение к PostgreSQL!")
            return True
        except Exception as e:
            print(f"❌ Ошибка подключения: {e}")
            return False
    
    def create_tables(self):
        """Создание таблиц в базе данных"""
        commands = [
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                full_name VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                price DECIMAL(10,2) NOT NULL,
                category VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]
        
        try:
            cursor = self.connection.cursor()
            for command in commands:
                cursor.execute(command)
            self.connection.commit()
            cursor.close()
            print("✅ Таблицы созданы успешно!")
            return True
        except Exception as e:
            print(f"❌ Ошибка создания таблиц: {e}")
            return False
    
    def insert_sample_data(self):
        """Добавление тестовых данных"""
        try:
            cursor = self.connection.cursor()
            
            # Пользователи
            users_data = [
                ('john_doe', 'john@example.com', 'John Doe'),
                ('jane_smith', 'jane@example.com', 'Jane Smith')
            ]
            
            for user in users_data:
                cursor.execute(
                    "INSERT INTO users (username, email, full_name) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING",
                    user
                )
            
            # Продукты
            products_data = [
                ('Laptop', 'Gaming laptop 16GB RAM', 1500.00, 'Electronics'),
                ('Mouse', 'Wireless mouse', 25.99, 'Accessories')
            ]
            
            for product in products_data:
                cursor.execute(
                    "INSERT INTO products (name, description, price, category) VALUES (%s, %s, %s, %s)",
                    product
                )
            
            self.connection.commit()
            cursor.close()
            print("✅ Тестовые данные добавлены!")
            return True
        except Exception as e:
            print(f"❌ Ошибка вставки данных: {e}")
            return False
    
    def get_users(self):
        """Получение всех пользователей"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
            users = cursor.fetchall()
            cursor.close()
            return users
        except Exception as e:
            print(f"❌ Ошибка получения пользователей: {e}")
            return []
    
    def get_products(self):
        """Получение всех продуктов"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM products ORDER BY price DESC")
            products = cursor.fetchall()
            cursor.close()
            return products
        except Exception as e:
            print(f"❌ Ошибка получения продуктов: {e}")
            return []
    
    def close(self):
        """Закрытие соединения"""
        if self.connection:
            self.connection.close()
            print("🔌 Соединение с базой данных закрыто")

# Тестовый код
if __name__ == "__main__":
    print("🧪 Тестирование database.py")
    db = Database()
    if db.connect():
        db.create_tables()
        db.insert_sample_data()
        db.close()