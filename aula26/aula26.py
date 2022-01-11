x = 10

try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento")

num = -10

if num < 1:
    raise Exception("Valor não permitido")

num = "Roberto"

if not type(num) is int:     #se tipo num não é um inteiro
    raise Exception("Somente números permitidos")
else:
    print(num)
