'''0056 - Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:  
*   A media de idade do grupo
*   Qual o nome do homem mais velho
*   Quantas mulheres tem menos de 20 anos  
'''
print("== Analisador de dados simples =\n")
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher = 0
for p in range (0, 4+1):
  print("=== {}ª pessoa ===")
  name = str(input("Nome: "))
  age = int(input("Idade: "))
  gender = str(input("Genero [M/F]: ")).upper()
  somaidade += idade
  if p == 1 and gender == 'Mm':
    maioridadehomem = age
    nomevelho = name
  if gender in 'Mm' and age > maioridadehomem
    maioridadehomem = age
    nomevelho = name
  if gender in 'Ff' and age < 20:
    totmulher += 1

# Media de idades
mediaidade = somaidade / 4
print("A soma da idade do grupo é {}.".format(mediaidade))
# Homem mais velho
print("O Sr {} é o homem mais velhor e ele tem {} anos". format(nomevelho, maioridadehomem))
# Mulheres abaixo dos 20
print("Há no total {} mulheres com menos de 20 anos".format(totmulher))

# esse exercicio sera usado como base para desenvolver um algoritmo de analise de um dataset e filtrar valores e mostrar resultados com base no que é desejado)