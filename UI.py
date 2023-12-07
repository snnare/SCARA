import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.uic import loadUi

class MiVentana(QMainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()

        # Cargar la interfaz de usuario desde el archivo .ui
        loadUi("Main.ui", self)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
