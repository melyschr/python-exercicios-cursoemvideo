'''064 - Crie um programa que leia varios numero inteiros pelo teclado. O programa só vai parar 
quando o usuario digitar o valor 999, que é a condição de parada. 
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)'''
c = 0
soma = 0
cont = 0
while c == 0:
  n = int(input("Digite um numero inteiro de 1 a 999: "))
  cont += 1
  soma += n
  if n == 999:
    print("Foram digitados {} numeros".format(cont))
    print("\nE a soma entre eles foi de {}".format(soma))
    c = 1

