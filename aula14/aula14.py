import os
os.system('cls')

i = 0
while i < 10:
    print(i)
    i += 1
print("Fim do programa\n")

i = 0
while i < 10:
    print(i)
    i += 1
    if (i >= 5):
        break
print("Fim do programa\n")


carros = []
carro = input("Digite nome do novo carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite nome do novo carro: ")


for x in carros:
    print(x)
    

print("Fim do loop\n")
