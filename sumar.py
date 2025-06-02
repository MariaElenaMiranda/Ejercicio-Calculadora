def sumar (*arg:int | float) -> int | float:
    resultado = 0
    for num in arg:
        resultado += num
    return resultado