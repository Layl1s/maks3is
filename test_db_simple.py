"""
Простое тестирование для database.py с использованием pytest
"""
import pytest
from unittest.mock import Mock, patch
from database import Database


def test_database_initialization():
    """Тест создания объекта базы данных"""
    db = Database()
    assert db.connection is None
    assert hasattr(db, 'connect')
    assert hasattr(db, 'create_tables')


def test_database_connect_success():
    """Тест успешного подключения к базе"""
    with patch('database.psycopg2.connect') as mock_connect:
        mock_connection = Mock()
        mock_connect.return_value = mock_connection
        
        db = Database()
        result = db.connect()
        
        assert result == True
        assert db.connection == mock_connection


def test_database_connect_failure():
    """Тест неудачного подключения"""
    with patch('database.psycopg2.connect') as mock_connect:
        mock_connect.side_effect = Exception("Connection failed")
        
        db = Database()
        result = db.connect()
        
        assert result == False
        assert db.connection is None


def test_create_tables():
    """Тест создания таблиц"""
    with patch('database.Database.connect'):
        db = Database()
        db.connection = Mock()
        db.connection.cursor.return_value = Mock()
        
        result = db.create_tables()
        
        assert result == True


def test_insert_sample_data():
    """Тест добавления тестовых данных"""
    with patch('database.Database.connect'):
        db = Database()
        db.connection = Mock()
        mock_cursor = Mock()
        db.connection.cursor.return_value = mock_cursor
        
        result = db.insert_sample_data()
        
        assert result == True
        assert mock_cursor.execute.call_count == 4


def test_get_users():
    """Тест получения пользователей"""
    with patch('database.Database.connect'):
        db = Database()
        db.connection = Mock()
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [
            {'id': 1, 'username': 'test', 'email': 'test@test.com'}
        ]
        db.connection.cursor.return_value = mock_cursor
        
        users = db.get_users()
        
        assert len(users) == 1
        assert users[0]['username'] == 'test'


def test_get_products():
    """Тест получения продуктов"""
    with patch('database.Database.connect'):
        db = Database()
        db.connection = Mock()
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [
            {'id': 1, 'name': 'Laptop', 'price': 1500.00}
        ]
        db.connection.cursor.return_value = mock_cursor
        
        products = db.get_products()
        
        assert len(products) == 1
        assert products[0]['name'] == 'Laptop'


def test_close_connection():
    """Тест закрытия соединения"""
    db = Database()
    db.connection = Mock()
    
    db.close()
    
    db.connection.close.assert_called_once()
