from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def index():
    return render_template('index.html', title = "Home Page")

@app.route('/orders')
def order_list():
    return render_template('orders.html', title = "Orders", orders = orders)
