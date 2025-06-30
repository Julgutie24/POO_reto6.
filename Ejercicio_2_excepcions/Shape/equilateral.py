from .triangle import Triangle
from .point import Point
import math

class Equilateral(Triangle):
    def __init__(self, p1: Point, side_length: float):
        if not isinstance(p1, Point):
            raise TypeError("El punto inicial debe ser una instancia de Point.")
        if not isinstance(side_length, (int, float)):
            raise TypeError("La longitud del lado debe ser un número.")
        if side_length <= 0:
            raise ValueError("La longitud del lado debe ser mayor que cero.")

        try:
            p2 = Point(p1.get_x() + side_length, p1.get_y())
            height = side_length * (math.sqrt(3) / 2)
            p3 = Point(p1.get_x() + side_length / 2, p1.get_y() + height)
            super().__init__(p1, p2, p3)
            self.set_is_regular(True)
        except Exception as e:
            raise Exception(f"No se pudo crear el triángulo equilátero: {e}")