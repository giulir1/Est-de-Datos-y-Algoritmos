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
            print('ERROR - Elemento "{}" inexistente.'.format(dato))
            return None
        else:
            if arbol.getDato() == dato:
                pass
                # print('El dato "{}" se encuentra en el arbol.'.format(dato))
            elif dato < arbol.getDato():
                arbol = arbol.getIzq()
                arbol = self.buscar(arbol, dato)
            else:
                arbol = arbol.getDer()
                arbol = self.buscar(arbol, dato)
        return arbol

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

    def suprimir(self, arbol, dato):
        pass

    def camino(self, dato1, dato2, nodos=[]):
        nodo1 = self.buscar(self.__raiz, dato1)
        nodo2 = self.buscar(self.__raiz, dato2)
        if (nodo1 is not None) and (nodo2 is not None):
            if dato1 < dato2:
                nodo1 = nodo1.getDer()
                if nodo1 is not None:
                    nodos.append(dato1)
                    dato1 = nodo1.getDato()
                    self.camino(dato1, dato2)
            elif dato1 > dato2:
                nodo1 = nodo1.getIzq()
                if nodo1 is not None:
                    nodos.append(dato1)
                    dato1 = nodo1.getDato()
                    self.camino(dato1, dato2)
            else:
                nodos.append(dato1)
        if (dato1 not in nodos) or (dato2 not in nodos):
            nodos = 'Camino inexistente.'
        return nodos

    def nivel(self, arbol, dato, nivel=0):
        if self.vacio(arbol):
            nivel = 'ERROR - Elemento inexistente.'
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

    def esHoja(self, arbol, dato):
        esHoja = 'El nodo con clave {} no es hoja'.format(dato)
        if self.vacio(arbol):
            esHoja = 'ERROR - Elemento inexistente.'
        else:
            if arbol.getDato() == dato:
                if (arbol.getDer() is None) and (arbol.getIzq() is None):
                    esHoja = 'El nodo con clave {} es hoja.'.format(dato)
            elif dato < arbol.getDato():
                arbol = arbol.getIzq()
                esHoja = self.esHoja(arbol, dato)
            else:
                arbol = arbol.getDer()
                esHoja = self.esHoja(arbol, dato)
        return esHoja

    def esHijo(self, arbol, dato1, dato2):
        esHijo = 'El nodo con clave {} no es hijo del nodo con clave {}.'.format(dato1, dato2)
        if self.vacio(arbol):
            esHijo = 'ERROR - El nodo ingresado como padre no existe en el arbol.'
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
                esHijo = self.esHijo(arbol, dato1, dato2)
            else:
                arbol = arbol.getDer()
                esHijo = self.esHijo(arbol, dato1, dato2)
        return esHijo

    def esPadre(self, arbol, dato1, dato2):
        esPadre = 'El nodo con clave {} no es padre del nodo con clave {}.'.format(dato1, dato2)
        if self.vacio(arbol):
            esPadre = 'ERROR - El nodo ingresado como padre no existe en el arbol.'
        else:
            if arbol.getDato() == dato1:
                izq = arbol.getIzq()
                der = arbol.getDer()
                if izq is not None:
                    if izq.getDato() == dato2:
                        esPadre = 'El nodo con clave {} es padre del nodo con clave {}.'.format(dato1, dato2)
                if der is not None:
                    if der.getDato() == dato2:
                        esPadre = 'El nodo con clave {} es padre del nodo con clave {}.'.format(dato1, dato2)
            elif dato1 < arbol.getDato():
                arbol = arbol.getIzq()
                esPadre = self.esPadre(arbol, dato1, dato2)
            else:
                arbol = arbol.getDer()
                esPadre = self.esPadre(arbol, dato1, dato2)
        return esPadre

    def altura(self, nodo, altura=0, maximo=0):
        if nodo is not None:
            dato = self.altura(nodo.getIzq(), altura+1, maximo)
            if altura > maximo:
                maximo = altura
            if dato > maximo:
                maximo = dato
            dato = self.altura(nodo.getDer(), altura+1, maximo)
            if dato > maximo:
                maximo = dato
        return maximo

    def preOrden(self, arbol):
        if not self.vacio(arbol):
            print(arbol.getDato())
            self.preOrden(arbol.getIzq())
            self.preOrden(arbol.getDer())

    def inOrden(self, arbol):
        if not self.vacio(arbol):
            self.inOrden(arbol.getIzq())
            print(arbol.getDato())
            self.inOrden(arbol.getDer())

    def postOrden(self, arbol):
        if not self.vacio(arbol):
            self.postOrden(arbol.getIzq())
            self.postOrden(arbol.getDer())
            print(arbol.getDato())
