from nodo import Nodo
from conexion import Conexion

# Ejemplo Arboles de decisión


class Arbol:

    def __init__(self, dato_raiz, heuristica_raiz):
        # Nodo raiz o nodo inicial
        self.raiz = Nodo(dato_raiz, heuristica_raiz)
        # agregar raiz a la lista de nodos
        self.nodos = [self.raiz]

    # Verificar si el nodo existe en nuestra lista de nodos
    def nodo_existe(self, dato):
        for nodo in self.nodos:
            if nodo.dato == dato:
                return True
        return False

    def buscar_nodo(self, dato):
        for nodo in self.nodos:
            if nodo.dato == dato:
                return nodo
        return None

    # Agrega el nodo y le da la conexion si es necesario
    def agregar_nodo(self, dato_padre = None, dato = '', heuristica = 0, coste = 0):
        dato_padre = self.raiz.dato if dato_padre is None else dato_padre
        if not self.nodo_existe(dato):
            if self.nodo_existe(dato_padre):
                nuevo_nodo = Nodo(dato, heuristica)
                nodo_padre = self.buscar_nodo(dato_padre)
                self.nodos.append(nuevo_nodo)
                nodo_padre.conexiones.append(Conexion(nuevo_nodo, coste))
            else:
                print('El padre no existe')
        else:
            nuevo_nodo = self.buscar_nodo(dato)
            nodo_padre = self.buscar_nodo(dato_padre)
            nodo_padre.conexiones.append(Conexion(nuevo_nodo, coste))

    def bfs(self):
        self.visitados = set()
        self.pila = []
        self._bfs(self.raiz)

    def dfs(self):
        self.visitados = set()
        self._dfs(self.raiz)

    def brpm(self):
        # Inicializar memoria para la busqueda
        memoria = Nodo('')
        self.solucion = []
        self.fn_final = 0
        self.coste_final = 0
        self._brpm(memoria, self.raiz, 'Bucharest')
        print('\nSolucion: ', [nodo.dato for nodo in reversed(self.solucion)])
        print('FN FINAL: ', self.fn_final)
        print('COSTE FINAL: ', self.coste_final)

    # Función de Búsqueda en amplitud
    def _bfs(self, node):
        self.visitados.add(node)
        self.pila.append(node)
        while self.pila:  # Loop para visitar cada nodo
            current_node = self.pila.pop(0)
            print(current_node.dato, end=", ")
            for neighbour in current_node.conexiones:
                if neighbour.nodo.dato not in self.visitados:
                    self.visitados.add(neighbour.nodo.dato)
                    self.pila.append(neighbour.nodo)

    # Función de busqueda en profundidad
    def _dfs(self, nodo):
        if nodo not in self.visitados:
            print(nodo.dato, end=", ")
            self.visitados.add(nodo)
            for conexion in nodo.conexiones:
                self._dfs(conexion.nodo)

    # Busqueda recursiva primero el mejor
    def _brpm(self, memoria, nodo, meta):
        print('nodo: ', nodo.dato)
        if nodo.dato == meta:
            self.solucion.append(nodo)
        else:
            if len(nodo.conexiones) != 0:
                # Capturamos los 2 hijos del nodo que menos pese continuar a ellos
                conexiones = self._camino_mas_corto(nodo.conexiones)
                bucle = True
                while bucle:
                    if len(self.solucion) == 0:
                        if len(conexiones) < 2:
                            conexion1 = conexiones.pop(0)
                            if conexion1.fn > memoria.fn:
                                self.fn_final += memoria.fn
                                self.coste_final += memoria.fn - memoria.heuristica
                                self._brpm(
                                    Nodo('', heuristica=float("inf")), memoria, meta)
                            else:
                                self.fn_final += conexion1.fn
                                self.coste_final += conexion1.coste
                                self._brpm(memoria, conexion1.nodo, meta)
                        else:
                            conexion1 = conexiones.pop(0)
                            conexion2 = conexiones.pop(0)
                            if conexion2.fn < memoria.fn:
                                memoria = conexion2.nodo
                                memoria.fn = conexion2.fn
                            self.fn_final += conexion1.fn
                            self.coste_final += conexion1.coste
                            self._brpm(memoria, conexion1.nodo, meta)
                    else:
                        self.solucion.append(nodo)
                        bucle = False
            else:
                self._brpm(memoria, memoria, meta)

    # ordena las conexiones mas cortas del nodo
    def _camino_mas_corto(self, conexiones=[]):
        conexiones_ordenadas = conexiones
        conexiones_ordenadas.sort(key=lambda conexion: conexion.fn)
        print('hijos: ', [
              conexion.nodo.dato for conexion in conexiones_ordenadas])
        print('fn: ', [conexion.fn for conexion in conexiones_ordenadas])
        print()
        return conexiones_ordenadas
