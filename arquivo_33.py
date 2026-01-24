#ESSE PROGRAMA IRÁ PERMITIR A VOCÊ CALCULAR O FATORIAL QUANTAS VEZES, VOCÊ DESEJAR

n = int(input("Escolha um número(maior do que 0 e menor do que 16):\n"))
while(n < 0 or n > 16):
    print("O valor está excedido ao limite solicitado pelo programa!\n")
    n = int(input("Escolha um número(maior do que 0 e menor do que 16):\n"))
#IMPLEMENTANDO FUNÇÃO EM PYTHON, PARA CALCULAR FATORIAL DE UM NÚMERO POR RECURSIVIDADE!

def CalculaFatorial(n):
    if(n == 0):
        return 1
    else:
        return n * CalculaFatorial(n - 1)


print(f"O valor do fatorial do número é igual a %d\n" % CalculaFatorial(n))

while(n != 0):
    n = int(input("Escolha um número(maior do que 0 e menor do que 16):\n"))
    if(n < 0 or n > 16):
        print("Valor incorreto!\n")
        exit(1)
    else:

        print(f"O valor do fatorial do número é igual a %d\n" % CalculaFatorial(n))



