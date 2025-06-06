from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir

class Calculadora:
    def __init__(self, *args:int | float) -> None:
        self.valores = args

    #Metodos para realizar las operaciones
    def suma(self) -> None:
        resultado = sumar(*self.valores)
        print(f"Resultado = {resultado}")

    def resta(self) -> None:
        resultado = restar(*self.valores)
        print(f"Resultado = {resultado}")

    def multiplica(self) -> None:
        resultado = multiplicar(*self.valores)
        print(f"Resultado = {resultado}")

    def divide(self) -> None:
        resultado = dividir(*self.valores)
        print(f"Resultado = {resultado}")


    #Metodo set
    def set_valores(self,*args):
        self.valores = args