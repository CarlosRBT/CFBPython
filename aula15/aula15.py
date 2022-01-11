l_carros = ["HRV", "Audi", "Civic\n"]      # l_carros =  List/Array

for x in l_carros:
    print(x)
                                            # l_carros = List permite mudar valor do array na tupla
l_carros[2] = "Corola\n"
for x in l_carros:
    print(x)

                                            # t_carros = tupla não perimite mudar valor diretamente da tupla
t_carros = ("HRV", "Audi", "Civic\n")

for x in t_carros:
    print(x)

t_carros = ("HRV", "Audi", "Civic\n")
l_carros = list(t_carros)
l_carros[1] = "Subaru"
t_carros = tuple(l_carros)

for x in t_carros:
    print(x)
