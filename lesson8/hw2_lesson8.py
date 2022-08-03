class DivisionByNull:
    def __init__(self, delitel, znaminatel):
        self.delitel = delitel
        self.znaminatel = znaminatel

    @staticmethod
    def divide_by_null(delitel, znaminatel):
        try:
            return (delitel / znaminatel)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))