from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import os
from config import config

app = Flask(__name__)

app.config.from_object(config)

# Головна сторінка
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        base_currency = request.form['base_currency']
        target_currency = request.form['target_currency']
        amount = request.form['amount']
        
        if not amount.isdigit():
            flash("Please enter a valid number for amount")
            return redirect(url_for('index'))
        
        amount = float(amount)
        conversion_result = convert_currency(base_currency, target_currency, amount)
        
        if conversion_result is None:
            flash("Error converting currency. Try again later.")
            return redirect(url_for('index'))

        return render_template('index.html', result=conversion_result, base_currency=base_currency, target_currency=target_currency, amount=amount)

    return render_template('index.html')

# Логіка конвертації
def convert_currency(base, target, amount):
    try:
        response = requests.get(f"{API_URL}&base={base}&symbols={target}")
        data = response.json()
        if data['success']:
            rate = data['rates'][target]
            return round(amount * rate, 2)
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)

