def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    vertices, aristas = grafo_lista
    grados = {v: 0 for v in vertices}

    for origen, destino in aristas:
        grados[origen] += 1
        grados[destino] += 1

    return grados

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vÃ©rtices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    vertices, aristas = grafo_lista
    conectados = set()

    for origen, destino in aristas:
        conectados.add(origen)
        conectados.add(destino)

    aislados = [v for v in vertices if v not in conectados]
    return aislados
    

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    vertices, aristas = grafo_lista
    
    adyacencia = {v: [] for v in vertices}
    for origen, destino in aristas:
        adyacencia[origen].append(destino)
        adyacencia[destino].append(origen)  

    visitados = set()
    componentes = []

    def dfs(v, componente):
        visitados.add(v)
        componente.append(v)
        for vecino in adyacencia[v]:
            if vecino not in visitados:
                dfs(vecino, componente)

    for v in vertices:
        if v not in visitados:
            componente = []
            dfs(v, componente)
            componentes.append(componente)

    return componentes

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la funciÃ³n "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    componentes = componentes_conexas(grafo_lista)
    return len(componentes) == 1
    
def es_completo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, devuelve True/False si el grafo es o no completo.
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B A', 'A C', 'C A', 'B C', 'C B']
    Ejemplo formato salida:
    	True
    '''
    vertices, aristas = grafo_lista
    n = len(vertices)
    
    conexiones_posibles = set()
    
    for i in range(n):
        for j in range(n):
            if i != j:
                conexiones_posibles.add((vertices[i], vertices[j]))
    
    return conexiones_posibles.issubset(set(aristas))
    	
def aristas_de(grafo, vertice):
    '''
    Dado un grafo en representacion de lista, devuelva todas las aristas salientes desde un vÃ©rtice dado
    Ejemplo Entrada:
    	grafo = ['3', 'A', 'B', 'C', 'A B', 'A C', 'B C']
	aristas_de(grafo, 'A')
    Ejemplo formato salida:
    	[('A', 'B'), ('A', 'C')]
    '''
    cantidad_vertices = int(grafo[0])
    aristas_str = grafo[1 + cantidad_vertices:]

    aristas_salientes = []

    for a in aristas_str:
        origen, destino = a.split()
        if origen == vertice:
            aristas_salientes.append((origen, destino))

    return aristas_salientes

def grafo_inducido(grafo, subconjunto_vertices):
    '''
    Dado un grafo en representacion de lista, y un subconjunto de vertices,
    devuelva el subgrafo inducido
    Ejemplo Entrada:
    	grafo = ['4', 'A', 'B', 'C', 'D', 'A B', 'A C', 'B D']
	subconjunto_vertices = ['A', 'B', 'C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'B'), ('A', 'C')])
    '''
    cantidad_vertices = int(grafo[0])
    aristas_str = grafo[1 + cantidad_vertices:]

    aristas_inducidas = []

    for a in aristas_str:
        origen, destino = a.split()
        if origen in subconjunto_vertices and destino in subconjunto_vertices:
            aristas_inducidas.append((origen, destino))

    return (subconjunto_vertices, aristas_inducidas)

def grafo_complementario(grafo):
    '''
    Dado un grafo en representacion de lista, devuelve el grafo complementario en forma de lista
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B')])
    '''
    cantidad_vertices = int(grafo[0])
    vertices = grafo[1:cantidad_vertices + 1]
    aristas_str = grafo[1 + cantidad_vertices:]

    aristas_originales = set()
    for a in aristas_str:
        origen, destino = a.split()
        aristas_originales.add((origen, destino))

    aristas_complementarias = []
    for origen in vertices:
        for destino in vertices:
            if origen != destino and (origen, destino) not in aristas_originales:
                aristas_complementarias.append((origen, destino))

    return (vertices, aristas_complementarias)