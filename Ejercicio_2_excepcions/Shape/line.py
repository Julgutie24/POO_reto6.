from .point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        # Validar que los puntos sean instancias de Point
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Los argumentos deben ser objetos de tipo Point.")
        
        self._start_point = start_point
        self._end_point = end_point

        try:
            self._length = self.compute_length()
        except Exception as e:
            raise ValueError(f"No se pudo calcular la longitud de la línea: {e}")

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, value):
        if not isinstance(value, Point):
            raise TypeError("El valor debe ser una instancia de Point.")
        self._start_point = value
        self._length = self.compute_length()

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, value):
        if not isinstance(value, Point):
            raise TypeError("El valor debe ser una instancia de Point.")
        self._end_point = value
        self._length = self.compute_length()

    def get_length(self):
        return self._length

    def compute_length(self):
        try:
            return self._start_point.compute_distance(self._end_point)
        except AttributeError as e:
            raise AttributeError("Uno de los puntos no tiene el método compute_distance.")
        except Exception as e:
            raise Exception(f"Error al calcular la longitud: {e}")