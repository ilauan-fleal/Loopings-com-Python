
#PROGRAMA PARA VERIFICAR EXISTÊNCIA DE NÚMEROS PRIMOS EM PYTHON

x = int(input("Digite um valor:\n"))

def VerificaValorPrimo(x):
    primo = True
    for i in range(2, x):
        if(x % i == 0):
            primo = False
            print(f"{x} não é um valor primo!\n")
            print("Divisores:\n")
            print([k for k in range(1, x//2 + 1) if x % k == 0])
            break
    if(primo):
        print(f"{x} é primo!\n")
        
#CHAMADA DA FUNÇÃO

    
VerificaValorPrimo(x)


