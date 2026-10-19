# order_processor.py — исходная версия (из ПЗ №1)
total_price = 0.0  # глобальная переменная (её уберём в Задании 3)

def process_order(items):
    global total_price
    total_price = sum(item["price"] * item["quantity"] for item in items)
    return total_price
