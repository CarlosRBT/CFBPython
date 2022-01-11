import os                                           #os.system limpa a tela qd roda o programa, função clear
os.system('cls')

#nome = input("Digite seu nome: ")

#print("Nome digitado é: " + nome)

num1 = (input("Digite o primeiro valor: "))
num2 = (input("Digite o segundo valor: "))
resposta = num1 + num2
print("Soma dos valores é: " + resposta)
print("\n")

num1 = int(input("Digite o primeiro valor: "))     # int vai representar qual tipo vai retornar como resposta
num2 = int(input("Digite o segundo valor: "))
resposta = num1 + num2
print("Soma dos valores é: " + str(resposta))
print("\n")



