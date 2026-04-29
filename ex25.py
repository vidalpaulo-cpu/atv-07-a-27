# Exercicio 25 - Desconto no pedido
4
produto = input("Digite o nome do produto:
6
preco = float(input("Digite o preço do produto: R$ "))
7
quantidade = int(input("Digite a quantidade:"))
8
total = preco *
quantidade
10
if total > 50:
11
12
desconto = total * 0.10
13
14
15
else:
total_final = total - desconto
print("Desconto aplicado: 10%")
total_final = total
16
17
print("Sem desconto")
18
print(f"Produto:{produto}")
19
print(f"Total a pagar: R$ {total_final:.2f}")
