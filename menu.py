from os import system
from calculadora import Calculadora
from math import trunc

#Función para crear el menu
def menu() -> None:
    system("clear")
    print("¡Bienvenido/a a la app calculadora!\n")
    print("Instrucciones:\n" +
        "- Selecciona la operación que deseas realizar\n" +
        "- Ingresa los números a operar\n")

    opciones = ["1.- Sumar", "2.- Restar", "3.- Multiplicar", "4.- Dividir", "5.- Salir"]
    for opcion in opciones:
        print(opcion)

# #Función para convertir los numeros (str) en una lista de numeros (int | float)
# def convertir_numero(texto_numeros_str:str) -> list[int | float]:
#     lista_numeros_str = texto_numeros_str.split(",")
#     lista_numeros_final = []
#     for num in lista_numeros_str:
#         numero_limpio = num.strip()
#         try:
#             numero = float(numero_limpio)
#             if numero.is_integer():
#                 numero = int(numero)
#             lista_numeros_final.append(numero)
#         except ValueError:
#             raise ValueError(f"Valor inválido: {numero_limpio}")
#     return lista_numeros_final

def lista_numeros() -> list[int | float]:
    lista = []
    while True:
        try:
            numero = float(input('Ingresa un número: '))
            if numero:
                lista.append(numero)
        except ValueError:
            print('Ingresa solo números enteros o decimales')
        otro = input('Enter para continuar, "salir" para cortar: ').lower()
        if otro == 'salir':
            return lista

if __name__ == "__main__":
    menu()

    #Inputs:
    opcion = int(input("Ingresa la opción aquí: "))
    listado_numeros = lista_numeros()

    #Instancia y condicional para seguir operando la calculadora
    calculator = Calculadora(*listado_numeros)
    seguir_operando = True

    while(seguir_operando):
        match(opcion):
            case 1: #suma
                calculator.suma()
            case 2:
                calculator.resta()
            case 3:
                calculator.multiplica()
            case 4:
                calculator.divide()
            case 5:
                print("\n¡Hasta pronto!")
                seguir_operando = False
            case _:
                print(f"Opción no válida:'{opcion}'\nIntentalo nuevamente...\n")
