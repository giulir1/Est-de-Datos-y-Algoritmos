class Manejador:
    __cajero = None
    __cola = None
    __max = None
    def __init__(self, cajero = None, cola = None):
        self.__cajero = cajero
        self.__cola = cola
        self.__max = 0
    def llegadaCliente(self, cliente):
        self.__cola.insertar(cliente)
    def tiempoMax(self, cliente): #guarda el tiempo máximo esperado
        tiempo = cliente.getTiempo()
        print(tiempo) #//////////////////////
        if(tiempo > self.__max):
            self.__max = tiempo
    def atencion(self):
        band = True
        if(self.__cajero.getEstado() == None and self.__cola.getCant() > 0):
            cliente = self.__cola.suprimir()
            cliente.incrementarTiempo()
            self.__cajero.ingresarCliente(cliente)
            band = False
        return band
    def aumentarTiempoCola(self): #descompone la cola, incrementa el tiempo y los vuelve a insertar
        #print('ENTRA')
        clientes = self.__cola.recorrer()
        for cliente in clientes:
            cliente.incrementarTiempo()
            self.__cola.insertar(cliente)
        #print('Cantidad: ', self.__cola.getCant())
    def aumentarTiempoCajero(self): #aumenta el tiempo del cajero, como también el del cliente
        cliente = self.__cajero.aumentarTiempo()
        if(cliente != None):
            self.tiempoMax(cliente)
    def getMax(self):
        return self.__max