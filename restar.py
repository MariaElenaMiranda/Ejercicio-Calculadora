def restar(*arg:int | float) -> int | float:
    resultado = arg[0]
    for num in arg[1:]:
        resultado -= num
    return resultado