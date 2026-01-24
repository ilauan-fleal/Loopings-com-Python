#EXIBINDO SÉRIE NUMÉRICA EM PYTHON


s = 0

x = int(input("Digite o valor de n:\n"))

y = 1

print("S = " , end="")
for z in range(1, x + 1):
    print(f"{z}/{y}", end="")
    if z < x and x > 1:
        print(" + ", end="")
    else:
        print(".")
    #OPERAÇÕES DE INCREMENTO
    s = s + z/y
    y = y + 2
print(f"A soma total da série obtida foi de {s:.2f}.")



