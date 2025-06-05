'''051 - Desenvolva um programa que leia o 
primeiro termo ea razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão'''
import time as t
import matplotlib.pyplot as plt
import numpy as np

# PROGRESSÃO ARITMETICA
print("~ Progressão aritimetica ~\n")
primeiroTermo = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA (numero inteiro): "))
n = int(input("Quantos termos deseja exibir: "))
ultimoTermo = primeiroTermo + (n - 1) * razao
ultimoTermo += 1

print("\nAqui esta os {} primeiro termos da sua PA:".format(n))
for c in range(primeiroTermo, ultimoTermo, razao):
  print(c, end=" ")