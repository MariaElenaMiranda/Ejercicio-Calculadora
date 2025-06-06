from sumar import sumar
from restar import restar
from multiplicar import multiplicar
from dividir import dividir

class Calculadora:
    def __init__(self, *args:int | float) -> None:
        self.valores = args

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