class Factory:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def buy_res(self):
        print(f'Закупка сырья')

    def sewing(self):
        print(f'Пошив')

    def coloring(self):
        print(f'Окраска')

    def create_toy(self):
        print('Создание игрушки:')
        self.buy_res()
        self.sewing()
        self.coloring()
        print('Игрушка создана')
        if self.toy_type == 'Animal':
            return AnimalToy(self.name, self.color)
        if self.toy_type == 'Cartoon':
            return CartoonToy(self.name, self.color)


class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = 'Animal'

    def __str__(self):
        return f'Игрушка: {self.name}, Цвет: {self.color}, Тип игрушки: {self.toy_type}'


class CartoonToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = 'Cartoon'

    def __str__(self):
        return f'Игрушка: {self.name}, Цвет: {self.color}, Тип игрушки: {self.toy_type}'


new_toy1 = Factory('Crocodile', 'Green', 'Animal').create_toy()
print(new_toy1)
new_toy2 = Factory('Miki Mouse', 'Black', 'Cartoon').create_toy()
print(new_toy2)
