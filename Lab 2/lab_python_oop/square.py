from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, color, side):
        self.side = side
        super().__init__(color, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.color,
            self.side,
            self.square()
        )

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
