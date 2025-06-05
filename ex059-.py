'''Crie um programa que leia dois valores e mostre um menu na tela:
* Somar
* Multiplicar
* Maior
* Pedir novos numeros
* Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
'''
from time import sleep

print('== Calculeitor ==\n')
soma = 0
mult = 0
maior = 0
n = 0
pare = False
repeat = 0

while pare == False:
  n1 = float(input("Digite o primeiro numero: "))
  n2 = float(input("Digite o segundo numero: "))
  while repeat == 0:
    print("\n\33[34mMenu de opcoes?:\n[1] - soma\n[2] - multiplicacao\n[3] - maior numero\n[4] - Pedir novos numeros\n[5] - Sair do Programa\33[34m]")
    n = int(input('Digite a opção desejada: '))
    if n == 1:
      soma = n1 + n2
      print("A soma de {} + {} = {}".format(n1, n2, soma))
      sleep(1)
      repeat = 0
    elif n == 2:
      mult = n1 * n2
      print("A multiplicação entre {} x {} = {}".format(n1, n2, mult))
      sleep(1)
      repeat = 0
    elif n == 3:
      maior = max(n1,n2)
      print("O maior numero foi: {}".format(n1, n2, maior))
      sleep(1)
      repeat = 0
    elif n == 4:
      pare = False
    elif n == 5:
      print("Encerrando programa em: ")
      for c in range(1,3+1):
        print(c, end=' ')
        sleep(1)
      repeat = 1
      pare = True


# Sera evoluido para um bot)