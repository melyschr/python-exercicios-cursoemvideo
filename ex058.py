'''058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero entre 0 e 10. 
Só que agora o jogador vai tentar divinhar até acertar mostrando final quantos palpites foram necessarios para vencer'''
import random
print("== Jogo de Adivinhação 2.0 ==\n")
c = 0
soma = 0
comp = random.randint(0,10 + 1)
while c == 0:
  user = int(input("Digite um numero inteiro entre 0 e 10: "))
  if user == comp:
    print("Parabens! Você advinhou o numero escolhido que foi {}".format(comp))
    print("Foram necessarias {} palpites para acertar7".format(soma))
    c = 1
  else:
    print("Errou! Tente novamente")
    soma += 1
    c = 0
