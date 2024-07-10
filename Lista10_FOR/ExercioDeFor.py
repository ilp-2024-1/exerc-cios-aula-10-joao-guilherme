#Questão01

for i in range(2, 12 +1 , 2):
    print(i, end = (","))

    #Questão02

numero = int(input('Digite um numero:'))

for i in range(1, numero+1):
    print(i)
print('Programa encerrado')

#Questão 03
var_1 = int(input("Digite o pireimeiro valor inteiro positivo: "))
var_2 = int(input("Digite o segundo valor inteiro positivo:"))

for i in range(var_1, var_2 + 1):
    print(i, end = ",")
print("Fim do Programa")

#Questão04

num1 = int(input('Digite o numero:'))
num2 = int(input('Digite o segundo numero:'))

for i in range(num1+1, num2):
    print(i)
print('Programa encerrado')

#Questão06

num1 = int(input('Digite o valor inicial:'))
num2 = int(input('Digite o valor final:'))
num3 = int(input('Digite o incremento:'))

for i in range(num1, num2, num3):  
    tempf = i*1.8+32
    print(f"{i}°C = {tempf}°F")
print('Programa encerrou')

