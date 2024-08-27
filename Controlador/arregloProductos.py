class ArregloProductos:

    def __init__(self):
        self.dataProducto = []

    def adicionaProducto(self, objPro):
        self.dataProducto.append(objPro)

    def devolverProducto(self, pos):
        return self.dataProducto[pos]
    
    def tamanoArregloProducto(self):
        return len(self.dataProducto)
    
    def buscarProducto(self, codigo):
        for i in range(self.tamanoArregloProducto()):
            if codigo == self.dataProducto[i].getCodigo():
                return i
        return -1
    
    def eliminarProducto(self, indice):
        del(self.dataProducto[indice])
