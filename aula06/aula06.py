curso = "Curso de Python"

print(curso[6])
print(curso[0:10])
print(curso[9:15])
print("Tamanho da String: " + str(len(curso)))

#print(curso.strip()) retira os espaços vazios do início e fim do texto
#print(curso.lower()) transforma todas as letras em minusculas 
#print(curso.upper().strip) transforma todas as letras em maiusculas e retira espaços vazios do início e fim
#print(curso.replace("Python", "C#")) substitui a palavra Python por C#

a=curso.split(" ") #split divide o texto por por caracter q usar como( espaço, .ponto, ? interrogação) formando um list/array
print(a[1])



