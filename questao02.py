print('Seja bem vindo ao sistema somatório de valores da Brightside, nos disponibilize dois valores e realizaremos a soma. Mas primeiramente digite 1 para iniciar o programa e 0 para encerrá-lo e exibir a soma')
desejacontinuar = int(input('Deseja iniciar o programa?'))
while(desejacontinuar != 0):
    valor1 = int(input('Digite o primeiro valor:'))
    valor2 = int(input('Digite o segundo valor:'))
    soma = valor1 + valor2
    desejacontinuar = int(input('Deseja encerrar o programa e exibir a soma?'))
    print('O valor da soma é:', soma)
    print('Programa encerrado')