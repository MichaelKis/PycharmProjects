"""
Создание класса Категории товаров
"""
from goods import Goods




class Category():

    def __init__(self, category: int, name: str, goods):
        if not isinstance(category, int):
            raise TypeError('Не верный тип данных для Кода Категории товара')
        self.category = category
        if not isinstance(name, str):
            raise TypeError('Не верный тип данных для Названия Категории товара')
        self.name = name
        self.goods = goods


    def display_product(self):
        print('Категория товара: {}, Название категории товара: {}'.format(self.category, self.name))


if __name__ == '__main__':

    # Создаем 3 категории товаров

    print(100 * '*')
    category1 = Category(1, 'Молочные продукты')
    Category.display_product(category1)
    category2 = Category(2, 'Рыба и морепродукты')
    Category.display_product(category2)
    category3 = Category(3, 'Фрукты и овощи')
    Category.display_product(category3)



    # Создаем 5 товаров

    print(100 * '*')
    goods = Goods(1, 'Молоко', 145.50, 'гр.', 950, 1)
    Goods.display_product(goods)
    goods1 = Goods(2, 'Масло сливочное', 169.89, 'гр.', 250, 2)
    Goods.display_product(goods1)
    goods2 = Goods(3, 'Икра лососовая', 319.99, 'гр.', 95, 3)
    Goods.display_product(goods2)
    goods3 = Goods(4, 'Колбаса вареная', 159.99, 'гр.', 1000, 4)
    Goods.display_product(goods3)
    goods4 = Goods(5, 'Картофель', 49.89, 'кг.', 1, 5)
    Goods.display_product(goods4)


    # # Связываем категории товаров с продуктами
    # item = Category(goods,)
    # print(item.name, item.category)
