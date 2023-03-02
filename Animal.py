class Animal:

    #Atributos

    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som




    #Metodos

    #Printa o som do animal na tela
    def emitir_som(self):
        print(self.nome + " fez o som " + self.som)

    #Muda a cor do animal para a cor especificada
    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
        print("A cor de " + self.nome + " foi mudada para " + self.cor)