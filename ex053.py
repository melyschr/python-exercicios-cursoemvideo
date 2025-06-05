'''053 - Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços 
(exemplos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA)'''
print('=== PALINDROMOS ===\n')

# Ler frase
frase = str(input(" Digite uma frase qualquer: ")).strip().upper()
# Separar frase em uma lista e juntar palavras com split e join
palavras = frase.split()
junto = ''.join(palavras)
# Inverter palavra com laço FOR
inverso = ''
for letra in range(len(junto) - 1, -1, -1)
  inverso += junto[letra]

if inverso == junto:
  print('Temos um palindromo! Leia de tras para frente')
else:
  print('O inverso de - {} - é - {} -'.format(junto, inverso))
  print('Não é um palindromo')

# Inverter palavra com fatiamento de strings
'''
inverso = junto[::-1]
if inverso == junto:
  print('Temos um palindromo! Leia de tras para frente')
else:
  print('O inverso de - {} - é - {} -'.format(junto, inverso))
  print('Não é um palindromo')
'''