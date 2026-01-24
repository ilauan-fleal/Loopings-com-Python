#ESCREVENDO NOVAMENTE PROGRAMA PARA CALCULAR O FATORIAL DE UM NÚMERO

n = int(input("Escreva um número inteiro:\n"))

def DeterminaFatorial(n):
    if(n == 0):
        return 1
    else:
        return n * DeterminaFatorial(n-1)
    
resultado = DeterminaFatorial(n)

print(f"O valor do fatorial calculado é igual a %d\n" % resultado)