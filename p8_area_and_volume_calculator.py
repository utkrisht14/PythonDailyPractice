import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area method")

    def volume(self):
        raise NotImplementedError("Subclasses must implement volume method")


# 2D Shapes
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# 3D Shapes
class Cuboid(Shape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


# Example usage
if __name__ == "__main__":
    rect = Rectangle(5, 10)
    print(f"Rectangle Area: {rect.area()}")

    circle = Circle(7)
    print(f"Circle Area: {round(circle.area(), 2)}")

    cuboid = Cuboid(5, 4, 3)
    print(f"Cuboid Volume: {cuboid.volume()}")

    sphere = Sphere(3)
    print(f"Sphere Volume: {round(sphere.volume(), 2)}")