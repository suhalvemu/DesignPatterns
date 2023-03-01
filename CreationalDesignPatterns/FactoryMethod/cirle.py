from shape import Shape
from dataclasses import dataclass


@dataclass
class Circle(Shape):
    radius: float

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
