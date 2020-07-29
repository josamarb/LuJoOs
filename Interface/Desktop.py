from tkinter import *
from datetime import datetime
import threading

class Desktop:

    def __init__(self):
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
            self.lfInicio.place(x=0, y=580)
            self.btnPanel = Button(self.lfInicio, text=" Panel ", command=self.cerrarMenu)
            self.btnPanel.grid(row=1,column=1)
            self.btnExplorador = Button(self.lfInicio, text=" Explorador ", command=self.cerrarMenu)
            self.btnExplorador.grid(row=2, column=1)
            self.btnApagar = Button(self.lfInicio, text=" Explorador ", command=self.apagar)
            self.btnApagar.grid(row=3, column=1)
            self.estadoMenu=False
        else:
            self.cerrarMenu()

    def cerrarMenu(self):
            self.estadoMenu=True
            self.lfInicio.destroy()

    def apagar(self):
        self.ventana.quit()
        self.ventana.destroy()
    #-------------------------------------------------------------------------------------------------------------------
    def panelControl(self):
        pass

    def exploradorArchivos(self):
        pass