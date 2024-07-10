num = int(input('Digite o numero:'))

numero = num
soma = 0

while num > 0:
    digito = num % 10
    soma += digito
    num //= 10
print(f"A soma dos dígitos de {numero} é {soma}")
