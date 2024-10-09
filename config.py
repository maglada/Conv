import os

class Config:
    """Основні конфігурації для веб-додатку."""
    SECRET_KEY = os.getenv('SECRET_KEY', '9870a123098')  # Секретний ключ для flash-повідомлень
    CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY', 'e72867dc1c15a016e8b25ad0bff5d039')  # Ваш API ключ для курсу валют
    CURRENCY_API_URL = 'http://data.fixer.io/api/latest'

# Вибір конфігурації для використання
config = Config()

