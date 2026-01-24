

#IMPLEMENTANDO FUNÇÃO DE FATORIAL EM PYTHON POR RECURSIVIDADE


def CalculaFatorial(x):
    if(x == 1):
        return 1
    else:
        return CalculaFatorial(x - 1) * x
    
number = int(input("Escreva um valor inteiro(0 para sair):\n"))

while(number != 0):
    print(f"O valor do fatorial calculado é: %d\n" % CalculaFatorial(number))
    number = int(input("Escreva um valor inteiro(0 para sair):\n"))