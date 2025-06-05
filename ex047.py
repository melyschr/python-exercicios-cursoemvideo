'''047 - Crie um programa que mostre na tela todos os numero pares que estão no intervalo entre 1 a 50'''
print(" -- Busca de numero pares --")

inicio = int(input("Informe um numero para iniciar: "))
fim = int(input("Informe um numero para terminar o intervalo: "))
c = 0
cont = 0
for c in range(inicio, fim):
  if c % 2 == 0:
    cont = cont + 1
    print(cont, "=", c)