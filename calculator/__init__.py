import tkinter as tk
from .controls import Display, CalcButton, KeyBoard
from cromannumbers import RomanNumber, RomanNumberError


WIDTH = 272
HEIGHT = 300

operaciones = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'x': lambda a, b: a * b,
    '÷': lambda a, b: a / b
}

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculadora')
        self.geometry(f'{WIDTH}x{HEIGHT}')

        self.reset()

        self.display = Display(self)
        self.display.pack()

        KeyBoard(self, self.clic ).pack()

        self.display.typing('Probando')
    
    def reset(self):
            self.value = ''
            self.op1 = self.op2 = self.operation = None
            self.equal = False

    """ CalcButton(self, self.clic, '1').pack()
        CalcButton(self, text='2', tiny_wire=self.clic).pack()
        CalcButton(self, text='3', tiny_wire=self.clic).pack()
        CalcButton(self, text='4', tiny_wire=self.clic).pack()

        """
    def clic(self, tecla):
        try:
            if tecla == 'AC':
                self.reset()
        
            elif tecla in operaciones:
                if self.operation:
                    if self.equal:
                        resultado = RomanNumber(self.value)
                    else:
                        self.op2 = RomanNumber(self.value)
                        resultado = operaciones[self.operation](self.op1, self.op2)
                    self.op1 = resultado
                    self.op2 = None
                    self.value = resultado.simbolo
                else:
                    self.op1 = RomanNumber(self.value)
                self.operation = tecla
            elif tecla == '=': 
                if self.equal:
                    resultado = operaciones [self.operation](RomanNumber(self.value), self.op2)
                else: 
                    self.op2 = RomanNumber(self.value)
                    resultado = operaciones[self.operation](self.op1, self.op2)
                self.value = resultado.simbolo
            else:
                if self.equal:
                    self.reset()
        
                if self.operation is not None and self.op2 is None:
                    self.value = ''
                    self.op2 = ''

                self.value += tecla
            
            self.display.typing(self.value)

            self.equal = (tecla == '=')
        except RomanNumberError:
            self.value = 'E'
            self.display.typing(self.value)
            self.reset()
