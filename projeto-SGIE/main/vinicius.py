import json


from funcoes_json import filtraRegistros


def remover(dic):
    with open("dados.json", "r") as variavel:
        dados = json.load(variavel)

        for i in range(len(dados)):
            if remover in dados[dic]:
                 del dados[remover]
            return -1
        return i
            


remove = input("o que tu deseja remover?")
caso = remover(remove)
if caso ==1:
    print("Não encontrado")
else:
    print(caso)


    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

