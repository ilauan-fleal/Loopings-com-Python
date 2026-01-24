
x = int(input("Insira um determinado valor:\n"))

def VerificaValor(x):

    if(x == 1 or x == 2):
        print(f"O número {x} é primo, e foram feitas 0 divisões foram executadas.\n")
    elif(x % 2 == 0):
        print(f"O número {x} não é primo e foi executada 1 divisão para descobrir isso.\n")
    
    else:
        contagem = 0       
        prime = True
        for n in range(3, x, 2):
            print(f"%d / %d" % (x,n))
            
            contagem = contagem + 1
            if(x % n == 0):
                prime = False
                break
            
        if prime:
            print(f"O número {x} é primo e foram efetuadas {contagem} divisões para descobrir isso.\n")
            

        else:
            print(f"O número {x} não é primo e foram efetuadas {contagem} divisões para descobrir isso.\n")



VerificaValor(x)