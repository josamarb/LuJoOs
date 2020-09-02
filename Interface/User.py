from Interface.Desktop import Desktop
import os
from Archivos.escritorJSON import escritorJSON

class User:

    def __init__(self,name, password,admin,imgPath='imagenes/default.png',window=None):
        self.name = name
        self.password = password
        self.admin = admin
        self.imagePath = imgPath
        try:
            self.crearDirectorio()
        except FileExistsError:
            pass
        self.pathDirectorio = "../Users/"+self.name
        self.desktop = window
        self.usuarios = []

    def setUsuarios(self,users):
        self.usuarios = users

    def crearDirectorio(self):
        self.path="../Users/"+self.name
        os.makedirs(self.path)

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def iniciar(self):
        self.desktop = Desktop(self.admin,self.pathDirectorio,self,self.usuarios)
        self.desktop.iniciar()

    def crearUsuario(self,name, password, check):
        writter = escritorJSON()
        nuevo = User(name,password,check)
        self.usuarios.append(nuevo)
        writter.escribirUsuarios(self.usuarios)

    def userEliminar(self,user):
        writter = escritorJSON()
        nueva = []
        for u in self.usuarios:
            if u.getName() == user.getName():
                pass
            else:
                nueva.append(u)
        self.setUsuarios(nueva)
        writter.escribirUsuarios(nueva)
        return True