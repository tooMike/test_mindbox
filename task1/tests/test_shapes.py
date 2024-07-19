import unittest

from geometry.shapes import Circle, Triangle


class TestShapes(unittest.TestCase):
    """Тестирование вычислений."""

    def test_circle_area(self):
        """Проверяем, что площадь круга вычисляется правильно."""
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_triangle_area(self):
        """Проверяем, что площадь треугольника вычисляется правильно."""
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=5)

    def test_right_triangle(self):
        """Проверяем, правильность определения прямоугольного треугольника."""
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right_triangle())

    def test_invalid_triangle(self):
        """
        Проверяем, правильность определения, может ли из указанных сторон
        получиться треугольник.
        """
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)


if __name__ == '__main__':
    unittest.main()
