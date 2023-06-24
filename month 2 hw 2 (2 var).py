class Figure:
    unit = 'cm'

    def __init__(self):
        self.__perimeter = 0

    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length
        self.__perimeter = self.calculate_perimeter()

    def calculate_perimeter(self):
        return self.__side_length * 4

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Square side length: {self.__side_length} {Figure.unit}, '
              f'perimeter: {self.__perimeter} {Figure.unit} '
              f'square: {self.calculate_area()} {Figure.unit}^2')


sq = Square(5)
sq.info()