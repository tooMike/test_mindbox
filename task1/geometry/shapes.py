import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный класс фигур."""

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    """Класс кругов."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Вычисление площади круга по радиусу."""
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Класс треугольников."""

    def __init__(self, a, b, c):
        # Проверяем, могут ли переданные стороны стать треугольником
        if not self.is_valid_triangle(a, b, c):
            raise ValueError(
                "Треугольник с такими сторонами не может существовать."
            )
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid_triangle(a, b, c):
        """Проверка, может ли существовать треугольник с такими сторонами."""
        return (a + b > c) and (a + c > b) and (b + c > a)

    def area(self):
        """Вычисление площади треугольника по формуле Герона."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self):
        """Проверка, что треугольник является прямоугольным."""
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)
