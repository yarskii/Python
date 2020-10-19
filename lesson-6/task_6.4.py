class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police is True:
            print(f'Автомобиль {self.name} является полицейским')

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_lef(self):
        print(f'{self.name} повернула налево')

    def turn_right(self):
        print(f'{self.name} повернула на право')

    def show_speed(self):
        print(f'{self.speed} км/ч текущая скорость владельца {self.name}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        if self.is_police is False:
            print(f'Автомобиль {self.name} является городским')
        print(f'Цвет автомобиля {self.name}: {self.color}')
        if self.speed > 60:
            print(f'Владелец {self.name} привысил скорость')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        if self.is_police is False:
            print(f'Автомобиль {self.name} является рабочим')
        print(f'Цвет автомобиля {self.name}: {self.color}')
        if self.speed > 40:
            print(f'Владелец {self.name} привысил скорость')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        if self.is_police is False:
            print(f'Автомобиль {self.name} является спортивным')
        print(f'Цвет автомобиля {self.name}: {self.color}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        print(f'Цвет автомобиля {self.name}: {self.color}')


# a = Car(100, 'blue', 'Mazda', False)
b = TownCar(60, 'black', 'Opel', True)
c = PoliceCar(120, 'red', 'Ford')
d = WorkCar(41, 'orange', 'Kia', False)
e = SportCar(300, 'green', 'Porsche', False)
# a.go()
# a.stop()
# a.turn_lef()
# a.turn_right()
# a.show_speed()
b.show_speed()
c.show_speed()
d.show_speed()
e.show_speed()
