'''Faça um programa que leia um numero qualquer e mostre seu fatorial
* 5x4x3x2x1 = 20'''
from math import factorial
from time import sleep
print("== Calculadora de Fatoriais ==")
c = 0
while c == 0:
  numero = int(input('Digite um numero qualquer: '))
  fatorial = factorial(numero)
  print("O fatorial de {} é igual á {}".format(numero, fatorial))
  cond = str(input("Deseja calcular outro numero? [S/N]: "))
  if cond != 'Ss':
    print('Encerrando...')
    sleep(2)
    c = 1
# A continuar....
