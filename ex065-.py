'''065 - Crie um programa que leia varios numeros inteiros pelo teclad. No final, mostre a media entre 
todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores'''
print("== Analisador de numeros ==\n")
c = 0
media = 0
soma = 0
cont = 0
maior = 0
menor = 0
while c == 0:
  ncond = int(input('Quantos numeros inteiros deseja calcular?: '))
  for c in range(0, ncond + 1):
    n = int(input('Digite o numero: '))
    soma += n
    cont += 1
  media = soma / cont
  print("A media dos termos digitados foi de: {}".format(media))
  print('O maior numero foi: {}'.format(max(n)))
  print('O menor numero foi: {}'.format(min(n)))
  stop = str(input('Desejar repetir o programa? [s/n]')).upper()
  if stop == 'Ss':
    c = 1
  else:
    print('Repetindo...\n')