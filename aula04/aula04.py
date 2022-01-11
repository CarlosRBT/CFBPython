x = 1
x = ["Carro", "Navio", "Avião", 1, 34.4, True,]  #x assume novo valor, List/Array, pode colocar diferentes tipos de variáveis
y = ("Carro", "Navio", "Avião", 1, 34.4, True)  # variáveis dentro de () se torna Tuplas NÃO PERMITE MUDAR VALORES 

print("Valor de x: " + str(x[1]))
print("Valor de x: " + str(x))    
print("Tipo de variável: " + str(type(x)))


print("Valor de y: " + str(y))
print("Tipo de variável: " + str(type(y)))