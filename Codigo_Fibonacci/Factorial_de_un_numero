def factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

num = 10 # Ingresa el número para el cual deseas calcular el factorial

# Llama a la función factorial y se muestra el resultado
resultado = factorial(num)
if isinstance(resultado, int):
    print(f"El factorial de {num} es {resultado}")
else:
    print(resultado)
