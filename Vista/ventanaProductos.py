from PyQt5 import QtWidgets, uic
from Controlador.productos import Producto
from Controlador.arregloProductos import *

aPro = ArregloProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/frmProductos.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnListar.clicked.connect(self.listar)
        self.btnBuscar.clicked.connect(self.buscar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabarModificado.clicked.connect(self.grabar_modificado)
    
        self.show()

    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerCategoria(self):
        return self.cboCategoria.currentText()
    
    def obtenerStock(self):
        return self.txtStock.text()
    
    def obtenerPrecioUnitario(self):
        return self.txtPrecioUnitario.text()
    
    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)
    
    
    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Codigo del producto...!!!"
            
        if self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripcion del producto...!!!"
        
        if self.cboCategoria.currentText() == "Selecionar categoria":
            self.cboCategoria.setCurrentIndex(0)
            return "Categoria del producto...!!!"
        
        if self.txtStock.text() == "":
            self.txtStock.setFocus()
            return "Stock del producto...!!!"
        
        if self.txtPrecioUnitario.text() == "":
            self.txtPrecioUnitario.setFocus()
            return "Precio Unitario del producto...!!!"
            
        else:
            
            return ""

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtDescripcion.clear()
        self.cboCategoria.setCurrentIndex(0)
        self.txtStock.clear()
        self.txtPrecioUnitario.clear()

    def registrar(self):
        if self.valida() == "":
            objPro = Producto(self.obtenerCodigo(), self.obtenerDescripcion(), self.obtenerCategoria(), self.obtenerStock(), self.obtenerPrecioUnitario())
            codigo = self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", "El codigo ingresado ya existe...!!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def listar(self):
        if aPro.tamanoArregloProducto() > 0:
            self.tblProductos.setRowCount(aPro.tamanoArregloProducto())
            self.tblProductos.setColumnCount(5)
            for i in range(aPro.tamanoArregloProducto()):
                self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigo()))
                self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcion())) 
                self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCategoria()))
                self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStock()))
                self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioUnitario()))
            self.tblProductos.update()
        else:
            QtWidgets.QMessageBox.information(self, "Listar Productos", "No existen productos para listar...!!!", QtWidgets.QMessageBox.Ok)
            
            
    def buscar(self):
        codigo, _ = QtWidgets.QInputDialog.getText(self, "Buscar Producto", "Ingrese el codigo del Producto")
        if codigo == "":
            QtWidgets.QMessageBox.information(self, "Codigo Producto", "Debe ingresar el codigo del Producto...!!!", QtWidgets.QMessageBox.Ok)
        else:
            pos = aPro.buscarProducto(codigo)
        if pos == -1:
            QtWidgets.QMessageBox.information(self, "Codigo Producto", "Producto no registrado...!!!", QtWidgets.QMessageBox.Ok)
        else:
            producto = aPro.devolverProducto(pos)
            self.txtCodigo.setText(producto.getCodigo() + " ")
            
            self.tblProductos.setRowCount(1)
            self.tblProductos.setColumnCount(5)
            self.tblProductos.setItem(0, 0, QtWidgets.QTableWidgetItem(producto.getCodigo()))
            self.tblProductos.setItem(0, 1, QtWidgets.QTableWidgetItem(producto.getDescripcion())) 
            self.tblProductos.setItem(0, 2, QtWidgets.QTableWidgetItem(producto.getCategoria()))
            self.tblProductos.setItem(0, 3, QtWidgets.QTableWidgetItem(producto.getStock()))
            self.tblProductos.setItem(0, 4, QtWidgets.QTableWidgetItem(producto.getPrecioUnitario()))



    def eliminar(self):
        if aPro.tamanoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto", "No existen Producto a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(indiceFila, 0).text()
                pos = aPro.buscarProducto(codigo)
                aPro.eliminarProducto(pos)
                
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto", "Debes seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aPro.tamanoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "No existen producto a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Producto", "Ingrese el codigo amodificar")
            pos = aPro.buscarProducto(codigo)
            if pos != -1:
                objProducto = aPro.devolverProducto(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabarModificado.setVisible(True)
                self.txtCodigo.setText(objProducto.getCodigo())
                self.txtCodigo.setVisible(False)
                self.lblCodigo.setVisible(False)
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.cboCategoria.setCurrentText(objProducto.getCategoria())
                self.txtStock.setText(objProducto.getStock())
                self.txtPrecioUnitario.setText(objProducto.getPrecioUnitario())

    def grabar_modificado(self):
        pos = aPro.buscarProducto(self.obtenerCodigo())
        objProducto = aPro.devolverProducto(pos)
        objProducto.setDescripcion(self.obtenerDescripcion())
        objProducto.setCategoria(self.obtenerCategoria())
        objProducto.setStock(self.obtenerStock())
        objProducto.setPrecioUnitario(self.obtenerPrecioUnitario())
        self.btnModificar.setVisible(True)
        self.btnGrabarModificado.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        self.listar()
        self.txtCodigo.setVisible(True)
        self.lblCodigo.setVisible(True)