import sys
from PyQt5 import QtWidgets
from Vista.ventanaProductos import VentanaProductos

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # ejecuta la ventana ventas de productos
    window = VentanaProductos()
    app.exec() 