#CRIANDO FUNÇÃO PARA VERIFICAR SE UM NÚMERO É PALÍNDROMO EM PYTHON

n = input("Insira um número:\n")

def VerificaNumeroPalindromo(n):
    if(int(n) == int(n[::-1])):
        print(f"{n} é um número palíndromo.\n")
    else:
        print(f"{n} não é um número palíndromo.\n")

VerificaNumeroPalindromo(n)

