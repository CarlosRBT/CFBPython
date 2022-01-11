curso = "Curso de Python" 

resposta = "Python" in curso
print(resposta)

resposta = "Python" not in curso   # not in funciona como negação por isso a resposta é false 
print(resposta)

resposta = "python" in curso
print(resposta)
print("-------------------------------------")

texto = "Curso de Python"
palavra = "python"

resposta = palavra in texto
print(resposta)

resposta = palavra.upper() in texto.upper()
print(resposta)

resposta = palavra.upper() not in texto.upper()
print(resposta)
print("------------------------------------")

curso = "Curso de Python"
canal = "CFB Curso"
resposta= curso + " do canal " + canal  #concatenou as duas Strings
print(resposta)
print("------------------------------------")


cidade = "São Paulo"
dia = 21
mes = "Novembro"
ano = 2021
canal = "CFB Cursos"
print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano))

data = "{}, {} de {} de {} \n\"{}\""
print(data.format(cidade, dia, mes, ano, canal))

