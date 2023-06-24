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


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.__perimeter = self.calculate_perimeter()


    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * self.__length + 2 * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length} {Figure.unit} '
              f'width: {self.__width} {Figure.unit} '
              f'perimeter: {self.__perimeter} {Figure.unit} '
              f'area: {self.calculate_area()} {Figure.unit}^2')
sq = Square(5)
sq.info()

rc = Rectangle(6, 7)
rc.info()