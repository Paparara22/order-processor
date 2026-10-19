# order_processor.py - версия после рефакторинга

def process_order(items):
    # Убрали глобальную переменную, теперь total_price локальная
    total_price = sum(item["price"] * item["quantity"] for item in items)
    return total_price
