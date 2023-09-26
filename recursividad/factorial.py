def fac(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        
        return n * fac(n - 1)


n = 5

r = fac(n)

print(f"El factorial de {n} es {r}")
