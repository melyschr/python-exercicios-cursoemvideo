'''046 - Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artificio, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles'''
import time as t

c = 0
print("Contagem regressiva para o ano novo em...")
for c in range (10,0,-1):
  print(c)
  t.sleep(1)
print("FELIZ ANO NOVO!")