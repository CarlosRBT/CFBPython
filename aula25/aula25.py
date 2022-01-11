class NPC:  # Base, pai, super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome.....: " + self.nome)
        print("Time.....: " + str(self.time))
        print("Força....: " + str(self.forca))
        print("Munição..: " + str(self.municao))
        print("Vivo.....: " + ("sim" if self.vivo else "não"))
        print("Energia..: " + str(self.energia))
        print("--------------------------------------")


class Soladado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)


class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)


class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)

        def inf(self):
            super().info()


s1 = Guarda("Olho vivo", 1)
s2 = Soladado("Bala na agulha", 1)
s3 = Elite("Ninja", 1)
s4 = Guarda("Super atento", 2)
s5 = Soladado("Tiro certo", 2)
s6 = Elite("Samurai", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
