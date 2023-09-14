import time

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

while True:
    print("Opciones:")
    print("Escribe 'suma' para sumar dos números")
    print("Escribe 'resta' para restar dos números")
    print("Escribe 'multiplicacion' para multiplicar dos números")
    print("Escribe 'division' para dividir dos números")
    print("Escribe 'salir' para salir del programa")

    opcion = input(": ")

    if opcion == "salir":
        break

    if opcion in ("suma", "resta", "multiplicacion", "division"):
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        start_time = time.time()

        if opcion == "suma":
            resultado = suma(a, b)
        elif opcion == "resta":
            resultado = resta(a, b)
        elif opcion == "multiplicacion":
            resultado = multiplicacion(a, b)
        elif opcion == "division":
            resultado = division(a, b)

        end_time = time.time()
        tiempo_procesamiento = end_time - start_time

        print(f"Resultado: {resultado}")
        print(f"Tiempo de procesamiento: {tiempo_procesamiento} segundos")
    else:
        print("Opción no válida. Por favor, elige una operación válida.")
