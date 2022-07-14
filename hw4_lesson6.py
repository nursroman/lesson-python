class car:
    show_speed = None
    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'машина {self.name} поехала')
    def stop(self):
        print(f'машина {self.name} остановилас')
    def turn_right(self):
        return (f'{self.name} повернул направо')
    def turn_left(self):
        return (f'{self.name} повернул налево')
    def police (self):
        if self.is_police == 'да':
            print(f'{self.name} Вы на службе')
        else:
            print(f'{self.name} Вы гражданский')

class TownCar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name,is_police)

    def run (self):
        if self.speed > 40:
            print(f'{self.name} Вы привышаете скорость')
        else:
            print(f'{self.name} , Ваша скороть допустимая для езды в городе')

class SportCar(car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


Maserati = SportCar(350,'black', 'Ghibli', 'да')
toyota = TownCar(220, 'white', 'Camry', 'нет')
toyota.go()
toyota.run()
Maserati.police()
toyota.police()



