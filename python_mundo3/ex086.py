'''
Exercício Python 086: 
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.

'''

lista = []

for i in range(3):
    for z in range(3):
        lista_temp = []
        num = int(input("Digite um número:"))
        lista_temp.append(num)
        lista.append(lista_temp[:])
        lista_temp.clear()

print(lista)