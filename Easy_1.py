class TownCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')


class SportCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')


class WorkCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')


class PoliceCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')


town_car = TownCar(60, "Blue", 'Town Car')
sport_car = SportCar(100, "Black", 'Bugatti')
town_car.go()
town_car.turn('Юг')
town_car.stop()
sport_car.go()
sport_car.turn('Север')
sport_car.stop()
