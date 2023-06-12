from romannumbers import *

class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif type(entrada) == str:
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumberError('Debe incializarse con un entero o romano valido')
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)

    @property
    def simbolo(self):
        return self._simbolo

    @simbolo.setter
    def simbolo(self, entrada):
        self._simbolo = entrada
        self._numero = romano_a_entero(entrada)

    """
    metodos mágicos para lógica
    """
    def __eq__(self, other):
        other = self.__to_roman(other)
        return self.numero == other.numero
    
    def __req__(self, other):
        return self.__eq__(other)
    
    def __lt__(self, other):
        other = self.__to_roman(other)
        return self.numero < other.numero
    
    def __le__(self, other):
        other = self.__to_roman(other)
        return self.numero <= other.numero
    
    def __gt__(self, other):
        other = self.__to_roman(other)
        return self.numero > other.numero
    
    def __ge__(self, other):
        other = self.__to_roman(other)
        return self.numero >= other.numero
    
    def __ne__(self, other):
        other = self.__to_roman(other)
        return self.numero != other.numero
    
    
    



    """
    metodos mágicos para aritmética
    """
    def __to_roman(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        return otro
    
    def __mul__(self, otro):
        if not isinstance (otro, RomanNumber):
            otro = RomanNumber (otro)

        resultado = self.numero * otro.numero

        return RomanNumber(resultado)
    
    def __rmul__ (self, otro):
        return self.__mul__(otro)
    
    def __add__(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado = self.numero + otro.numero
        return RomanNumber(resultado)
    
    def __radd__(self, otro):
        return self.__add__(otro)
    
    def __floordiv__(self, otro):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        resultado = self.numero // otro.numero
        return RomanNumber(resultado)
    
    def __rfloordiv__(self, otro):
        otro = RomanNumber(otro)
        return otro.__floordiv__(self)
        
        #Otra forma de cambiar el orden
        self, otro = otro, self
        return self.__floordiv__(otro)
       
        #Otra forma de cambiar el orden
        aux= otro
        otro= self
        self = aux
    
    def __sub__(self, otro ):
        if not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)
        
        return RomanNumber(self.numero - otro.numero)
    
    def __rsub__(self, otro):
        otro = self.__to_roman(otro)

        return otro.__sub__(self)

    def __pow__(self, otro):
        otro = self.__to_roman(otro) 
        return RomanNumber(self.numero ** otro.numero)
    
    def __rpow__(self, otro):
        otro = self.__to_roman(otro)
        return otro.__pow__(self)
    
        """
        metodos mágicos para representación
        """
    def __repr__(self):
        return f"{self.numero} - {self.simbolo}"

    def __str__(self):
        return self.__repr__()

   