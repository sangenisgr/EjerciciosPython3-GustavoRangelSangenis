

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from logica_proyecto import ClienteGustavo

if __name__ == '__main__':
    app = QApplication()

    window = ClienteGustavo()
    window.show()

    app.exec_()



