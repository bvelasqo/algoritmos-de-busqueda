class Nodo:
    def __init__(self, dato = '', heuristica = float("inf"), fn = float("inf")):
        self.dato = dato
        self.heuristica = heuristica
        self.conexiones = []
        self.fn = fn