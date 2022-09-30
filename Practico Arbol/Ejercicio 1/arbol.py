from nodo import Nodo

# {}
class Arbol:
    __raiz = None

    def __init__(self):
        self.__raiz = None
    
    def vacio(self, arbol):
        return arbol == None

    def getRaiz(self):
        return self.__raiz

    def mostrarRaiz(self):
        return self.__raiz.getDato()

    def buscar(self, arbol, dato):
        if self.vacio(arbol):
            print('ERROR - Elemento inexistente.')
        else:
            if arbol.getDato() == dato:
                print('El dato "{}" se encuentra en el arbol.'.format(dato))
            elif dato < arbol.getDato():
                    arbol = arbol.getIzq()
                    self.buscar(arbol, dato)
            else:
                arbol = arbol.getDer()
                self.buscar(arbol, dato)
    
    def insertar(self, arbol, dato):
        if self.vacio(arbol):
            unNodo = Nodo(dato)
            self.__raiz = unNodo
        else:
            if dato == arbol.getDato():
                print('ERROR - El elemento ya existe en el árbol.')
            elif dato < arbol.getDato():
                if arbol.getIzq() is None:
                    arbol.setIzq(Nodo(dato))
                else:
                    arbol = arbol.getIzq()
                    self.insertar(arbol, dato)
            else:
                if arbol.getDer() is None:
                    arbol.setDer(Nodo(dato))
                else:
                    arbol = arbol.getDer()
                    self.insertar(arbol, dato)

    def nivel(self, arbol, dato, nivel=0):
        if self.vacio(arbol):
            nivel = ('ERROR - Elemento inexistente.')
        else:
            if arbol.getDato() == dato:
                arbol = None
            elif dato < arbol.getDato():
                    arbol = arbol.getIzq()
                    nivel += 1
                    nivel = self.nivel(arbol, dato, nivel)
            else:
                arbol = arbol.getDer()
                nivel += 1
                nivel = self.nivel(arbol, dato, nivel)
        return nivel

    def hoja(self, arbol, dato):
        esHoja = 'El nodo con clave {} no es hoja'.format(dato)
        if self.vacio(arbol):
            esHoja = 'ERROR - Elemento inexistente.'
        else:
            if arbol.getDato() == dato:
                if (arbol.getDer() is None) and (arbol.getIzq() is None):
                    esHoja = 'El nodo con clave {} es hoja.'.format(dato)
            elif dato < arbol.getDato():
                arbol = arbol.getIzq()
                esHoja = self.hoja(arbol, dato)
            else:
                arbol = arbol.getDer()
                esHoja = self.hoja(arbol, dato)
        return esHoja

    def hijo(self, arbol, dato1, dato2):
        esHijo = 'El nodo con clave {} no es hijo del nodo con clave {}.'.format(dato1, dato2)
        if self.vacio(arbol):
            esHijo = 'ERROR - Al menos uno de los nodos ingresados no existe en el arbol.'
        else:
            if arbol.getDato() == dato2:
                izq = arbol.getIzq()
                der = arbol.getDer()
                if izq is not None:
                    if izq.getDato() == dato1:
                        esHijo = 'El nodo con clave {} es hijo del nodo con clave {}.'.format(dato1, dato2)
                if der is not None:
                    if der.getDato() == dato1:
                        esHijo = 'El nodo con clave {} es hijo del nodo con clave {}.'.format(dato1, dato2)
            elif dato2 < arbol.getDato():
                arbol = arbol.getIzq()
                esHijo = self.hijo(arbol, dato1, dato2)
            else:
                arbol = arbol.getDer()
                esHijo = self.hijo(arbol, dato1, dato2)
        return esHijo
                
    def padre(self, arbol, dato1, dato2):
        esPadre = 'El nodo con clave {} no es padre del nodo con clave {}.'.format(dato1, dato2)
        if self.vacio(arbol):
            esPadre = 'ERROR - Al menos uno de los nodos ingresados no existe en el arbol.'
        else:
            if arbol.getDato() == dato1:
                print('encontro dato')
                izq = arbol.getIzq()
                der = arbol.getDer()
                if izq is not None:
                    if izq.getDato() == dato2:
                        esPadre = 'El nodo con clave {} es padre del nodo con clave {}.'.format(dato1, dato2)
                if der is not None:
                    if der.getDato() == dato2:
                        esPadre = 'El nodo con clave {} es padre del nodo con clave {}.'.format(dato1, dato2)
            elif dato2 < arbol.getDato():
                arbol = arbol.getIzq()
                esPadre = self.padre(arbol, dato1, dato2)
            else:
                arbol = arbol.getDer()
                esPadre = self.padre(arbol, dato1, dato2)
        return esPadre
