import json, datetime;

#Eu pego a data local do usuário
dataLocal = datetime.datetime.now()

#Faço um vetor para armazenar os registros
vetorRegistros = []

#Crio uma função que envia esses registros para o meu arquivo JSON
def addRegistro(dados):
    
    with open('projeto-SGIE/main/json/dados.json', 'w') as arquivoJson:
        json.dump(dados, arquivoJson, indent=4)


#Crio uma função que resgata os dados existentes desse usuário
def buscarRegistros():
    
    with open('projeto-SGIE/main/json/dados.json', 'r') as arquvoJson:
        
        #Faço um try catch para tratamento de erros caso não tenha dados no arquivo retorno um array vazio
        try:
            dadosJson = json.load(arquvoJson)
        except:
            return []
    
    return dadosJson

#Aqui eu chamo minha função que busca esses registros caso o usuário ja tenha registrado algo antes
dadosUsuario = buscarRegistros()

if(len(dadosUsuario) != 0):
    
    #Faço um for que itera sobre esses registros e adiciona ao vetor registros
    for i in range(len(dadosUsuario)):
        vetorRegistros.append(dadosUsuario[i])
            
    addRegistro(vetorRegistros)

#Aqui escolhemos fazer um menu pro usuário escolher as operações que deseja fazer no software
opcaoUsuario = int( input("=======\n1-Adicionar\n2-Ver registros\n0-Sair\n===========\nInforme uma opção: "))

while(opcaoUsuario != 0):
    
    match opcaoUsuario:
        
        #Esse case cuida dos registros que usuário deseja fazer
        case 1:
            codRegistro = input("Informe um código pro produto: ")
            nomeRegistro = input("Informe o nome do registro: ")
            precoRegistro = float(input("Informe o preço do registro: "))
            categoriaRegistro = input("Informe uma categoria para o registro: ")
            quantidadeRegistro = int(input("Informe a quantidade do produto: "))
            
            registrosUsuario = {
                'codRegistro': codRegistro,
                'nomeRegistro': nomeRegistro,
                'precoRegistro': precoRegistro,
                'categoriaRegistro': categoriaRegistro,
                'quantidadeRegistro': quantidadeRegistro,
                'dataRegistro': f"{dataLocal.day}/{dataLocal.month}/{dataLocal.year}"
            }
            
            vetorRegistros.append(registrosUsuario)
            
            addRegistro(vetorRegistros)
        
        #Esse case faz com que o usuário vê todos os registros
        case 2:
            dadosUsuario = buscarRegistros()

            if(len(dadosUsuario) == 0):
                print("Você não possui registros!")  
            
            else:
                print("\t| Código | Nome do registro | Preço do registro | Categoria do registro | Quantidade do registro | Data registrada |")
                for i in range(len(dadosUsuario)):
                    print(f"\t| {dadosUsuario[i]['codRegistro']} | {dadosUsuario[i]['nomeRegistro']} | {dadosUsuario[i]['precoRegistro']} | {dadosUsuario[i]['categoriaRegistro']} | {dadosUsuario[i]['quantidadeRegistro']} | {dadosUsuario[i]['dataRegistro']} |")
        
        #Caso informe uma opção inválida mostro uma mensagem
        case _:
            print("Informe uma opção válida!")
    
    opcaoUsuario = int(input("=======\n1-Adicionar\n2-Ver registros\n0-Sair\n===========\nInforme uma opção: "))
