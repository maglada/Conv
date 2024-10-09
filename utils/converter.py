import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"

    def convert(self, base, target, amount):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            if response.status_code == 200 and base in data['data'] and target in data['data']:
                rate = data['data'][target] / data['data'][base]  # Отримуємо курс з базової валюти до цільової
                return round(amount * rate, 2)
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

