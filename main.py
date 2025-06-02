from ejercicios.practica2 import *

def main():
    
  #  grafo = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'B')])

  # resultado_grados = cuenta_grado(grafo)
  # print("Grados:", resultado_grados)

  # aislados = vertice_aislado(grafo)
  # print("Vértices aislados:", aislados)

  #-----------------------------------------------

  # grafo = (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'E')])
  # resultado = componentes_conexas(grafo)
  # print("Componentes conexas:", resultado)

  #-----------------------------------------------

  # grafo = (
    # ['A', 'B', 'C', 'D', 'E'],  
    # [('A', 'B'), ('B', 'C'), ('C', 'B'), ('D', 'E')]  
  # )

  # resultado = es_conexo(grafo)

  # if resultado:
    # print("El grafo es conexo")
  # else:
    # print("El grafo NO es conexo")

#----------------------------------------------------

  # grafo = (
  # ['A', 'B', 'C'],
  # [('A', 'B'), ('B', 'A'), ('A', 'C'), ('C', 'A'), ('B', 'C'), ('C', 'B')]
  # )

  # print(es_completo(grafo))

#----------------------------------------------------

  # grafo = ['3', 'A', 'B', 'C', 'A B', 'A C', 'B C']
  # print(aristas_de(grafo, 'A'))

#----------------------------------------------------

  # grafo = ['4', 'A', 'B', 'C', 'D', 'A B', 'A C', 'B D']
  # subconjunto = ['A', 'B', 'C']

  # print(grafo_inducido(grafo, subconjunto))
    
#----------------------------------------------------

   grafo = ['3', 'A', 'B', 'C', 'A B', 'B C']
   print(grafo_complementario(grafo))

#----------------------------------------------------

if __name__ == '__main__':
    main()