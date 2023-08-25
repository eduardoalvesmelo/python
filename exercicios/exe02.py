# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = float(input("Informe o terceiro numero: "))

r1 = (2 * n1) + (n2 / 2)
r2 = (3 * n1) + n3
r3 = n3 *n3 * n3

print("O produto do dobro do primeiro com metade do segundo: {:.2f}".format(r1))
print("A soma do triplo do primeiro com o terceiro: {:.2f}".format(r2))
print("O terceiro elevado ao cubo: {:.2f}".format(r3))
