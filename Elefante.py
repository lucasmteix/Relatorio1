from Animal import Animal


class Elefante(Animal):

    #Atributos

    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho




    #Metodos

    def trombar(self):
        print("O elefante " + self.nome + " trombou: " + self.nome)

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        print("O tamanho do animal " + self.nome + " foi mudado para " + self.tamanho)