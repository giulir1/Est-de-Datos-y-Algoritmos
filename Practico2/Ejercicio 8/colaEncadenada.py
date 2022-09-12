from celda import Celda

class ColaE:
    __cant = None
    __primer = None 
    __ultimo = None
    def __init__(self, cant = 0):
        self.__cant = cant
        self.__primer = None
        self.__ultimo = None
    def vacia(self):
        return self.__cant == 0
    def insertar(self, dato): #REVISAR
        aux = Celda(dato)
        #aux.setSiguiente(None)
        if(self.__ultimo == None and self.__primer == None):
            self.__primer = aux
            self.__cant += 1
        else:
            if(self.__ultimo == None):
                self.__ultimo = aux
                self.__primer.setSiguiente(self.__ultimo)
            self.__ultimo.setSiguiente(aux)
            self.__ultimo = aux
            self.__cant += 1
            #print(self.__cant)
    def suprimir(self):
        if(self.vacia()):
            print('Cola vacia')
            return -2
        else:
            aux = self.__primer
            x = self.__primer.getDato()
            self.__primer = self.__primer.getSiguiente()
            self.__cant -= 1
            if(self.__primer == None):
                self.__ultimo = None
            del(aux)
            return x
    def recorrer(self):
        cola = []
        if(not self.vacia()):
            i = 0
            j = self.__cant
            while i < j:
                cont = self.suprimir()
                if(cont != -2):
                    cola.append(cont)
                i += 1
        return cola
    def getPrimer(self):
        return self.__primer
    def getCant(self):
        return self.__cant