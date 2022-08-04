class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * j'

    def __add__(self, other):
        return f'с = {self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        return f'с = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * j'

    def __str__(self):
        return f'с = {self.a} + {self.b} * j'


с1 = ComplexNumber(5, -7)
с2 = ComplexNumber(11, 8)
print(с1)
print(с1 + с2)
print(с1 * с2)
