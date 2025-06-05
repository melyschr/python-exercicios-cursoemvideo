'''050 - Desenvolva um programa que leia seis numero inteiros e mostre 
a soma apenas daquele que forem pares. Se o valor digitado for impar, desconsiderar.'''
print("Soma de pares\n")

soma = 0
for c in range (0,6):
  numero = int(input("Escreva um numero inteiro: "))
  if numero % 2 == 0:
    soma += numero
print("\nA soma de pares é igual á",soma)