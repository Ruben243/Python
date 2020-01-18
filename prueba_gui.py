# importamos la libreria
import tkinter


# creamos la clase App con el frame de tkinter
class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # funcion que crea la ventana y añade los botones
    def create_widgets(self):
        # constructor del boton
        self.hi_there = tkinter.Button(self)
        # primer boton con texto
        self.hi_there["text"] = "Hola mundo\n(click me)"
        # al hacer click llama a la funcion say_hi
        self.hi_there["command"] = self.say_hi
        # posicion boton
        self.hi_there.pack(side="top")
        # segundo boton al hacer click cierra el programa
        self.quit = tkinter.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # posicion del boton
        self.quit.pack(side="bottom")

    # funcion que imprime texto
    def say_hi(self):
        print("hola a todos")


root = tkinter.Tk()
# titulo de la ventana
root.title('Probando tkinter')
# tamaño de la ventana
root.minsize(1000, 400)
app = App(master=root)
app.mainloop()
