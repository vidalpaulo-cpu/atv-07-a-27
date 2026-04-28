# Exercícios 16 - Condição com AND

idade= int(input("Idade"))
carteira = input("Tem carteira? (sim/não): ")

if idade >= 18 and carteira == "sim":
  print("Pode dirigir")
else:
  print("não poe dirigir")
