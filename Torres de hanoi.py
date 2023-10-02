def torHan(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 desde varilla {origen} a varilla {destino}")
        return
    torHan(n-1, or, des, aux)
    print(f"Mover disco {n} desde varilla {origen} a varilla {destino}")
    torHan(n-1, aux, or, des)

# Ejemplo de uso
n = 3  # Cambia el número de discos según tu necesidad
torHan(n, 'A', 'B', 'C')
