from models.order import *
import datetime

order_1 = Order("Loid Forge", datetime.date(2024,2,12), 3, "George Ezra", "Wanted On Voyage")
order_2 = Order("Tim McIlrath", datetime.date(2024,2,14), 10, "Rise Against", "The Sufferer & The Witness")
order_3 = Order("Mark Jacobs", datetime.date(2024,2,17), 5, "Falling In Reverse", "The Drug In Me Is You")
order_4 = Order("Dave Grohl", datetime.date(2023,12,25), 1, "Foo Fighters", "The Colour and the Shape")

orders = [order_1, order_2, order_3, order_4]