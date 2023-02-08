from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def index():
    return render_template('index.html', title = "Orders", orders = orders)

@app.route('/order/<index_num>')
def single_order(index_num):
    order = orders[int(index_num)]
    return render_template('order.html', title = "Customer Order", order = order)
