'''055 - Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos'''
print("== Analisador de pesos ==")
maior = 0
menor = 0
for p in range(0, 5 + 1)
  peso = float(input("Informe o peso da {}ª pessoa".format(p)))
  if p == 1:
    maior = p
    menor = p
  else:
      if peso > maior:
        maior = peso
      if peso < menor:
        menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('\nO menor peso lido foi de {}kg'.format(maior))