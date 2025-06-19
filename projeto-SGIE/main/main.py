import json, datetime;

def addRegistro(vetorDadosUsuario):
    with open('dados.json', 'w') as dados:
        json.dump(vetorDadosUsuario, dados)

def buscarRegistros():
    pass

opcaoUsuario = int( input("=======\n1-Adicionar\n2-Ver registros0-Sair\n===========\nInforme uma opção: "))
id = 1

while(opcaoUsuario != 0):
    registrosUsuario = []
    
    match opcaoUsuario:
        case 1:
            nomeRegistro = input("Informe o nome do registro: ")
            precoRegistro = float(input("Informe o preço do pedido: "))
            dataFabricacao = input("Informe a data de fabricação (dd/mm/aaaa): ")
            quantidadeRegistro = int(input("Informe a quantidade do produto: "))

            registrosUsuario.append(id)
            registrosUsuario.append(nomeRegistro)
            registrosUsuario.append(precoRegistro)
            registrosUsuario.append(dataFabricacao)
            registrosUsuario.append(quantidadeRegistro)
            registrosUsuario.append(datetime.datetime.today)

            addRegistro(registrosUsuario)
            id += 1
        case 2:
            buscarRegistros()
    
    opcaoUsuario = int(input("=======\n1-Adicionar\n2-Ver registros0-Sair\n===========\nInforme uma opção: "))


    
    
    
    
    
    
    
    
    
    #Henrique
    #Vou adicionar um campo para pedir o critério de Organização, dependendo do critério ele irá printar de acordo  