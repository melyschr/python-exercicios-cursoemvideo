'''057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado peça a digitação novamente até ter um valor correto.'''
print("== Analisador de dados por Genero ==")
c = 1
while c == 1:
  gender = str(input("Digite qual o seu genero:\n [M] - Masculino] [F] - Feminino : "))
  if gender in 'Mm' or gender in 'Ff':
    print("Encerrando...")
    c = 0
  else:
    print('Valor incorreto, digite novamente')
    c = 1

