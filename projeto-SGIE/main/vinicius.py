import json


from funcoes_json import filtraRegistros

def remover(dic):
 
    with open("dados.json", "r") as variavel:
        dados = json.load(variavel)

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


        for i in range(len(dados)):
            indice = filtraRegistros(remove)
            if remover(dados[i]) == dic:
                 if codigo in dados:
                    del dados[remover]
            return -1
        else:
            return i
            

codigo = input("Digite o codigo")
remove = input("o que tu deseja remover?")


caso = remover(remove)
if caso ==1:
    print("Não encontrado")
else:
    print(caso)


    