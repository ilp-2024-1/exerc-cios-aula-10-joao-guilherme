import random

numeroaleatorio = random.randint(1,100)
palpite = int(input("Digite 0 para inicar o jogo de palpites!"))
while palpite != numeroaleatorio:
    palpite = int(input('Dê o seu palpite:'))
print('Você acertou!')
print('Programa encerrando em 3, 2, 1...')


