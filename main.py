from Elefante import Elefante

elefante1 = Elefante("nome", 12, "especie", "cinza", "som", "medio")

print(elefante1.som)

if(elefante1.especie == "Africano"):
    if(elefante1.idade < 10):
        elefante1.tamanho = "pequeno"
        elefante1.som = "Paaah"
    else:
        elefante1.tamanho = "grande"
        elefante1.som = "PAHHHHHH"

print (elefante1.nome, elefante1.idade, elefante1.especie, elefante1.cor,
       elefante1.som, elefante1.tamanho)