#CALCULANDO VALORES DA SÉRIE DE FIBONACCI

#EXEMPLO DE IMPLEMENTAÇÃO DA FUNÇÃO POR RECURSIVIDADE


def CalculaFibonacci(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return CalculaFibonacci(n - 1) + CalculaFibonacci(n - 2)
    
a = 0
resultado = 0


while(resultado < 500):
    a += 1
    
    print(f"-%d-" % CalculaFibonacci(a), end='')
    resultado = CalculaFibonacci(a)
