def soma(a, b): return a + b
def mult(a, b, c): return (a + b) * c


r = soma(2, 6)
print(r)
print((str(mult(2, 4, 6))) + ("\n"))

print((lambda a, b: a + b)(4, 7))


def r(x, func): return x + func(x)


res = r(2, lambda x: x * x)
print(res)
res = r(2, lambda x: x + 3)
print(res)
