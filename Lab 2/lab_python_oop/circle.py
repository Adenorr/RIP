from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, color, rad):
        self.rad = rad
        self.fc = FigureColor()
        self.fc.color = color

    def __repr__(self):
        return '{} {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.color,
            self.rad,
            self.square()
        )

    def square(self):
        return math.pi*(self.rad**2)

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

