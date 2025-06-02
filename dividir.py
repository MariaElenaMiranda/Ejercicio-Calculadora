def dividir (*arg:int | float) -> int | float:
    try:
        resultado = arg[0]
        for num in arg[1:]:
            resultado /= num
        return resultado
    except ZeroDivisionError:
        print("Error: No puedes dividir por cero")
        return None