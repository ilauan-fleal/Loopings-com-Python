#ESSE PROGRAMA DEVERÁ LER UMA QUANTIDADE INDETERMINADA DE NÚMEROS POSITIVOS!

#E DETERMINAR QUANTOS DELES ESTÃO EM INTERVALOS ESPECÍFICOS!


number = 0

ValoresNoIntervalo0a25 = 0

ValoresNoIntervalo26a50 = 0

ValoresNoIntervalo51a75 = 0

ValoresNoIntervalo76a100 = 0

ValoresNoIntervalode100emdiante = 0

while(number >= 0):
    print("Digite um número(sempre maior do que 0 ou o programa será encerrado):\n")
    number = int(input())

    if(number > 0 and number < 25):
        ValoresNoIntervalo0a25 += 1
    elif(number > 26 and number < 50):
        ValoresNoIntervalo26a50 += 1
    elif(number > 51 and number < 75):
        ValoresNoIntervalo51a75 += 1
    elif(number > 76 and number < 100):
        ValoresNoIntervalo76a100 += 1

    else:
        ValoresNoIntervalode100emdiante += 1
        
print(f"A quantidade total de números no intervalo de 0 a 25 é igual {ValoresNoIntervalo0a25}\n")    
print(f"A quantidade total de números no intervalo de 26 a 50 é igual {ValoresNoIntervalo26a50}\n")    
print(f"A quantidade total de números no intervalo de 51 a 75 é igual a {ValoresNoIntervalo51a75}\n")
print(f"A quantidade total de números no intervalo de 76 a 100 é igual a {ValoresNoIntervalo76a100}\n")