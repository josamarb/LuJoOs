from Interface.Desktop import Desktop

class User:

    def __init__(self,name, password,admin,imgPath):
        self.name = name
        self.password = password
        self.admin = admin
        self.imagePath = imgPath
        self.desktop = None

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def iniciar(self):
        self.desktop = Desktop()
        self.desktop.iniciar()
