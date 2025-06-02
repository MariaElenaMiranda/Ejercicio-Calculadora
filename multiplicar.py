def multiplicar (*arg:int | float) -> None:
    resultado = arg[0]
    for num in arg[1:]:
        resultado *= num
    return resultado