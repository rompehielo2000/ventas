    
    # metodo para limpiar la tabla

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    # metodo para limpiar las cajas de texto y para asignar el primer item al combobox

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

    # metodo para consultar por un producto y mostrarlo en la tabla

    def consultar(self):
        self.limpiarTabla()
        if aPro.tamanoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto", "No existen productos a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto", "Ingrese el codigo a consultar")
            pos = aPro.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto", "El codigo ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblProductos.setRowCount(1)
                self.tblProductos.setItem(0, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getCodigo()))
                self.tblProductos.setItem(0, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getNombre()))
                self.tblProductos.setItem(0, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getDescripcion()))
                self.tblProductos.setItem(0, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockMinimo()))
                self.tblProductos.setItem(0, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockActual()))
                self.tblProductos.setItem(0, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioCosto()))
                self.tblProductos.setItem(0, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioVenta()))
                self.tblProductos.setItem(0, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getProveedor()))
                self.tblProductos.setItem(0, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getAlmacen()))

    
    )

    # metodo para modificar los productos y regresar los valores a los campos
    def modificar(self):
        if aPro.tamanoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "No existen producto a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Producto", "Ingrese el codigo amodificar")
            pos = aPro.buscarProducto(codigo)
            if pos != -1:
                objProducto = aPro.devolverProducto(pos)
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtCodigo.setText(objProducto.getCodigo())
                self.txtCodigo.setVisible(False)
                self.lblCodigo.setVisible(False)
                self.txtNombre.setText(objProducto.getNombre())
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStockMinimo.setText(objProducto.getStockMinimo())
                self.txtStockActual.setText(objProducto.getStockActual())
                self.txtPrecioCosto.setText(objProducto.getPrecioCosto())
                self.txtPrecioVenta.setText(objProducto.getPrecioVenta())
                self.cboProveedor.setCurrentText(objProducto.getProveedor())
                self.cboAlmacen.setCurrentText(objProducto.getAlmacen())
    # metodo para grabar las modificaiones que se hicieron en el metodo anterior
    
    def grabar(self):
        pos = aPro.buscarProducto(self.obtenerCodigo())
        objProducto = aPro.devolverProducto(pos)
        objProducto.setNombre(self.obtenerNombre())
        objProducto.setDescripcion(self.obtenerDescripcion())
        objProducto.setStockMinimo(self.obtenerStockMinimo())
        objProducto.setStockActual(self.obtenerStockActual())
        objProducto.setPrecioCosto(self.obtenerPrecioCosto())
        objProducto.setPrecioVenta(self.obtenerPrecioVenta())
        objProducto.setProveedor(self.obtenerProveedor())
        objProducto.setAlmacen(self.obtenerAlmacen())
        self.btnModificar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        aPro.grabar()
        self.listar()
        self.txtCodigo.setVisible(True)
        self.lblCodigo.setVisible(True)



        def adicionaProducto(self, objPro):
        self.dataProductos.append(objPro)

    def devolverProducto(self, pos):
        return self.dataProductos[pos]
    
    def tamanoArregloProducto(self):
        return len(self.dataProductos)
    
    def buscarProducto(self, codigo):
        for i in range(self.tamanoArregloProducto()):
            if codigo == self.dataProductos[i].getCodigo():
                return i
        return -1
    
    def eliminarProducto(self, indice):
        del(self.dataProductos[indice])

        def buscarProducto(self):
        codigoProducto = self.txtCodigoProducto.text()
        if self.txtCodigoProducto.text() == "":
            QtWidgets.QMessageBox.information(self, "Codigo Producto", "Debe ingresar el codigo del producto...!!!", QtWidgets.QMessageBox.Ok)
        else:
            pos = aPro.buscarProducto(codigoProducto)
            objProducto = aPro.devolverProducto(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Codigo Producto", "Producto no registrado...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStock.setText(objProducto.getStockActual())
                self.txtPrecio.setText(objProducto.getPrecioVenta())