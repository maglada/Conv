from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import os
from config import config
from utils.converter import CurrencyConverter


app = Flask(__name__)

converter = CurrencyConverter(config.CURRENCY_API_KEY)
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
        conversion_result = converter.convert(base_currency, target_currency, amount)
        
        if conversion_result is None:
            flash("Error converting currency. Try again later.")
            return redirect(url_for('index'))

        return render_template('index.html', result=conversion_result, base_currency=base_currency, target_currency=target_currency, amount=amount)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

