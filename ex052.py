'''052 - Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo'''
# Considere que numero primos são divisiveis por 2
print("== Identificador de numero primos ==\n")

n = int(input("Digite um numero inteiro: "))
tot = 0 # saber numero de divisiveis
for c in range (1, n + 1):
  if n % c == 0:
    print('\33[31m', end=" ")
    tot += 1
  else:
    print('\33[34m', end=" ")
  print('{}'.format(c), end=" ")
print('\n\33[39m O numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
  print('É por isso ele é PRIMO')
else:
  print('É por isso ele é NÃO É PRIMO')
