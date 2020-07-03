from PySide2.QtWidgets import QMainWindow, QFileDialog

from Proyecto.estudiante import Estudiante
from ui_proyecto import Ui_ClienteGustavo


import pickle
import socket as s
import time

class Cliente:
    client = None

    def __init__(self, ip='3.17.169.218', puerto=45019):
        ip = str(ip)
        puerto = int(puerto)
        try:
            self.client = s.socket()
        except OSError as msg:
            self.client = None
            print(msg)
        try:
            self.client.connect((ip, puerto))
        except OSError as msg:
            self.client.close()
            self.client = None
            print(msg)


    def connection_state(self):
        if self.client == None:
            return False
        else:
            return True


    def enviarEstudiante(self, message):
        self.client.send(message)


    def enviarMensaje(self, message):
        self.client.send(message.encode())


    def enviarArchivo(self, buffer):
        self.client.send(buffer)


    def recibir(self):
        message = self.client.recv(1024)
        print(message)
        return message.decode()


    def desconectar(self):
        self.client.close()


class ClienteGustavo(QMainWindow):
    def __init__(self):
        super(ClienteGustavo, self).__init__()
        self.ui = Ui_ClienteGustavo()
        self.ui.setupUi(self)
        self.ui.conectar.clicked.connect(self.conectar)
        self.ui.enviarB.clicked.connect(self.enviarB)
        self.ui.abrirB.clicked.connect(self.abrirB)
        self.reset_connection()

    def enviarB(self):
        filename = self.ui.abrir.text()
        self.client.enviarMensaje('iniciozip')
        file = open(filename, 'rb')
        i = file.read(500)
        count = 0
        while i:
            print(f'[{count + 1}:{len(i)}] {len(i)}')
            self.client.enviarArchivo(i)
            count += 1
            i = file.read(500)
        file.close()
        time.sleep(0.5)
        self.client.enviarMensaje('finzip')
        self.ui.estado.setText('Archivo enviado')

    def abrirB(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'Zip Files(*.zip)')
        print(filename[0])
        self.ui.abrir.setText(filename[0])



    def server_widgets(self, state):
        if state:
            self.ui.ip.setEnabled(True)
            self.ui.puerto.setEnabled(True)
        else:
            self.ui.ip.setEnabled(False)
            self.ui.puerto.setEnabled(False)

    def student_widgets(self, state):
        if state:
            self.ui.nombre.setEnabled(True)
            self.ui.email.setEnabled(True)
            self.ui.contrasenia.setEnabled(True)
            self.ui.enviarB.setEnabled(True)
        else:
            self.ui.nombre.setEnabled(False)
            self.ui.email.setEnabled(False)
            self.ui.contrasenia.setEnabled(False)
            self.ui.enviarB.setEnabled(False)

    def file_widgets(self, state):
        if state:
            self.ui.abrir.setEnabled(True)
            self.ui.enviarB.setEnabled(True)
            self.ui.abrirB.setEnabled(True)
        else:
            self.ui.abrir.setEnabled(False)
            self.ui.enviarB.setEnabled(False)
            self.ui.abrirB.setEnabled(False)

    def send_student(self):
        try:
            name = self.ui.nombre.text()
            email = self.ui.email.text()
            password = self.ui.contrasenia.text()
            student = Estudiante(name, email, password)
            student_bytes = pickle.dumps(student)
            print(student)
            self.client.enviarEstudiante(student_bytes)
            message = (self.client.recibir())
            print(message)
            if message == 'enviararchivo':
                self.file_widgets(1)
                self.student_widgets(0)
            else:
                self.ui.estado.setText('servidor no envió enviararchivo')
        except:
            self.reset_connection()

    def reset_connection(self):
        try:
            self.client.close_connection()
        except:
            pass
        self.ui.estado.setText('Desconectado')
        self.ui.conectar.setText('Conectar')
        self.ui.ip.setText('3.17.169.218')
        self.ui.puerto.setText('45019')
        self.file_widgets(0)
        self.student_widgets(0)
        self.server_widgets(1)

    def conectar(self):
        self.server_widgets(0)
        self.ip = self.ui.ip.text()
        self.puerto = self.ui.puerto.text()
        if self.ui.conectar.text() == 'Conectar':
            self.client = Cliente(self.ip, self.puerto)
            if self.client.connection_state():
                self.ui.estado.setText('Conectado')
                self.ui.conectar.setText('Desconectar')
                self.student_widgets(1)
            else:
                self.ui.estado.setText('Error al conectar')
                self.reset_connection()
        else:
            self.reset_connection()





