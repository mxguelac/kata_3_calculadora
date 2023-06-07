import tkinter as tk

class Display(tk.Frame):
    def __init__(self, location):
        super().__init__(location, width= 272, height= 50)
        self.pack_propagate(False)
        label = tk.Label(self, background='#000000', text='Prueba', foreground='#FFFFFF')
        label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



