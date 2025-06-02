def cuenta_grado(grafo_lista):
    '''
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    pass

def vertice_aislado(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene una lista de los vÃ©rtices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    pass

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    pass

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la funciÃ³n "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    pass
    
def es_completo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, devuelve True/False si el grafo es o no completo.
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B A', 'A C', 'C A', 'B C', 'C B']
    Ejemplo formato salida:
    	True
    '''
    pass
    	
def aristas_de(grafo, vertice):
    '''
    Dado un grafo en representacion de lista, devuelva todas las aristas salientes desde un vÃ©rtice dado
    Ejemplo Entrada:
    	grafo = ['3', 'A', 'B', 'C', 'A B', 'A C', 'B C']
	aristas_de(grafo, 'A')
    Ejemplo formato salida:
    	[('A', 'B'), ('A', 'C')]
    '''
    pass

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
    pass

def grafo_complementario(grafo):
    '''
    Dado un grafo en representacion de lista, devuelve el grafo complementario en forma de lista
    Ejemplo Entrada:
    	['3', 'A', 'B', 'C', 'A B', 'B C']
    Ejemplo formato salida:
    	(['A', 'B', 'C'], [('A', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B')])
    '''
    pass