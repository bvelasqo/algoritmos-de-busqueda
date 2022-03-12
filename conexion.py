# REPRESENTA LAS CONEXIONES DEL NODO ESPECFICANDO A QUE NODO CONECTAR Y CUANTO CUESTA LA CONEXION
from nodo import Nodo
class Conexion:
    def __init__(self, nodo = Nodo(), coste = 0):
        self.nodo = nodo
        self.coste = coste
        self.fn = nodo.heuristica + coste
