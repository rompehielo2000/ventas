class Producto:

    def __init__(self, codigo, descripcion, categoria, stock, precioUnitario):

        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__categoria = categoria
        self.__stock = stock
        self.__precioUnitario = precioUnitario

    def getCodigo(self):
        return self.__codigo
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getCategoria(self):
        return self.__categoria
    
    def getStock(self):
        return self.__stock
    
    def getPrecioUnitario(self):
        return self.__precioUnitario
    
    
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def setStock(self, stock):
        self.__stock = stock

    def setPrecioUnitario(self, precioUnitario):
        self.__precioUnitario = precioUnitario