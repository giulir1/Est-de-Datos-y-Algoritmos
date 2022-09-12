class Controlador:
    __manejador = None
    __ordenInicio = None
    __ordenFinal = None
    __movimientos = None
    __optimo = None
    def __init__(self):
        self.__manejador = None
        self.__ordenInicio = None
        self.__ordenFinal = None
        self.__movimientos = 0
        self.__optimo = None
    def moveOp(self, dif):
        self.__optimo = (2**dif)-1
    def verifFinal(self, cont, dif):
        band = False
        i = 0
        long = len(cont)
        if(long == dif):
            band = True
        return band
    def escanear(self, dif):
        band = False
        cont = self.__manejador.escanear()
        if(self.verifFinal(cont, dif)):
            band = True
        return band
    def validarOrden(self, orden):
        band = False
        long = self.__manejador.getLen()
        try:
            orden = int(orden)
            if(orden > 0 and orden <= long):
                band = True
        except ValueError:
            band = False
        return band
    def loadOrdenI(self, orden):
        band = True
        if(self.validarOrden(orden)):
            if(self.__manejador.getTope(int(orden)) != -1):
                self.__ordenInicio = int(orden)
            else:
                band = False
        else:
            band = False
        return band
    def loadOrdenF(self, orden):
        band = True
        if(self.validarOrden(orden) and int(orden) != self.__ordenInicio):
            if(self.__manejador.getTope(int(orden)) == -1):
                self.__ordenFinal = int(orden)
                self.__movimientos += 1
            elif(self.__manejador.getContTope(int(orden)) > self.__manejador.getContTope(self.__ordenInicio)):
                self.__ordenFinal = int(orden)
                self.__movimientos += 1
            else:
                band = False
        else:
            band = False
        return band
    def loadManejador(self, manejador):
        self.__manejador = manejador
    def mover(self):
        self.__manejador.moverTope(self.__ordenInicio, self.__ordenFinal)
    def mostrar(self):
        text = '{}'.format(self.__manejador)
        return text
    def getMovimientos(self):
        return self.__movimientos
    def puntaje(self):
        band = False
        if(self.__movimientos == self.__optimo):
            band = True
        return band