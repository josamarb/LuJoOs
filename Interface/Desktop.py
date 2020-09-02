#from Interface.User import User
from tkinter import *
from datetime import datetime
import threading
from tkinter import messagebox
import os
from os.path import isfile, join, isdir
from tkinter import messagebox



class Desktop:

    def __init__(self,administrador,path,user,users =[]):
        self.admin = administrador
        self.rutaDirectorio = path
        self.rutaActual = ""
        self.user = user
        self.users = users
        self.absoluta = "C:/Users/Samuel/Documents/SamPython/LuJo/Users"
        self.ventana = Tk()
        self.widgets()

    def widgets(self):
        self.ventana.wm_attributes('-fullscreen','true')
        self.ventana.geometry('1366x768')
        vc = Canvas(self.ventana, width=1366, height=768)
        vc.place(x=0, y=0)
        logo = PhotoImage(file="imagenes/LOGO.png")
        vc.create_image(0, 0, image=logo, anchor="nw")
        self.btnInicio = Button(self.ventana, text=" Menu ",command=self.showMenu)
        self.btnInicio.place(x=0,y=742)
        self.estadoMenu=True

    # ---------------------------------Reloj-----------------------------------------------------------------------------
    def iniciar(self):
        hilo1 = threading.Thread(target=self.showReloj)
        hilo1.start()
        self.ventana.mainloop()

    def showReloj(self):
        while True:
            now = datetime.now()
            if now.minute<10:
                min = "0"+str(now.minute)
            else:
                min = str(now.minute)
            if now.second<10:
                seg= "0"+str(now.second)
            else:
                seg = str(now.second)
            hora = str(now.hour)+":"+min+":"+seg
            Label(text=hora).place(x=1300,y=742)
    #-------------------------------Comonentes del menu inicio----------------------------------------------------------
    def showMenu(self):
        if self.estadoMenu:
            self.lfInicio = LabelFrame(self.ventana, padx=30, pady=40)
            self.lfInicio.place(x=0, y=555)
            self.btnCrearUsuario = Button(self.lfInicio, text=" Crear Usuario ", command=self.ventanaCrearusuarios)
            self.btnCrearUsuario.grid(row=1,column=1)
            self.btnEliminarusuario = Button(self.lfInicio, text=" Eliminar Usuario ", command=self.ventanaEliminarUsuarios)
            self.btnEliminarusuario.grid(row=2, column=1)
            self.btnExplorador = Button(self.lfInicio, text=" Explorador ", command=self.exploradorArchivos)
            self.btnExplorador.grid(row=3, column=1)
            self.btnCerrarSesion = Button(self.lfInicio, text=" Cerrar Sesion ", command=self.cerrarSesion)
            self.btnCerrarSesion.grid(row=4, column=1)
            self.btnApagar = Button(self.lfInicio, text=" Apagar ", command=self.apagar)
            self.btnApagar.grid(row=5, column=1)
            self.estadoMenu=False
        else:
            self.cerrarMenu()

    def cerrarMenu(self):
            self.estadoMenu=True
            self.lfInicio.destroy()

    def apagar(self):
        self.ventana.quit()
        self.ventana.destroy()

    def cerrarSesion(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

    def cerrarAdministradorUsuarios(self):
        pass
        #self.lfUsuarios.destroy()

    #---------------------------Administrar Usuarios-----------------------------------------------------------

    def ventanaEliminarUsuarios(self):
        if self.admin:
            ventana = Tk()
            for i in range(len(self.users)) :
                nombreUser = Label(ventana, text=self.users[i].getName())
                nombreUser.grid(row=i, column=1)
                btnEliminar = Button(ventana, text="Eliminar", command=lambda u=self.users[i]: self.eliminarUsuario(u,ventana, ))
                btnEliminar.grid(row=i, column=2)
            btncerrar = Button(ventana, text="Cerrar", command=lambda: self.cerrarVentana(ventana, )).grid(row=len(self.users), column=2)
            ventana.mainloop()
        else:
            messagebox.showinfo(message="No tiene derechos de administrador", title="Restringido")

    def cerrarVentana(self,ventana):
        ventana.quit()
        ventana.destroy()

    def ventanaCrearusuarios(self):
        if self.admin:
            ventana = Tk()
            ventana.geometry('300x200')
            username = StringVar()
            password = StringVar()
            isAdmin = BooleanVar()
            nombreUser = Label(ventana, text="Nombre Usuario").grid(row=1, column=1)
            userName = Entry(ventana, textvariable=username, width=15).grid(row=1, column=2)
            nombreUser = Label(ventana, text="Contraseña").grid(row=2, column=1)
            userName = Entry(ventana, show="*", textvariable=password, width=15).grid(row=2, column=2)
            adminCheck = Checkbutton(ventana, text="¿Administrador?", variable=isAdmin).grid(row=3, column=1)
            btnCrear = Button(ventana, text="Crear",
                                 command=lambda: self.crearUsuario(username.get(),password.get(), isAdmin.get(),ventana)).grid(row=4, column=2)
            btnCerrar = Button(ventana, text="Cerrar",
                              command=lambda: self.cerrarVentana(ventana)).grid(row=5,column=2)
            ventana.mainloop()
        else:
            messagebox.showinfo(message="No tiene derechos de administrador", title="Restringido")

    def eliminarUsuario(self,u,ventana):
        if self.user.userEliminar(u):
            self.cerrarVentana(ventana)
        else:
            print("error")

    def crearUsuario(self,name, password, check,ventana):
        print(name)
        if len(name) == 0 or len(password)==0:
            self.user.crearUsuario("Enola", "12345", check)
            self.cerrarVentana(ventana)
        else:
            self.user.crearUsuario(name,password,check)
            self.cerrarVentana(ventana)
            """"
            MsgBox = messagebox.askquestion('Reiniciar', 'Es necesario reiniciar para guardar los Cambios \n ¿Reiniciar ahora?',icon = 'warning')
            if MsgBox == 'yes':
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                messagebox.showinfo('Return', 'You will now return to the application screen')
            """



#-------------------Eplorador de archivos-----------------------------------
    def exploradorArchivos(self):
        self.cerrarMenu()
        self.exploradorArchivos = Tk()
        self.exploradorArchivos.geometry('800x400')
        self.btnRegresar = Button(self.exploradorArchivos, text="Regresar",command=lambda: self.showFrame(self.cortarDireccion(), ))
        self.btnRegresar.grid(row=1, column=2)
        #self.btnNuevo = Button(self.exploradorArchivos, text="Nuevo Archivo de texto")
        #self.btnNuevo.grid(row=1, column=3)

        self.lfexplorador = LabelFrame(self.exploradorArchivos,padx=30, pady=10)
        self.lfexplorador.grid(row=2, column=1)

        self.btnSalirExplorador = Button(self.exploradorArchivos, text="Cerrar", command=self.cerrarExplorador)
        self.btnSalirExplorador.grid(row=3, column=2)

        self.showFrame(self.rutaDirectorio)
        #self.showFrame("C:/")
    def cerrarExplorador(self):
        self.exploradorArchivos.destroy()

    def showFrame(self,path):
        self.lfexplorador.destroy()
        self.lfexplorador = LabelFrame(self.exploradorArchivos, padx=30, pady=40)
        self.lfexplorador.grid(row=1, column=1)
        if len(self.rutaActual)==0:
            self.rutaActual = path
        else:
            self.rutaActual = self.rutaActual +"/"+ path
        elementos=self.getElementosRutas(self.rutaActual)
        folders = elementos[0]
        files = elementos[1]
        for f in range(len(folders)):
            label = Label(self.lfexplorador,text=folders[f])
            label.grid(row=f, column=1)
            btnAbrir= Button(self.lfexplorador, text="Abrir",command=lambda u=folders[f]: self.showFrame(u))
            btnAbrir.grid(row=f, column=2)

        for f in range(len(files)):
            label = Label(self.lfexplorador, text=files[f])
            label.grid(row=f, column=1)
            btnAbrir = Button(self.lfexplorador, text="Abrir",command=lambda u=files[f]: self.abrirArchivo(u))
            btnAbrir.grid(row=f, column=2)

    def crearArchivoFolder(self):
        ventana = Tk()


    def abrirArchivo(self,ruta):
        r = self.rutaActual.split("Users")
        os.system("start "+self.absoluta+r[1]+"/"+ruta)
        """"
        extension = ruta.split(".")[len(ruta.split("."))-1]
        if extension == "txt":
            os.system("notepad "+ruta)
        elif extension in ["jpg","gif", "png"]:
            os.system("mspaint "+ruta)
        elif extension in ["avi", "mp4", "mwv"]:
            pass
        elif extension in ["mp3", "wav", "wma"]:
            pass
        elif extension in ["zip", "rar"]:
            pass
        elif extension == "pdf":
            pass
        elif extension == "exe":
            pass
        """
    def getElementosRutas(self,ruta):
        contenido = os.listdir(ruta)

        # Archivos
        archivos = [nombre for nombre in contenido if isfile(join(ruta, nombre))]
        print('Archivos')
        print(archivos)

        # Carpetas
        carpetas = [nombre for nombre in contenido if isdir(join(ruta, nombre))]
        print('Carpetas')
        print(carpetas)
        return (carpetas,archivos)



    def cortarDireccion(self):
        cortes = self.rutaActual.split("/")
        nueva = ""
        for i in range(len(cortes)-1):
            if i==0:
                nueva = nueva+cortes[i]
            else:
                nueva = nueva+"/"+cortes[i]
        self.rutaActual=nueva
        return ""
#--------------------------------------------------------------------------------