from hash import Hash


if __name__ == '__main__':
    tablaHash = Hash()
    cad = 15
    cad2 = 61
    tablaHash.agregar(cad)
    tablaHash.agregar(cad2)
    tablaHash.mostrar()
    tablaHash.buscar(cad)
    tablaHash.buscar(cad2)
    tablaHash.buscar(21666)
