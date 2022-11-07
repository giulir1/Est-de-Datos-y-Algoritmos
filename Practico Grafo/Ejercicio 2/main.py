from grafoSec import GrafoSec

if __name__ == '__main__':
    unGrafo = GrafoSec()
    unGrafo.agregarNodos()
    unGrafo.nuevaArista(1, 2)
    unGrafo.nuevaArista(0, 2)
    unGrafo.nuevaArista(1, 0)
    unGrafo.nuevaArista(2, 0)
    unGrafo.nuevaArista(2, 1)
    unGrafo.nuevaArista(0, 4)
    unGrafo.nuevaArista(0, 0)
    unGrafo.mostrarMatriz()
    print(unGrafo.adyacentes('a'))
    print(unGrafo.caminoNodo('a'))
    print(unGrafo.camino('a', 'e'))
    print(unGrafo.gradoEntrada('a'))
    print(unGrafo.gradoSalida('a'))
