import math
from .shape import Shape
from .point import Point

class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        for p in [p1, p2, p3]:
            if not isinstance(p, Point):
                raise TypeError("Todos los vértices deben ser instancias de Point.")
        super().__init__([p1, p2, p3])

    def compute_area(self):
        try:
            a, b, c = [edge.get_length() for edge in self.get_edges()]
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            if math.isnan(area) or area <= 0:
                raise ValueError("Los vértices no forman un triángulo válido (área no positiva).")
            return area
        except Exception as e:
            raise Exception(f"Error al calcular el área del triángulo: {e}")

    def compute_inner_angles(self):
        try:
            a, b, c = [edge.get_length() for edge in self.get_edges()]
            # Validar que no haya división por cero
            if a == 0 or b == 0 or c == 0:
                raise ValueError("Los lados del triángulo no pueden ser cero.")

            # Prevenir errores numéricos fuera del dominio de acos
            def seguro_acos(x):
                return math.acos(min(1, max(-1, x)))

            angle_A = math.degrees(seguro_acos((b**2 + c**2 - a**2) / (2 * b * c)))
            angle_B = math.degrees(seguro_acos((a**2 + c**2 - b**2) / (2 * a * c)))
            angle_C = 180.0 - angle_A - angle_B

            self.set_inner_angles([angle_A, angle_B, angle_C])
            return self.get_inner_angles()
        except Exception as e:
            raise Exception(f"Error al calcular los ángulos internos del triángulo: {e}")