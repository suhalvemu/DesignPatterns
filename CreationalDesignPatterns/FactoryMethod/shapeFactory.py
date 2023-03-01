from rectangle import Rectangle
from cirle import Circle


class ShapeFactory:

    def create_shape(self, name):
        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))


def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape: ")
    shape = shape_factory.create_shape(shape_name)
    print(f"The type of object created: {type(shape)}")
    print(f"The area of the {shape_name} is: {shape.calculate_area()}")
    print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")


if __name__ == '__main__':
    shapes_client()
