"""
Создание класса Корзина
"""

from goods import Goods


class Basket:
    def __init__(self, goods, count):
        self.goods = goods
        self.count = count

    def __str__(self):
        # % f является заполнителем для десятичного типа
        return '%s: %.2f * %s' % (self.goods.name,
                                     self.goods.price, self.count)


    def amout(self): # Рассчитать подытог продукта
        return self.goods.price * self.count


if __name__ == '__main__':
    goods1 = Goods(1,'Молоко',145.50,'гр.',950,1)
    goods2 = Goods(3, 'Икра лососовая', 319.99, 'гр.',95, 3)
    # Создайте объект продукта корзины покупок, вам нужно передать объект продукта
    item1 = Basket(goods1, 2)
    item2 = Basket(goods2, 2)
    money = item1.amout()
    print(item1,'Итого', money)