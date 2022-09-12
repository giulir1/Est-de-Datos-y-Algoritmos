class Cajero:
    __atencion = None
    __cliente = None
    __tiempo = None
    def __init__(self, atencion):
        self.__atencion = atencion
        self.__cliente = None
        self.__tiempo = 0
    def setCliente(self, cliente):
        self.__cliente = cliente
    def getEstado(self):
        #print(self.__cliente)
        return self.__cliente
    def aumentarTiempo(self):
        cliente = None
        if(self.__cliente != None):
            if(self.__tiempo < self.__atencion):
                #print('t: ', self.__tiempo)
                self.__tiempo += 1
                self.__cliente += 1
            else:
                self.__tiempo = 0
                self.__cliente += 1
                cliente = self.__cliente
                self.__cliente = None
        return cliente