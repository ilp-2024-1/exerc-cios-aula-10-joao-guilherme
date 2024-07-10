#Questão 01 

n1 = 0

while( n1 <=1000):
    print(n1)
    n1= n1 +1

#Questão 02

print('Seja bem vindo ao sistema somatório de valores da Brightside, nos disponibilize dois valores e realizaremos a soma. Mas primeiramente digite 1 para iniciar o programa e 0 para encerrá-lo e exibir a soma')
desejacontinuar = int(input('Deseja iniciar o programa?'))
while(desejacontinuar != 0):
    valor1 = int(input('Digite o primeiro valor:'))
    valor2 = int(input('Digite o segundo valor:'))
    soma = valor1 + valor2
    desejacontinuar = int(input('Deseja encerrar o programa e exibir a soma?'))
    print('O valor da soma é:', soma)
    print('Programa encerrado')

# Questão 03

senha =  input("Digite sua senha: ")
flag =  "carlinhos"

while(senha !=flag):
    if(senha != flag):
        senha = input("Digite sua senha novamente: ")
print("Fim do programa")

#Questão 04
import random

numeroaleatorio = random.randint(1,100)
palpite = int(input("Digite 0 para inicar o jogo de palpites!"))
while palpite != numeroaleatorio:
    palpite = int(input('Dê o seu palpite:'))
print('Você acertou!')
print('Programa encerrando em 3, 2, 1...')


#05

a =  int(input("Digite um valor inteiro: "))
fatorial = 1
x = 1

while(x <= a ):
    fatorial = fatorial * x
    x += 1
print(fatorial)

#Questao 06

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
    
#Questão 08
num = int(input('Digite o numero:'))

numero = num
soma = 0

while num > 0:
    digito = num % 10
    soma += digito
    num //= 10
print(f"A soma dos dígitos de {numero} é {soma}")