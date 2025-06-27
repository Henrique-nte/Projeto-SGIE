import json, datetime

#Eu pego a data local do usuário
dataLocal = datetime.datetime.now()

urlJson = 'projeto-SGIE/main/json/dados.json'

#Crio uma função que envia esses registros para o meu arquivo JSON
def addRegistro(dados):
    with open(urlJson, 'w', encoding='utf-8') as arquivoJson:
        json.dump(dados, arquivoJson, indent=4)


#Crio uma função que resgata os dados existentes desse usuário
def buscarRegistros():
    try:
        with open(urlJson, 'r', encoding='utf-8') as arquivoJson:
            return json.load(arquivoJson)
    except:
        return []

#Essa função edita a partir do registro especificado pelo usuário
def buscaFiltroRegistro(posRegistro):
    with open(urlJson, 'r', encoding='utf-8') as arquvoJson:
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
        with open(urlJson, 'w', encoding='utf-8') as arquvoJson:
            json.dump(dadosJson, arquvoJson, indent=4)

#Função que valida caso o usuário informa um código ja existente no arquivo json
def validarRegistro(novoRegistro):
    registrosUsuario = buscarRegistros()
    if len(registrosUsuario) != 0:
        for i in range(len(registrosUsuario)):
            if registrosUsuario[i]['codRegistro'] == novoRegistro['codRegistro']:
                return 0
    return 1

#Função que exclui o registro a partir no índice escolhido pelo usuário
def excluiRegistro(indiceRegistro):
    with open(urlJson, 'r', encoding='utf-8') as arquivoJson:
        dadosJson = json.load(arquivoJson)

        del dadosJson[indiceRegistro]

        with open(urlJson, 'w', encoding='utf-8') as arquivoJson:
            json.dump(dadosJson, arquivoJson, indent=4)

#Função aonde pega o registo a partir do código que o usuário informa
def filtraRegistros(cod):
    try:
        with open(urlJson, 'r', encoding='utf-8') as arquivoJson:
            dadosJson = json.load(arquivoJson)
            for i in range(len(dadosJson)):
                if dadosJson[i]['codRegistro'] == cod:
                    return i
            return -1
    except:
        return []

#Função que faz a busca do registro filtrado a partir do tipo da escolha o usuário
def buscaRegistrosFiltrados(filtroUsuario, tipoEscolhido):
    try:
        with open(urlJson, 'r', encoding='utf-8') as arquivoJson:
            dadosJson = json.load(arquivoJson)
            vetorRegistrosFiltrados = []

            for i in range(len(dadosJson)):
                if dadosJson[i][tipoEscolhido].lower() == filtroUsuario:
                    vetorRegistrosFiltrados.append(dadosJson[i])
            
            if len(vetorRegistrosFiltrados) == 0:
                return 0
            return vetorRegistrosFiltrados
    except:
        return []

#Função que ordena o estoque
def ordenar_estoque(estoque):
    print("Qual ordenação deseja?")
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

#Função para exibir o estoque
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