import psycopg2
from config import load_config

def connect(config):
    """Подключение к серверу PostgreSQL"""
    try:
        # Устанавливаем соединение
        with psycopg2.connect(**config) as conn:
            print('Подключено к серверу PostgreSQL.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print("Ошибка подключения:", error)

if __name__ == '__main__':
    config = load_config()  # Убедитесь, что эта функция возвращает правильную конфигурацию
    connect(config)         # Вызываем функцию подключения, чтобы установить соединение
