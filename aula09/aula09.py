carros = ["Virtus", "Ideia", "Logan", "Palio"]  # []List/Array 
print(carros)

carros = ["Virtus", "Ideia", "Logan", "Palio"]
print(carros[2])

carros = ["Virtus", "Ideia", "Logan", "Palio"]   # método append= adciona objeto a lista
carros.append("Audi Q3")
carros.append("Civic")
carros.append("HRV")
print(carros)
print(str(len(carros)) + " carros na lista")   # método len= consulta tamanho da list + str retorna em String
print("--------------------------------------")

carros = ["Virtus", "Ideia", "Logan", "Palio"]   # método append= adciona objeto a lista
carros.append("Audi Q3")
carros.append("Civic")
carros.append("HRV")
print(carros)
print(str(len(carros)) + " carros na lista")   # método len= consulta tamanho da list + str retorna em String
carros.remove("Palio")
print(str(len(carros)) + " carros na lista")
print(carros)                                  # método .remove= remove objeto da list
                                               # método .pop= remove último objeto da list
                                               # método del carros[2]= remove o segundo objeto da list
                                               # método carros.clear = remove todos os objetos da list

print("\nLista de carros2")                    # métodp list copia todo conteúdo de uma lista para outra
carros2 = list(carros) 
print(carros2)
print(str(len(carros2)) + " carros2 na lista")      
print("--------------------------------------\n")    

carros3 = ["Gol", "Fusca", "Meriva"]
carros3 = carros + carros2
print(str(len(carros3)) + " carros3 na lista ")
print(carros3)


