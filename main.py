from Elefante import Elefante


#Instanciando o objeto e fazendo a entrada
print("Insira os dados do animal:") #texto de instrucao
elefante1 = Elefante(input("Nome: "), input("Idade: "), input("Espécie: "), input("Cor: "),
                     input("Som: "), input("Tamanho: "))

print("Som original: " + elefante1.som) #saida do som original

#Estrutura de decisao para decidir sobre mudar ou nao o som do elefante
if(elefante1.especie == "Africano"):
    if(int(elefante1.idade) < 10):
        elefante1.tamanho = "pequeno"
        elefante1.som = "Paaah"
    else:
        elefante1.tamanho = "grande"
        elefante1.som = "PAHHHHHH"
    print("Novo som: " + elefante1.som) #saida do novo som
    print("Novo tamanho: " + elefante1.tamanho)