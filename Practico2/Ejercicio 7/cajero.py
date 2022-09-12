class Cajero:
    __atencion = None
    __cliente = None
    __tiempo = None
    def __init__(self, atencion):
        self.__atencion = atencion
        self.__cliente = None
        self.__tiempo = 0
    def ingresarCliente(self, cliente):
        if(cliente != -1):
            self.__cliente = cliente
    def terminarCliente(self):
        cliente = None
        if(self.__cliente != None):
            self.__cliente = None
        return cliente
    def getEstado(self):
        return self.__cliente
    def aumentarTiempo(self):
        cliente = None
        if(self.__cliente != None):
            if(self.__tiempo < self.__atencion):
                self.__tiempo += 1
                self.__cliente.incrementarTiempo()
            else:
                self.__tiempo = 0
                cliente = self.__cliente
                self.__cliente = None
        return cliente