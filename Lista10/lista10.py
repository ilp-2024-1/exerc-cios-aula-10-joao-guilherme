# questão 07

a = int(input("Escolha um numero de 1 até 1000: "))
b = 2

while(b < a):
    
    if a == 3 or a == 5:
        print("Ele é um numero primo")
        break
    elif a % b == 0 or a % 3 == 0 or a % 5 == 0:
        print("Não é primo")
        break
    else:
        print("Ele é um numero primo")
        
        break
        a = int(input("Escolha um numero de 1 até 1000: "))
    
print("Fim do programa")




    



