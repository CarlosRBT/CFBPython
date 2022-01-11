# key=chave EX: "Fabricante" e valve= valor Ex: "Honda"

carro = {
    "Fabricante": "Honda",
    "Modelo": "HRV",
    "Ano": "2021",
    "Cor": "Prata"
}

fabricante = carro.get("Fabricante")
print(fabricante)

print(carro["Fabricante"])
print("--------------")

for x in carro:
    print(x)
print("--------------")

for x in carro:
    # print(x)=Chave  print(carro[x])= valor
    print(carro[x])
print("-----------")

for c, v in carro.items():
    print(c + " : " + v)
print("----------------")

if "Modelo" in carro:
    print("Sim, modelo é uma chava ")
print("--------------------")

print("Tamanho do dictionary: " + str(len(carro)))
print("--------------------")

# adiciona mais uma chave e valor
carro["Cambio"] = "Automatico"
for x in carro:
    print(x)
print("-----------------------")

# Pop = remove uma chave e valor ou usar del carro["Ano"]
carro.pop("Ano")
for x in carro:
    print(x)
print("-----------------")

# carro.clear = limpa tudo dentro da chave/dictionary



carros = {
    "Carro1" : {
        "Fabricante" : "Honda",
        "Modelo" : "Civic"
    },
    "Carro2" : {
        "Fabricante" : "Audi",
        "Modelo" : "A3"
    },
    "Carro3" : {
        "Fabricante" : "Chevrolet",
        "Modelo" : "Tracker"
    }
}

for x in carros:
    print(carros[x])
print("\n")
print(carros["Carro2"])  
print("\n")
print(carros["Carro3"]["Modelo"])  
print("-----------------")


