'''061 - Refaça o desafio 051, lendo o primeiro termo 
e a razão de uma PA e mostrando os 10 primeiros termos da progressão usando a estrutura while'''
print("== Progressão Aritmetica - 2.0 ==\n")
primeiroTermo = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA (numero inteiro): "))
n = int(input("Quantos termos deseja exibir: "))
ultimoTermo = primeiroTermo + (n - 1) * razao
ultimoTermo += 1

