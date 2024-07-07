
num = int(input('Digite um número:'))
a1 = num-1
a2 = num-2
repeticoes = num
sequencia = a1 + a2

while repeticoes != 0:
    repeticoes = repeticoes - 1
    print(sequencia)
    a1 = sequencia - 1
    a2 = sequencia - 2
    sequencia = a1 + a2
    


