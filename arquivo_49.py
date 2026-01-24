
x = int(input("Insira um valor:\n"))

def NumeroPrimo(x):
    divisores = 0
    for y in range(1, x + 1):
        if(x % y == 0):
            divisores += 1
    return divisores

lista = [z for z in range(1,x)]

Nprimos = [1]

for r in lista:
    divisores = NumeroPrimo(r)
    if divisores == 2:
        
        Nprimos.append(r)

print(Nprimos)
