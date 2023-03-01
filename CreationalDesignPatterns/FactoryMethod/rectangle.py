from shape import Shape
from dataclasses import dataclass


@dataclass
class Rectangle(Shape):
    height: int
    width: int

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)
