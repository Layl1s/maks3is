import os
from dotenv import load_dotenv

print("🔍 ЭКСПРЕСС-ДИАГНОСТИКА .env ФАЙЛА")
print("=" * 50)

# 1. Проверяем текущую директорию
current_dir = os.getcwd()
print(f"📁 Текущая директория: {current_dir}")

# 2. Проверяем файлы в директории
files = os.listdir('.')
print(f"📁 Файлы в папке: {files}")

# 3. Проверяем существует ли .env
env_path = os.path.join(current_dir, '.env')
print(f"🔍 Путь к .env: {env_path}")
print(f"✅ Файл .env существует: {os.path.exists(env_path)}")

# 4. Если файл существует - показываем содержимое
if os.path.exists(env_path):
    print("\n📄 СОДЕРЖИМОЕ .env ФАЙЛА:")
    print("=" * 30)
    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    print("=" * 30)
    
    # 5. Пробуем загрузить переменные
    load_dotenv(env_path)
    
    print("\n🔧 ЗАГРУЖЕННЫЕ ПЕРЕМЕННЫЕ:")
    variables = {
        'DB_HOST': os.getenv('DB_HOST'),
        'DB_PORT': os.getenv('DB_PORT'), 
        'DB_NAME': os.getenv('DB_NAME'),
        'DB_USER': os.getenv('DB_USER'),
        'DB_PASSWORD': os.getenv('DB_PASSWORD')
    }
    
    for key, value in variables.items():
        if value:
            print(f"✅ {key}: '{value}'")
        else:
            print(f"❌ {key}: НЕ НАЙДЕН")
else:
    print("\n🚨 ФАЙЛ .env НЕ СУЩЕСТВУЕТ!")
    print("Нужно создать файл .env с настройками базы данных")