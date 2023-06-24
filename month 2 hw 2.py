class Figure:
    unit = 'cm'

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * self.__radius ** 2

    def info(self):
        print(f'Circle radius: {self.__radius} {Figure.unit}, area: {self.calculate_area()} {Figure.unit}^2')

class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return self.__side_a * self.__side_b / 2

    def info(self):
        print(f'Right Triangle side_a: {self.__side_a} {Figure.unit}, '
              f'side_b: {self.__side_b} {Figure.unit}, area: {self.calculate_area()} {Figure.unit}^2')

cr = Circle(5)
print(cr.calculate_area())
cr.info()

tr = RightTriangle(5, 6)
print(tr.calculate_area())
tr.info()