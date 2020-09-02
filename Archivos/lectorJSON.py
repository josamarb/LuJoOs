from Interface.User import User
import json
class lectorJSON:

    def __init__(self):
        pass

    def leerJSON(self):
        users = []
        #l = open('/DB/usuarios.txt')
        with open('C:\\Users\\Samuel\\Documents\\SamPython\\LuJo\\Archivos\\DB\\userJson.json','r') as file:
            data = json.load(file)

            for user in data.get('users'):
                nombre = user.get("name")
                password = user.get("password")
                if user.get("admin") == "True":
                    admin = True
                else:
                    admin = False
                imgPath = user.get("imagePath")
                users.append(User(nombre,password,admin,imgPath))
            for u in users:
                if u.admin:
                    u.setUsuarios(users)
        return users