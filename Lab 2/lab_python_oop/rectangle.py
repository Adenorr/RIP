from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"


    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        self.fc = FigureColor()
        self.fc.color = color

    def __repr__(self):
        return '{} {} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.color,
            self.width,
            self.height,
            self.square()
        )

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def square(self):
        return self.width*self.height
