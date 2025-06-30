from .triangle import Triangle
from .point import Point

class Isosceles(Triangle):
    def __init__(self, p1: Point, base: float, height: float):
        if not isinstance(p1, Point):
            raise TypeError("El primer punto debe ser una instancia de Point.")
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("La base y la altura deben ser números.")
        if base <= 0 or height <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")

        try:
            p2 = Point(p1.get_x() + base, p1.get_y())
            p3 = Point(p1.get_x() + base / 2, p1.get_y() + height)
            super().__init__(p1, p2, p3)
        except Exception as e:
            raise Exception(f"No se pudo crear el triángulo isósceles: {e}")