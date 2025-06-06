from os import system
from calculadora import Calculadora
from math import trunc

#Función para crear el menu
def menu() -> int:
    system("clear")
    print("¡Bienvenido/a a la app calculadora!\n")
    print("Instrucciones:\n" +
        "- Selecciona la operación que deseas realizar\n" +
        "- Ingresa los números a operar\n")

    opciones = ["1.- Sumar", "2.- Restar", "3.- Multiplicar", "4.- Dividir", "5.- Salir"]
    for opcion in opciones:
        print(opcion)
    opcion = int(input("Ingresa la opción aquí: "))
    return opcion

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
                if numero.is_integer():
                    numero = int(numero)
                lista.append(numero)
        except ValueError:
            print('Ingresa solo números enteros o decimales')
        otro = input('Enter para continuar, "salir" para cortar: ').lower()
        if otro == 'salir':
            return lista

if __name__ == "__main__":
    seguir_operando = True

    while(seguir_operando):
        #Instancia y condicional para seguir operando la calculadora
        opcion = menu()
        calculator = Calculadora()

        match(opcion):
            case 1: #suma
                system("clear")
                listado_numeros = lista_numeros()
                calculator.set_valores(*listado_numeros)
                calculator.suma()
                enter = input("\nPresiona Enter para continuar...")
            case 2:
                system("clear")
                listado_numeros = lista_numeros()
                calculator.set_valores(*listado_numeros)
                calculator.resta()
                enter = input("\nPresiona Enter para continuar...")
            case 3:
                system("clear")
                listado_numeros = lista_numeros()
                calculator.set_valores(*listado_numeros)
                calculator.multiplica()
                enter = input("\nPresiona Enter para continuar...")
            case 4:
                system("clear")
                listado_numeros = lista_numeros()
                calculator.set_valores(*listado_numeros)
                calculator.divide()
                enter = input("\nPresiona Enter para continuar...")
            case 5:
                system("clear")
                print("\n¡Hasta pronto!")
                seguir_operando = False
            case _: #Default
                system("clear")
                print("\nDebes ingresar una opción válida, vuelve a intentarlo")
                enter = input("\nPresiona Enter para continuar...")
