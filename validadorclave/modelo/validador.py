# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError
from errores import NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError

calisto_mayus = ["C", "A", "L", "I", "S", "T", "O"]
calisto_minus = ["c", "a", "l", "i", "s", "t", "o"]

class ReglaValidacion(ABC):
    @abstractmethod
    def es_valida(self):
        pass
    
    def validar_longitud(self):
        pass
    
    def contiene_mayuscula(self):
        pass
    
    def contiene_minuscula(self):
        pass
    
    def contiene_numero(self):
        pass
    
class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, clave: str):
        self.clave = clave
        super().__init()
        
    def validar_longitud(self) -> bool:
        try:
            if len(self.clave) >= 8:
                return True
            return False
        except NoCumpleLongitudMinimaError:
            print("La longitud de la clave no cumple la mínima requerida.")
    
    def contiene_mayuscula(self) -> bool:
        try:
            for c in self.clave:
                if c in calisto_mayus:
                    return True
            return False
        except NoTieneLetraMayusculaError:
            print("La clave ingresada no contiene al menos una letra mayúscula.")
        
    def contiene_minuscula(self) -> bool:
        try:
            for c in self.clave:
                if c in calisto_minus:
                    return True
            return False
        except NoTieneLetraMinusculaError:
            print("La clave ingresada no contiene al menos una letra minúscula.")    
        
    def contiene_numero(self) -> bool:
        try:
            for c in self.clave:
                if type(c) == int:
                    return True
            return False
        except NoTieneNumeroError:
            print("La clave ingresada no contiene al menos un número.")

    def contiene_caracter_especial(self) -> bool:
        try:
            for c in self.clave:
                if c in ["@", "_", "#", "$", "%"]:
                    return True
            return False
        except NoTieneCaracterEspecialError:
            print("La clave ingresada no contiene un carácter especial.")
                        
    def es_valida(self):
        if self.validar_longitud() and self.contiene_mayuscula() and self.contiene_minuscula() and self.contiene_caracter_especial():
            print(f"La clave {self.clave} es válida bajo la validación Ganímedes.")
            return True
        return False
            
class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, clave: str):
        self.clave = clave
        super().__init()
    
    def validar_longitud(self) -> bool:
        try:
            if len(self.clave) >= 6:
                return True
            return False
        except NoCumpleLongitudMinimaError:
            print("La longitud de la clave no cumple la mínima requerida.")

    def contiene_numero(self) -> bool:
        try:
            for c in self.clave:
                if type(c) == int:
                    return True
            return False    
        except NoTieneNumeroError:
            print("La clave ingresada no contiene al menos un número.")
            
    def contiene_calisto(self):
        mayusculas = []
        try:
            for c in self.clave:
                if c in calisto_mayus:
                    mayusculas.append(c)
                if len(mayusculas) >= 2 and len(mayusculas < 6):
                    return True
            return False
        except NoTienePalabraSecretaError:
            print("La clave ingresada no contiene la palabra secreta con, al menos, dos letras mayúsculas.")
        
class Validador:
    def __init__(self, regla: ReglaValidacion, clave: str):
        self.regla = regla
        self.clave = clave

    def es_valida(self):
        if self.regla.es_valida():
            print("La clave ingresada cumple todos los requisitos, es válida.")
            return True
        print("La clave no cumple todos los requisitos, no es válida.")
        return False