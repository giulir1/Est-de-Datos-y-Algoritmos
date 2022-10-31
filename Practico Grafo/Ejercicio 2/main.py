from grafo import Grafo

if __name__=='__main__':
    unGrafo = Grafo()
    unGrafo.agregarNodos()
    unGrafo.nuevaArista(1, 2)
    unGrafo.nuevaArista(0, 2)
    unGrafo.nuevaArista(1, 0)
    unGrafo.nuevaArista(2, 0)
    unGrafo.nuevaArista(2, 1)
    unGrafo.nuevaArista(0, 4)
    unGrafo.nuevaArista(0, 0)
    unGrafo.mostrarMatriz()
    print(unGrafo.adyacentes(0))