import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def validate_positive(**dimensions):
        for dimension, value in dimensions.items():
            if value <= 0:
                raise ValueError(f"{dimension} must be greater than 0")

    def display_name(self):
        return f"Shape: {self.name}"

    @abstractmethod
    def area(self):
        pass


class TwoDShape(Shape):
    @abstractmethod
    def perimeter(self):
        pass


class ThreeDShape(Shape):
    @abstractmethod
    def volume(self):
        pass


class Triangle(TwoDShape):
    def __init__(self, base: float, height: float, side1: float, side2: float, side3: float):
        super().__init__("Triangle")
        self.validate_positive(
            base=base,
            height=height,
            side1=side1,
            side2=side2,
            side3=side3
        )

        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(TwoDShape):
    def __init__(self, length: float, width: float):
        super().__init__("Rectangle")
        self.validate_positive(length=length, width=width)

        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(TwoDShape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.validate_positive(radius=radius)

        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Cuboid(ThreeDShape):
    def __init__(self, length: float, width: float, height: float):
        super().__init__("Cuboid")
        self.validate_positive(length=length, width=width, height=height)

        self.length = length
        self.width = width
        self.height = height

    def area(self):
        return 2 * (
            self.length * self.width
            + self.length * self.height
            + self.width * self.height
        )

    def volume(self):
        return self.length * self.width * self.height


class Cylinder(ThreeDShape):
    def __init__(self, radius: float, height: float):
        super().__init__("Cylinder")
        self.validate_positive(radius=radius, height=height)

        self.radius = radius
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


def display_shape_details(shape: Shape):
    print(shape.display_name())
    print(f"Area: {shape.area():.2f}")

    if isinstance(shape, TwoDShape):
        print(f"Perimeter: {shape.perimeter():.2f}")

    if isinstance(shape, ThreeDShape):
        print(f"Volume: {shape.volume():.2f}")

    print("-" * 30)


if __name__ == "__main__":
    shapes = [
        Triangle(base=10, height=5, side1=6, side2=8, side3=10),
        Rectangle(length=10, width=5),
        Circle(radius=5),
        Cuboid(length=5, width=10, height=2),
        Cylinder(radius=5, height=10),
    ]

    for shape in shapes:
        display_shape_details(shape)