from database import Database

def main():
    db = Database()
    
    # Создаем таблицы
    db.create_tables()
    
    # Добавляем тестовые данные
    db.insert_sample_data()
    
    # Показываем пользователей
    print("\n📋 Список пользователей:")
    users = db.get_users()
    for user in users:
        print(f"ID: {user[0]}, Имя: {user[1]}, Email: {user[2]}")
    
    # Закрываем соединение
    db.close()

if __name__ == "__main__":
    main()
    from database import Database

def main():
    print("🚀 Запуск приложения для работы с PostgreSQL")
    print("=" * 50)
    
    # Создаем экземпляр базы данных
    db = Database()
    
    # Подключаемся к базе данных
    if not db.connect():
        print("❌ Не удалось подключиться к базе данных")
        print("Проверьте:")
        print("1. Запущен ли PostgreSQL")
        print("2. Правильный ли пароль в файле .env")
        print("3. Существует ли база данных 'myapp_database'")
        return
    
    try:
        # Создаем таблицы
        print("📋 Создание таблиц...")
        if not db.create_tables():
            return
        
        # Добавляем тестовые данные
        print("📊 Добавление тестовых данных...")
        if not db.insert_sample_data():
            return
        
        # Получаем и показываем пользователей
        print("\n👥 Список пользователей:")
        users = db.get_users()
        for user in users:
            print(f"  - {user['full_name']} ({user['email']})")
        
        # Получаем и показываем продукты
        print("\n🛍️ Список продуктов:")
        products = db.get_products()
        for product in products:
            print(f"  - {product['name']}: ${product['price']} - {product['category']}")
        
        # Статистика
        print(f"\n📈 Статистика:")
        print(f"  Пользователей: {len(users)}")
        print(f"  Продуктов: {len(products)}")
        
        print(f"\n🎉 Приложение успешно завершило работу!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
    finally:
        # Всегда закрываем соединение
        db.close()

if __name__ == "__main__":
    main()