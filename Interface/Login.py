from tkinter import *
from Interface.User import User
from tkinter import messagebox
from Archivos.lectorJSON import lectorJSON

class Login:

    def __init__(self):
        self.ventana = Tk()
        self.lj = lectorJSON()
        self.users = self.lj.leerJSON()
        self.widgets()


    def widgets(self):
        self.ventana.wm_attributes('-fullscreen','true')
        self.ventana.geometry('1366x768')
        self.usersView()

    def iniciar(self):
        self.ventana.mainloop()

    def usersView(self):
        self.lfUsers = LabelFrame(self.ventana, padx=100, pady=100)
        self.lfUsers.place(x=450, y=280)
        user = self.getUsers()
        column = 1
        self.images = []
        for u in user:
            self.images.append(PhotoImage(file=u.imagePath))
            btnUsuario = Button(self.lfUsers, text="", command=lambda u=u: self.loginUser(u.name),image=self.images[column-1])
            btnUsuario.grid(row=7, column=column)
            Label(self.lfUsers,text=u.name).grid(row=8, column=column)
            column = column + 1

        self.imageOff = PhotoImage(file="imagenes/off.png")
        btnOff = Button(command=self.apagar, image=self.imageOff)
        btnOff.place(x=0,y=0)

    def validar(self,name, password):
        users = self.getUsers()
        userLogged = None
        for user in users:
            if user.name == name and password == user.password:
                userLogged = user
        if userLogged:
            self.ventana.destroy()
            userLogged.setUsuarios(self.users)
            userLogged.iniciar()
        else:
            messagebox.showinfo(message="Password Wrong", title="Password Wrong")

    def getUsers(self):
        return self.users


    def loginUser(self,name):
        user = self.getUser(name)
        if len(user.getPassword())==0:
            self.ventana.destroy()
            user.iniciar()
        else:
            self.lfUsers.destroy()
            self.ventana.update()
            password = StringVar()
            self.lflogin = LabelFrame(self.ventana,text=name, padx=100, pady=100)
            self.lflogin.place(x=450, y=280)
            Label(self.lflogin, image=self.images[self.users.index(user)]).grid(row=1, column=1)
            Label(self.lflogin, text='password:').grid(row=2, column=1)
            lpassword = Entry(self.lflogin, show="*", textvariable=password, width=15).grid(row=2, column=2)
            btnLogear = Button(self.lflogin, text=" Login ",command=lambda:self.validar(name,password.get()))
            btnLogear.grid(row=3, column=1)

            btnRetroceder = Button(self.lflogin, text=" Go back ", command=lambda: self.goBack())
            btnRetroceder.grid(row=4, column=1)

    def getUser(self,name):
        for u in self.users:
            if name==u.name:
                return u
        return None
        
    def goBack(self):
        self.lflogin.destroy()
        self.ventana.update()
        self.usersView()

    def apagar(self):
        self.ventana.quit()
        self.ventana.destroy()