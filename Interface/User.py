from Interface.Desktop import Desktop
import os
import shutil
from os.path import isfile, join, isdir
from Archivos.escritorJSON import escritorJSON

class User:

    def __init__(self,name, password,admin,imgPath='imagenes/default.png',window=None):
        self.name = name
        self.password = password
        self.admin = admin
        self.imagePath = imgPath
        self.absoluta = "C:/Users/Samuel/Documents/SamPython/LuJo/Users"
        try:
            self.crearDirectorio()
        except FileExistsError:
            pass
        self.pathDirectorio = "../Users/"+self.name
        self.path = "Users/"+self.name
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
                contenido = os.listdir(self.absoluta)
                carpetas = [nombre for nombre in contenido if isdir(join(self.absoluta, nombre))]
                shutil.rmtree(path="../Users/"+u.getName())
            else:
                nueva.append(u)
        self.setUsuarios(nueva)
        writter.escribirUsuarios(nueva)
        return True

    def userEditar(self,user,name,password):
        writter = escritorJSON()
        nueva = []
        for u in self.usuarios:
            if u.getName() == user.getName():
                if u.getName()!= name:
                    u.name = name
                    os.renames("../"+u.path,"../Users/"+name)
                if u.getPassword()!=password:
                    u.password = password
                nueva.append(u)
            else:
                nueva.append(u)
        self.setUsuarios(nueva)
        writter.escribirUsuarios(nueva)
        return True