n1 = 15
n2 = 7

def somar():
    r = n1 + n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))

somar()
print("----------------")


def somar(n1, n2):
    r = n1 + n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))

somar(5,7)
somar(39, 23)
somar(12, 7)
print("--------------------")


def somar(n1, n2, n3, n4):
    r = n1 + n2 + n3 + n4
    print("Somar = " + str(r))

somar(12, 7, 5, 124)
somar(23, 26, 27,2)
somar(23, 45, 67, 12)
print("---------------------------")


def textos(*t):
    print(t[0])
    print(t[1])
    print(t[2])

textos("CFB Cursos", "Python", "Dia", "Computador", "Anime")
print("-----------------------------")

def textos(*txt):
    for t in txt:
        print(t)

textos("CFB Cursos", "Python", "Dia", "Computador", "Anime")
print("--------------------------")


def somar(*num):
    r=0
    for n in num:
        r += n
    
    print("Soma = " + str(r))

somar(7, 3, 34, 3, 245, 34,76,87,9675,123)
print("------------------------")


valores = [3, 4, 6, 76, 21]
def somar(num):
    r=0
    for n in num:
        r += n

    print("Soma = " + str(r))

somar(valores)







