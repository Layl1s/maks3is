🚀 Руководство по использованию
📋 Содержание
Быстрый старт

Работа с классом Database

Примеры использования

Продвинутые сценарии

Обработка ошибок

Лучшие практики

Интеграция с другими проектами

⚡ Быстрый старт
Минимальный пример
python
from database import Database

# Создание и настройка базы данных
db = Database()
if db.connect():
    db.create_tables()
    db.insert_sample_data()
    
    # Получение данных
    users = db.get_users()
    products = db.get_products()
    
    print(f"Найдено {len(users)} пользователей и {len(products)} товаров")
    db.close()
Стандартный сценарий использования
python
from database import Database

def main():
    print("🚀 Запуск приложения для работы с PostgreSQL")
    
    # Инициализация базы данных
    db = Database()
    
    # Подключение к базе данных
    if not db.connect():
        print("❌ Не удалось подключиться к базе данных")
        return
    
    try:
        # Создание таблиц
        print("📋 Создание таблиц...")
        if not db.create_tables():
            print("❌ Ошибка создания таблиц")
            return
        
        # Добавление тестовых данных
        print("📊 Добавление тестовых данных...")
        if not db.insert_sample_data():
            print("❌ Ошибка добавления данных")
            return
        
        # Работа с данными
        print("\n👥 Список пользователей:")
        users = db.get_users()
        for user in users:
            print(f"  - {user['full_name']} ({user['email']})")
        
        print("\n🛍️ Список товаров:")
        products = db.get_products()
        for product in products:
            print(f"  - {product['name']}: ${product['price']} - {product['category']}")
        
        # Статистика
        print(f"\n📈 Статистика:")
        print(f"  Пользователей: {len(users)}")
        print(f"  Товаров: {len(products)}")
        
        print(f"\n🎉 Приложение успешно завершило работу!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
    finally:
        # Всегда закрываем соединение
        db.close()

if __name__ == "__main__":
    main()
🗄️ Работа с классом Database
Инициализация и подключение
python
from database import Database

# Создание экземпляра базы данных
db = Database()

# Подключение к базе данных
if db.connect():
    print("✅ Подключение успешно")
    # Дальнейшие операции...
else:
    print("❌ Ошибка подключения")
Создание таблиц
python
# Создание таблиц users и products
if db.create_tables():
    print("✅ Таблицы созданы успешно")
else:
    print("❌ Ошибка создания таблиц")
Добавление тестовых данных
python
# Добавление предустановленных данных
if db.insert_sample_data():
    print("✅ Тестовые данные добавлены")
else:
    print("❌ Ошибка добавления данных")
Получение данных
python
# Получение всех пользователей
users = db.get_users()
for user in users:
    print(f"ID: {user['id']}, Имя: {user['full_name']}, Email: {user['email']}")

# Получение всех товаров (отсортированных по цене)
products = db.get_products()
for product in products:
    print(f"ID: {product['id']}, Название: {product['name']}, Цена: ${product['price']}")
Закрытие соединения
python
# Всегда закрывайте соединение после использования
db.close()
print("🔌 Соединение закрыто")
💡 Примеры использования
Пример 1: Простая CRM система
python
from database import Database

class SimpleCRM:
    def __init__(self):
        self.db = Database()
        
    def initialize(self):
        """Инициализация CRM системы"""
        if not self.db.connect():
            return False
        
        if not self.db.create_tables():
            return False
            
        if not self.db.insert_sample_data():
            return False
            
        return True
    
    def show_users(self):
        """Показать всех пользователей"""
        users = self.db.get_users()
        print("\n📋 Список клиентов:")
        for user in users:
            print(f"  👤 {user['full_name']}")
            print(f"     📧 {user['email']}")
            print(f"     🆔 {user['username']}")
            print()
    
    def show_products(self):
        """Показать все товары"""
        products = self.db.get_products()
        print("\n🛍️ Каталог товаров:")
        for product in products:
            print(f"  📦 {product['name']}")
            print(f"     💰 ${product['price']}")
            print(f"     🏷️  {product['category']}")
            if product['description']:
                print(f"     📝 {product['description']}")
            print()
    
    def get_statistics(self):
        """Получить статистику"""
        users = self.db.get_users()
        products = self.db.get_products()
        
        print("\n📊 Статистика системы:")
        print(f"  👥 Количество клиентов: {len(users)}")
        print(f"  🛍️ Количество товаров: {len(products)}")
        
        # Анализ товаров по категориям
        categories = {}
        for product in products:
            category = product['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(product)
        
        print(f"  🏷️  Категории товаров: {len(categories)}")
        for category, items in categories.items():
            print(f"     • {category}: {len(items)} товаров")
    
    def close(self):
        """Закрытие соединения"""
        self.db.close()

# Использование CRM системы
crm = SimpleCRM()
if crm.initialize():
    crm.show_users()
    crm.show_products()
    crm.get_statistics()
    crm.close()
Пример 2: Инвентаризация товаров
python
from database import Database
from decimal import Decimal

class InventoryManager:
    def __init__(self):
        self.db = Database()
        
    def start(self):
        """Запуск менеджера инвентаризации"""
        if not self.db.connect():
            return False
        return True
    
    def add_product(self, name, description, price, category):
        """Добавление нового товара"""
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(
                "INSERT INTO products (name, description, price, category) VALUES (%s, %s, %s, %s)",
                (name, description, price, category)
            )
            self.db.connection.commit()
            cursor.close()
            print(f"✅ Товар '{name}' успешно добавлен")
            return True
        except Exception as e:
            print(f"❌ Ошибка добавления товара: {e}")
            return False
    
    def update_product_price(self, product_id, new_price):
        """Обновление цены товара"""
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(
                "UPDATE products SET price = %s WHERE id = %s",
                (new_price, product_id)
            )
            self.db.connection.commit()
            cursor.close()
            print(f"✅ Цена товара ID:{product_id} обновлена до ${new_price}")
            return True
        except Exception as e:
            print(f"❌ Ошибка обновления цены: {e}")
            return False
    
    def get_products_by_category(self, category):
        """Получить товары по категории"""
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(
                "SELECT * FROM products WHERE category = %s ORDER BY price DESC",
                (category,)
            )
            products = cursor.fetchall()
            cursor.close()
            return products
        except Exception as e:
            print(f"❌ Ошибка получения товаров: {e}")
            return []
    
    def get_total_inventory_value(self):
        """Рассчитать общую стоимость инвентаря"""
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT SUM(price) as total_value FROM products")
            result = cursor.fetchone()
            cursor.close()
            return result['total_value'] or Decimal('0')
        except Exception as e:
            print(f"❌ Ошибка расчета стоимости: {e}")
            return Decimal('0')
    
    def close(self):
        """Закрытие соединения"""
        self.db.close()
