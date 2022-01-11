carros = ["Audi", "Subaru", "HRV", "Tracker\n"]

for x in carros:
    print(x)

carros = [                          # primeiro valor "Linha", segundo valor"colona"
    ["Modelo", "HRV"],              # "modelo" = linha=0, "HRV"= coluna=1
    ["Fabricante", "Honda"],
    ["Ano", "2020"]
]                                   # primeiro valor "Linha", segundo valor"colona"

print(carros[2][1])
print("\n")


carros = [                          # primeiro valor "Linha", segundo valor"colona"
    ["Modelo", "HRV"],              # "modelo" = linha=0, "HRV"= coluna=1
    ["Fabricante", "Honda"],
    ["Ano", "2020"]
]

for l, c in carros:
    print("Linha: " + l + "| Coluna: " + c)
print("\n")


carros = [                          
    ["Modelo", "HRV"],             
    ["Fabricante", "Honda"],
    ["Ano", 2020]               # "ano" = String, "2020"= Int, necessário concatenar valores string com int
]

for l, c in carros:
    print("Linha: " + l + "| Coluna: " + str(c))
print("\n")


carros = [                          
    ["Modelo", "HRV"],             
    ["Fabricante", "Honda"],
    ["Ano", 2020]              
]

carros [2][1] = 2021        # Alterou o valor da matriz de 2010 para 2021, indicando linha e coluna da mudança desejada
print(carros [1][1])         #imprimir único elemento da matriz

for l, c in carros:
    print("Linha: " + l + "| Coluna: " + str(c))
print("\n")


carros= [                          
    ["Modelo", "HRV"],             
    ["Fabricante", "Honda"],
    ["Ano", 2020]              
]

carros.append(["Cor", "Prata"])      # append adicionou mais uma linha e duas colunas na matriz

for l, c in carros:
    print("Linha: " + l + "| Coluna: " + str(c))

