'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

lista_notas = []

while True:

    lista_temp = []

    nome = str(input("Digite seu nome:"))
    lista_temp.append(nome)
    nota1 = float(input("Digite sua nota:"))
    lista_temp.append(nota1)
    nota2 = float(input("Digite sua nota:"))
    lista_temp.append(nota2) 

    lista_notas.append(lista_temp[:])

    lista_temp.clear()


    usuario = input("Que continuar cadastrando alunos? S/N").upper()

    if usuario == 'S':
        continue

    else:
        break
print(lista_notas)

for i in lista_notas:
    for z in i:
        nome = i[0]
        media = (i[1] + i[2]) / 2
    print(f" Nome: {nome}")
    print(f"A média do aluno é {media}") 


while True:
    usuario2 = input("Que aluno você quer ver as notas?")

    if usuario2 == 999:
        break
    else:
        continue
