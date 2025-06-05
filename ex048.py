'''048 - Faça um programa que calcule a soma entre todos os numero
impares que são multiplos de tres e que se encontram no intervalo de 1 a 500'''

print("Somando numero impares multiplos de tres\n")
c = 0
soma = 0
for c in range(0, 50):
  if c % 2 != 0 and c % 3 == 0:
    soma +=c
    contador +=1
    print(c, end=" ")
print("\nA soma total é igual á: ", soma)
