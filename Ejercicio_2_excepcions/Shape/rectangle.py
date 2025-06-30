from .shape import Shape
from .point import Point

class Rectangle(Shape):
    def __init__(self, bottom_left: Point, width: float, height: float):
        if not isinstance(bottom_left, Point):
            raise TypeError("El punto inferior izquierdo debe ser una instancia de Point.")
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("El ancho y la altura deben ser números.")
        if width <= 0 or height <= 0:
            raise ValueError("El ancho y la altura deben ser mayores que cero.")

        self._width = width
        self._height = height

        try:
            vertices = [
                bottom_left,
                Point(bottom_left.get_x() + width, bottom_left.get_y()),
                Point(bottom_left.get_x() + width, bottom_left.get_y() + height),
                Point(bottom_left.get_x(), bottom_left.get_y() + height)
            ]
            super().__init__(vertices, is_regular=(width == height))
        except Exception as e:
            raise Exception(f"Error al construir los vértices del rectángulo: {e}")

    def get_width(self):
        return self._width

    def set_width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("El ancho debe ser un número.")
        if value <= 0:
            raise ValueError("El ancho debe ser mayor que cero.")
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La altura debe ser un número.")
        if value <= 0:
            raise ValueError("La altura debe ser mayor que cero.")
        self._height = value

    def compute_area(self):
        try:
            return self._width * self._height
        except Exception as e:
            raise Exception(f"No se pudo calcular el área: {e}")

    def compute_inner_angles(self):
        try:
            self.set_inner_angles([90.0, 90.0, 90.0, 90.0])
            return self.get_inner_angles()
        except Exception as e:
            raise Exception(f"Error al establecer los ángulos internos: {e}")