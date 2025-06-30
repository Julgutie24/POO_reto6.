import math

class Point:
    def __init__(self, x: int, y: int):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Las coordenadas deben ser números (int o float).")
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("El valor de x debe ser un número.")
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("El valor de y debe ser un número.")
        self._y = value

    def compute_distance(self, other):
        if not isinstance(other, Point):
            raise TypeError("El argumento debe ser una instancia de Point.")
        try:
            return math.hypot(self._x - other.get_x(), self._y - other.get_y())
        except Exception as e:
            raise Exception(f"Error al calcular la distancia: {e}")