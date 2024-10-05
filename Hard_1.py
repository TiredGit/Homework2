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
        return Toy(self.name, self.color, self.toy_type)

class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f'Игрушка: {self.name}, Цвет: {self.color}, Тип игрушки: {self.toy_type}'


new_toy = Factory('Crocodile', 'Green', 'Animal').create_toy()
print(new_toy)
