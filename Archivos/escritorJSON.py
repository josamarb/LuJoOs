import json

class escritorJSON:

    def __init__(self):
        pass

    def escribirUsuarios(self,users):
        datos = []
        for u in users:
            dato = {
                "name": u.getName(),
                "password": u.getPassword(),
                "admin": str(u.admin),
                "imagePath": u.imagePath,
            }
            datos.append(dato)
        usuarios = {"users": datos}
        #u = open("C:\\Users\\Samuel\\Documents\\SamPython\\LuJo\\Archivos\\DB\\userJson.json", "w")
        with open('C:\\Users\\Samuel\\Documents\\SamPython\\LuJo\\Archivos\\DB\\userJson.json', 'w') as file:
            json.dump(usuarios, file)
