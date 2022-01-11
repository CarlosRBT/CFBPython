def somar():
    print("Curso de python")
    print("CFB python")


somar()
print("-----------------------")

n1 = 10
n2 = 15


def somar():
    r = n1 + n2
    print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))


somar()
print("-----------------------")

def subtrair():
    r = n1 - n2
    print("Subtração de " + str(n1) + " e " + str(n2) + " = " + str(r))

subtrair()
print("------------------------------")

def calculos():
    somar()
    subtrair()

calculos()
