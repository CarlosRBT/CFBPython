Valores = [1, 5, 3, 2]


def somar(num):
    r = 0
    for n in num:
        r += n              # r += significa x = x+valor
    return r


r = somar(Valores)

print(str(Valores) + ": Soma = " + str(r))
