import unittest

from geometry.area_calculator import calculate_area
from geometry.shapes import Circle, Triangle


class TestAreaCalculator(unittest.TestCase):
    """Тестирование вычисления площадей."""

    def test_calculate_area_circle(self):
        """Проверяем, что площадь круга вычисляется правильно."""
        circle = Circle(5)
        self.assertAlmostEqual(
            calculate_area(circle),
            78.53981633974483,
            places=5
        )

    def test_calculate_area_triangle(self):
        """Проверяем, что площадь треугольника вычисляется правильно."""
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=5)


if __name__ == '__main__':
    unittest.main()
