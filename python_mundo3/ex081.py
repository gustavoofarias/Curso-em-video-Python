'''
Exercício Python 081: 
Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []

while True:
    print("Digite um número negativo caso queira cancelar.")
    num = int(input("Digite um número:"))
    if num < 0:
        break
    else:
        lista.append(num)

tamanho_lista = len(lista)
print(f"Foi digitado {tamanho_lista} números.")

if lista.count(5) == 5:
    print("O número 5 está presente na lista.")
else:
    print("Não está na lista.")

lista_reversa = lista.sort(reverse=True)

print(f"A lista de forma descrecente: {lista_reversa}")


    
