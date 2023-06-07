import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mi primera pantalla tkinter')
        self.geometry('800x600+400+200')
        self.label = tk.Label(self, text = '', bd =2, relief=tk.RAISED)
        self.label.pack()
        self.valor_nombre = tk.StringVar()
        nombre = tk.Entry(self, textvariable=self.valor_nombre)
        nombre.pack()
        boton = tk.Button(self, text='Púlsame', command=self.imprimir_saludo)
        boton.pack()
    
    def imprimir_saludo(self):
        self.label.config(text=f'Hola, {self.valor_nombre.get()}')
    
Ventana().mainloop()