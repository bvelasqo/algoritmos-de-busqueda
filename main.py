from arbol import Arbol

# EJEMPLO SACADO DE: https://www.uv.mx/personal/edbenitez/files/2010/09/CursoIA10-II-3.pdf
arbol = Arbol(dato_raiz='Arad', heuristica_raiz=366)
arbol.agregar_nodo(dato='Timisoara', heuristica=329, coste=118)
arbol.agregar_nodo(dato='Sibiu', heuristica=253, coste=140)
arbol.agregar_nodo(dato='Zerind', heuristica=374, coste=75)
arbol.agregar_nodo(dato_padre='Sibiu', dato='Rimnicu Vilcea',
                   heuristica=193, coste=80)
arbol.agregar_nodo(dato_padre='Sibiu', dato='Fagaras',
                   heuristica=178, coste=99)
arbol.agregar_nodo(dato_padre='Timisoara', dato='Lugoj',
                   heuristica=244, coste=111)
arbol.agregar_nodo(dato_padre='Zerind', dato='Oradea',
                   heuristica=380, coste=71)
arbol.agregar_nodo(dato_padre='Oradea', dato='Sibiu',
                   heuristica=253, coste=151)
arbol.agregar_nodo(dato_padre='Lugoj', dato='Mehadia',
                   heuristica=241, coste=70)
arbol.agregar_nodo(dato_padre='Mehadia', dato='Dobreta',
                   heuristica=242, coste=75)
arbol.agregar_nodo(dato_padre='Dobreta', dato='Craiova',
                   heuristica=160, coste=120)
arbol.agregar_nodo(dato_padre='Rimnicu Vilcea',
                   dato='Craiova', heuristica=160, coste=146)
# NODO A QUITAR PARA PROBAR MEMORIA
arbol.agregar_nodo(dato_padre='Rimnicu Vilcea',
                   dato='Pitesti', heuristica=98, coste=97)
arbol.agregar_nodo(dato_padre='Craiova', dato='Pitesti',
                   heuristica=98, coste=138)
arbol.agregar_nodo(dato_padre='Pitesti', dato='Bucharest',
                   heuristica=0, coste=101)
arbol.agregar_nodo(dato_padre='Fagaras', dato='Bucharest',
                   heuristica=0, coste=211)
arbol.agregar_nodo(dato_padre='Bucharest', dato='Giurgiu',
                   heuristica=77, coste=90)
arbol.agregar_nodo(dato_padre='Bucharest', dato='Urziceni',
                   heuristica=80, coste=85)
arbol.agregar_nodo(dato_padre='Urziceni', dato='Hirsova',
                   heuristica=151, coste=98)
arbol.agregar_nodo(dato_padre='Urziceni', dato='Vaslui',
                   heuristica=199, coste=142)
arbol.agregar_nodo(dato_padre='Hirsova', dato='Eforie',
                   heuristica=161, coste=86)
arbol.agregar_nodo(dato_padre='Vaslui', dato='Iasi',
                   heuristica=226, coste=92)
arbol.agregar_nodo(dato_padre='Iasi', dato='Neamt',
                   heuristica=234, coste=87)
print('Búsquedas')
print('\nBFS')
arbol.bfs()
print('\n\nDFS')
arbol.dfs()
print('\n\nBRPM')
arbol.brpm()