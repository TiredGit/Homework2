class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.name} поехала со скоростью {self.speed}!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}!')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


town_car = TownCar(60, "Blue", 'Town Car')
sport_car = SportCar(100, "Black", 'Bugatti')
town_car.go()
town_car.turn('Юг')
town_car.stop()
sport_car.go()
sport_car.turn('Север')
sport_car.stop()
