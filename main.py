from database import Database

def main():
    print("🚀 Запуск приложения для работы с PostgreSQL")
    print("=" * 50)
    
    # Создаем экземпляр базы данных
    db = Database()
    
    # Подключаемся к базе данных
    if not db.connect():
        print("❌ Не удалось подключиться к базе данных")
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
        
        print("🎉 Приложение успешно завершило работу!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
    finally:
        # Всегда закрываем соединение
        db.close()

if __name__ == "__main__":
    main()
