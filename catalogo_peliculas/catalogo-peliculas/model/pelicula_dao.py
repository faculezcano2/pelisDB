
from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()     #se conecta a la base de datos y una vez que hace esa conexion, en la carpeta 'database' se realiza una BD   y se realiza a conexion

    sql ='''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''       #creamos codigo sql para ejecutar dentro de la conexion o dentro de la base de datos 

    try:
        conexion.cursor.execute(sql) #ejecutamos el codigo sql usando el cursor de la clase conexionDB
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConexionDB()

    sql='DROP TABLE peliculas'     #creamos el codigo sql para eliminar la tabla 
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar registro'
        mensaje = 'La tabla de la base de datos se borro con exito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar registro'
        mensaje= 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Peliculas[{self.nombre}, {self.duracion}, {self.genero}]'



def guardar(pelicula):      #guardar una pelicula en la BD
    conexion = ConexionDB()   #primero genero la conexion

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""  #codigo sql a enviar

    try:
        conexion.cursor.execute(sql)        #ejecuta el codigo sql
        conexion.cerrar()                   #cierra la conexion
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla peliculas no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)       #msj de error si no existe la tabla 


def listar():

    conexion = ConexionDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo,mensaje)

    return lista_peliculas


def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se pudo editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se ha podido eliminar el registro'
        messagebox.showerror(titulo, mensaje)