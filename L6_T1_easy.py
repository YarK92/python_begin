# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class TownCar:
    def __init__(self, speed, color, hatchback, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.hatchback = hatchback
        self.is_police = False

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self):
        print('Машина повернула.')


class SportCar:
    def __init__(self, speed, color, sport_car, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.sport_car = sport_car
        self.is_police = False

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self):
        print('Машина повернула.')


class WorkCar:
    def __init__(self, speed, color, work_car, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.work_car = work_car
        self.is_police = False

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self):
        print('Машина повернула.')


class PoliceCar:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self):
        print('Машина повернула.')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car:
    def __init__(self, speed, color, name, type_car=None, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.type_car = type_car
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self):
        print('Машина повернула.')

class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, 'hatchback', is_police=False)

class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, 'sport_car', is_police=False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, 'work_car', is_police=False)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, 'police_car', is_police=True)



