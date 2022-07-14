class Road:
    __length = None
    __width = None
    __weigth = None
    __tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        self.weigth = 30
        self.tickness = 0.05
        mass = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'необходимо {mass} тонн для строительства')

a = Road(30000, 20)
a.mass()


