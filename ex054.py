'''054 -  Crie um programa que leia o ano de nascimento de 7 pessoas. 
No final mostre, quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores (considerando 21 = maior)'''
print(" = Identificador de maioridade =\n")
from datetime import date

contmaior = 0
contmenor = 0
anoatual = date.today().year

for c in range(1, 7 + 1):
  ano = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
  idade = anoatual - ano
  if idade >= 21:
    contmaior += 1
  else:
    contmenor =+ 1
print("Das 7 pessoas, apenas {} atingiram a maioridade.".format(contmaior))
print("\n Das 7 pessoas, apenas {} são menores.".format(contmaior))