num1 = num2 = res=0
canal = "CFB Cursos"

def cn1():
    print(canal)

cn1()

def cn():
    global canal
    canal = "CFB Cursos"

cn()

print(canal)