'''049 - Faça o desafio de mostrar a tabuada de um numero que o usuario escolher, utilizando um laço FOR'''
print("= Gerador de tabuada =")
c = 0
tabuada = int(input("Escolha um numero: "))
mult = 0

print("Tabuada do {}".format(tabuada))
for c in range(1,11):
  mult = c * tabuada
  print("{} x {} = {}".format(tabuada, c, mult))
print("FIM!")