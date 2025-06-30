from .line import Line
from .point import Point

class Shape:
    def __init__(self, vertices: list, is_regular: bool = False):
        if not isinstance(vertices, list):
            raise TypeError("Los vértices deben estar en una lista.")
        if len(vertices) < 3:
            raise ValueError("Una figura debe tener al menos 3 vértices.")
        for v in vertices:
            if not isinstance(v, Point):
                raise TypeError("Todos los elementos de vértices deben ser instancias de Point.")
        
        self._is_regular = is_regular
        self._vertices = vertices

        try:
            self._edges = self._compute_edges()
        except Exception as e:
            raise Exception(f"Error al calcular las aristas de la figura: {e}")
        
        self._inner_angles = []

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, value):
        if not isinstance(value, bool):
            raise TypeError("El valor debe ser booleano.")
        self._is_regular = value

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, value):
        if not isinstance(value, list):
            raise TypeError("Los vértices deben estar en una lista.")
        if len(value) < 3:
            raise ValueError("Una figura debe tener al menos 3 vértices.")
        for v in value:
            if not isinstance(v, Point):
                raise TypeError("Todos los elementos de vértices deben ser instancias de Point.")
        self._vertices = value
        self._edges = self._compute_edges()

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, value):
        if not isinstance(value, list):
            raise TypeError("Los ángulos internos deben estar en una lista.")
        if not all(isinstance(a, (int, float)) for a in value):
            raise TypeError("Todos los ángulos deben ser numéricos.")
        self._inner_angles = value

    def _compute_edges(self):
        edges = []
        n = len(self._vertices)
        for i in range(n):
            try:
                edge = Line(self._vertices[i], self._vertices[(i + 1) % n])
                edges.append(edge)
            except Exception as e:
                raise Exception(f"Error al crear una arista entre los vértices {i} y {(i + 1) % n}: {e}")
        return edges

    def compute_area(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

    def compute_perimeter(self):
        try:
            return sum(edge.get_length() for edge in self._edges)
        except Exception as e:
            raise Exception(f"Error al calcular el perímetro: {e}")

    def compute_inner_angles(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")