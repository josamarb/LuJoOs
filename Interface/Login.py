from tkinter import *
from Interface.User import User
from tkinter import messagebox


class Login:

    def __init__(self):
        self.ventana = Tk()
        self.users = [User("Public", "0",False), User("Samuel", "12345",True)]
        self.widgets()


    def widgets(self):
        self.ventana.wm_attributes('-fullscreen','true')
        self.ventana.geometry('1366x768')
        self.usersView()

    def iniciar(self):
        self.ventana.mainloop()

    def usersView(self):
        self.lfUsers = LabelFrame(self.ventana, padx=100, pady=100)
        self.lfUsers.place(x=533, y=300)
        user = self.getUsers()
        column = 1
        self.image = PhotoImage(file="imagenes/profileDefault.png")
        for u in user:
            btnUsuario = Button(self.lfUsers, text=u.name, command=lambda: self.loginUser(u.name),image=self.image)
            btnUsuario.grid(row=7, column=column)
            column = column + 1
            """"
            btnUsuario = Button(lfUsers, text=u.name, command=lambda: self.loginUser(u.name,lfUsers))
            btnUsuario.grid(row=7, column=column)
            column = column + 1
            """
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
            userLogged.iniciar()
        else:
            messagebox.showinfo(message="Password Wrong", title="Password Wrong")

    def getUsers(self):
        return self.users


    def loginUser(self,name):
        self.lfUsers.destroy()
        self.ventana.update()
        password = StringVar()
        self.lflogin = LabelFrame(self.ventana,text=name, padx=100, pady=100)
        self.lflogin.place(x=300, y=300)
        Label(self.lflogin, text='username:').grid(row=4, column=1)
        Label(self.lflogin, text='password:').grid(row=4, column=1)
        lpassword = Entry(self.lflogin, show="*", textvariable=password, width=15).grid(row=4, column=3)
        btnAgregar = Button(self.lflogin, text=" Login ",command=lambda:self.validar(name,password.get()))
        btnAgregar.grid(row=7, column=1)

        btnRetroceder = Button(self.lflogin, text=" Go back ", command=lambda: self.goBack())
        btnRetroceder.grid(row=8, column=1)

    def goBack(self):
        self.lflogin.destroy()
        self.ventana.update()
        self.usersView()

    def apagar(self):
        self.ventana.quit()
        self.ventana.destroy()