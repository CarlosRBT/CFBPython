carros = ["Fusion", "Jeta", "Subaru", "Civic", "Corola"]
for c in carros:
    print(c)
print("---------------")

itCarros = iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break
