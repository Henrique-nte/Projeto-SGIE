import json, datetime
import os
#Eu pego a data local do usuário
dataLocal = datetime.datetime.now()

CAMINHO_JSON = os.path.join(os.path.dirname(__file__), 'dados.json')

#--------------------------------ÁREA LUCAS HEILER--------------------------------


#Crio uma função que envia esses registros para o meu arquivo JSON

def addRegistro(dados):
    with open(CAMINHO_JSON, 'w', encoding='utf-8') as arquivoJson:
        json.dump(dados, arquivoJson, indent=4)


#Crio uma função que resgata os dados existentes desse usuário
def buscarRegistros():
    try:
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as arquivoJson:
            return json.load(arquivoJson)
    except:
        return []

#Essa função filtra a partir da posição encontrada no filtro do registro
def buscaFiltroRegistro(posRegistro):
    with open(CAMINHO_JSON, 'r', encoding='utf-8') as arquvoJson:
        dadosJson = json.load(arquvoJson)
        
        print("=============Menu filtro============")
        opFiltrado = int(input("1 - Alterar nome\n2 - Alterar Preço\n3 - Alterar Categoria\n4 - Alterar quantidade\n0 - Sair:"))
        while opFiltrado != 0:
            match opFiltrado:
                case 1:
                    dadosJson[posRegistro]['nomeRegistro'] = input("Informe o novo nome para o registro: ")
                case 2:
                    dadosJson[posRegistro]['precoRegistro'] = float(input("Informe o novo preço para o registro: "))
                case 3:
                    dadosJson[posRegistro]['categoriaRegistro'] = input("Informe a nova categoria para o registro: ")
                case 4:
                    dadosJson[posRegistro]['quantidadeRegistro'] = int(input("Informe a nova quantidade para o registro: "))
                case _:
                    print("Opção inválida, tente novamente!")
                
            opFiltrado = int(input("1 - Alterar nome\n2 - Alterar Preço\n3 - Alterar Categoria\n4 - Alterar quantidade\n0 - Sair:"))
        
        dadosJson[posRegistro]['dataRegistro'] = f"{dataLocal.day}/{dataLocal.month}/{dataLocal.year}"
        with open(CAMINHO_JSON, 'w', encoding='utf-8') as arquvoJson:
            json.dump(dadosJson, arquvoJson, indent=4)


def validarRegistro(novoRegistro):
    registrosUsuario = buscarRegistros()
    if len(registrosUsuario) != 0:
        for i in range(len(registrosUsuario)):
            if registrosUsuario[i]['codRegistro'] == novoRegistro['codRegistro']:
                return 1
    return 0


def excluiRegistro(indiceRegistro):
    with open(CAMINHO_JSON, 'r', encoding='utf-8') as arquivoJson:
        dadosJson = json.load(arquivoJson)

        del dadosJson[indiceRegistro]

        with open(CAMINHO_JSON, 'w', encoding='utf-8') as arquivoJson:
            json.dump(dadosJson, arquivoJson, indent=4)

#--------------------------------FIM ÁREA LUCAS HEILER--------------------------------



#--------------------------------ÁREA VINICIUS--------------------------------


#Função Filtrar Registros
def filtraRegistros(cod):
    try:
        with open(CAMINHO_JSON, 'r', encoding='utf-8') as arquivoJson:
            dadosJson = json.load(arquivoJson)
            for i in range(len(dadosJson)):
                if dadosJson[i]['codRegistro'] == cod:
                    return i
            return -1
    except:
        return []

#--------------------------------FIM ÁREA VINICIUS--------------------------------





#--------------------------------ÁREA HENRIQUE S--------------------------------

#ORDENAR ESTOQOUE

def ordenar_estoque(estoque):

    print("--CRITÉRIO--")
    print("1 - CATEGORIA")
    print("2 - QUANTIDADE")
    print("3 - PRECO")
    print("4 - DATA")
    response = int(input("Sua escolha: "))

    match response:
        case 1:
            return sorted(estoque, key = lambda x: x['categoriaRegistro'])
        case 2:
            return sorted(estoque, key = lambda x: x['quantidadeRegistro'])
        case 3:
            print("1 - CRESCENTE")
            print("2 - DESCRESCENTE")
            chose = int(input("Sua escolha: "))
            if chose == 1:
                #ORDEM CRESCENTE
                return sorted(estoque, key=lambda item: item["precoRegistro"])
            elif chose == 2:
                #ORDEM DECRESCENTE
                return sorted(estoque, key=lambda item: item["precoRegistro"], reverse=True)
        case 4:
            return sorted(estoque, key=lambda item: item["dataRegistro"])


def exibir_estoque(estoque_ordenado):
    print("\n| {:^10} | {:^20} | {:^10} | {:^15} | {:^10} | {:^12} |".format(
        "CÓDIGO", "NOME", "PREÇO", "CATEGORIA", "QTDE", "DATA"
    ))
    print("-" * 89)
    for item in estoque_ordenado:
        print("| {:^10} | {:<20} | R${:>7.2f} | {:<15} | {:^10} | {:^12} |".format(
            item['codRegistro'],
            item['nomeRegistro'],
            item['precoRegistro'],
            item['categoriaRegistro'],
            item['quantidadeRegistro'],
            item['dataRegistro']
        ))



#--------------------------------FIM ÁREA HENRIQUE S--------------------------------

