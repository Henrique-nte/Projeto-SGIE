import json

with open("dados.json", "r") as variavel:
    dados = json.load(variavel)

remover = input("Arquivo que você deseja remover: ")

if "arquivo" in dados and remover in variavel:

    dados["arquivo"].remove(remover)
else:
    print("Não encontrado")


with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)


print(dados)