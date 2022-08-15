import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    root = tk.Tk() #crear una ventana
    root.title('Catalogo de peliculas')
    root.iconbitmap('img/cp-logo.ico')
    root.resizable(0,0)    #hacer que la ventana no se pueda agrandar o achicar
    
    #barra
    barra_menu(root)

    app = Frame(root = root)
    app.mainloop() #para que se mantenga la ejecucion

if __name__ == '__main__':
    main()