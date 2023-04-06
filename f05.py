def funcao_detecta(n):
    if(n % 2 == 0):
        return "E Par"
    else:
        return 'E impar'
print (funcao_detecta(int(input('Entre com um numero'))))