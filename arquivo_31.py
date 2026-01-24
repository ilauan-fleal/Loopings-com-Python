

n = int(input("Escolha um número:\n"))

#IMPLEMENTANDO FUNÇÃO EM PYTHON, PARA CALCULAR FATORIAL DE UM NÚMERO POR RECURSIVIDADE!



def CalculaFatorial(n):
    if(n == 0):
        return 1
    else:
        return n * CalculaFatorial(n - 1)


print(f"O valor do fatorial do número é igual a %d\n" % CalculaFatorial(n))

