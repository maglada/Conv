import os

class Config:
    """Основні конфігурації для веб-додатку."""
    SECRET_KEY = os.getenv('SECRET_KEY', '9870a123098')  # Секретний ключ для flash-повідомлень
    CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY', 'fca_live_thxhbygMLzChMIcTf174RzB7OVmeqstApElldkvD')  # Ваш API ключ для курсу валют
    CURRENCY_API_URL = 'https://api.freecurrencyapi.com/v1/latest'

# Вибір конфігурації для використання
config = Config()

