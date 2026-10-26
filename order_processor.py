from abc import ABC, abstractmethod

# Базовый класс скидки (открыт для расширения, закрыт для модификации)
class Discount(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class SeasonalDiscount(Discount):
    """
    Класс для расчета сезонной скидки.
    Применяет скидку 10% к стоимости заказа.
    """
    def apply(self, price):
        return price * 0.9 # Сезонная скидка 10%
 
class LoyaltyDiscount(Discount):
    def apply(self, price):
        return price * 0.95 # Накопительная скидка 5%

class PromoCodeDiscount(Discount):
    def apply(self, price):
        return max(0, price - 500) # Промокод на 500 рублей

def calculate_total(price, discounts):
    """Применяет список скидок. Новые скидки не требуют изменения этой функции."""
    for discount in discounts:
        price = discount.apply(price)
    return price
