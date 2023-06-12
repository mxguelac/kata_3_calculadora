import tkinter as tk
from tkinter.font import Font

class Display(tk.Frame):
    def __init__(self, location):
        super().__init__(location, width= 272, height= 50)
        self.pack_propagate(False)
        self.label = tk.Label(self, background='#000000', text='Prueba', foreground='#FFFFFF',
                              anchor=tk.E, padx=8,
                              font=Font(family='Arial', size='40'))
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def typing(self, text):
        self.label.config(text=text)



