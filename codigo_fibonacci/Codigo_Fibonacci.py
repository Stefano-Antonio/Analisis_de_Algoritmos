def fibonacci(n):

    fibo = [0, 1] #se crea la lista con los primeros dos valores
    for i in range(2, n + 1):  #se crea el bucle for
        fibo_sig = fib[i - 1] + fib[i - 2]   #se calcula el siguiente valor de la lista

        fibo.append(fibo_sig) #asigna el resultado de la operacion a la siguiente posicion de la lista
    return fibo[n]   #regresa el valor en la posicion de la lista deseada

n = 15  # Cambia este valor para obtener el término deseado
resultado = fibonacci(n)  #asigna el valor a la variable resultado
print(f"El término {n}-ésimo de Fibonacci es {resultado}")
