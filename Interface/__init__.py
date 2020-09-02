from tkinter import *
from Interface.Login import Login
import os

def comenzar(ventana):
    ventana.mainloop()

def cerrar(ventana):
    ventana.destroy()
    login = Login()
    login.iniciar()


if __name__ == '__main__':
    #os.system("C:\Program Files (x86)\Windows Live\Photo Gallery\WLXPhotoGallery.exe"+" "+"C:/Users/Samuel/Pictures/11A.jpg")
    venta = Tk()
    venta.wm_attributes('-fullscreen','true')
    venta.geometry('1366x768')
    vc = Canvas(venta, width=1366, height=768)
    vc.place(x=0, y=0)
    logo = PhotoImage(file="imagenes/LOGO.png")
    vc.create_image(0, 0, image=logo, anchor="nw")
    btnComenzar = Button(venta, text=" Press to Start ",command=lambda:cerrar(venta))
    btnComenzar.place(x=673,y=600)
    vc.update()
    comenzar(venta)


