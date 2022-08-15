import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = 'database/peliculas.db'   #aca colocamos una ruta porque cuando trabajamos con sqlite si la BD o el archivo de la BD no existe lo que va a hacer es crearlo, 
                                                    #entonces como lo va a crear si no existe entonces vamos a colocar la ruta donde va a crear o concetarse a esa BD. Si existe simplemente
                                                    #se conecta y si no existe lo crea
        self.conexion = sqlite3.connect(self.base_datos)    #realizo la conexion a nuestra base de datos (self.base_datos)
        self.cursor = self.conexion.cursor()    #escribir o realizar alguna modificacion dentro de la base de datos
    

    def cerrar(self):
        self.conexion.commit()      #abrir la conexion
        self.conexion.close()       #cerrar la conexion