def dividir (num1:int | float, num2:int | float) -> None:
    if num2 == 0:
        print(f"Error: No puedes dividir por cero")
        return
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} * {num2} = {resultado}")