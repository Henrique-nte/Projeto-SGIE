import json, datetime

#Importando Funções Lucas
from funcoes_json import addRegistro, buscarRegistros, buscaFiltroRegistro;

#Importando Funções Henrique
from funcoes_json import ordenar_estoque, exibir_estoque

#Importando Funções Vinicius
from funcoes_json import filtraRegistros

dataLocal = datetime.datetime.now()
vetorRegistros = []

#-------início--------#


# Carrega registros já existentes
dadosUsuario = buscarRegistros()
if len(dadosUsuario) != 0:
    vetorRegistros.extend(dadosUsuario)
    addRegistro(vetorRegistros)

# Menu principal
opcaoUsuario = int(input("=======\n1-Adicionar\n2-Ver registros\n3-Editar\n0-Sair\n===========\nInforme uma opção: "))

while opcaoUsuario != 0:
    match opcaoUsuario:
        case 1:
            codRegistro = input("Informe um código pro produto: ")
            nomeRegistro = input("Informe o nome do registro: ")
            precoRegistro = float(input("Informe o preço do registro: "))
            categoriaRegistro = input("Informe uma categoria para o registro: ")
            quantidadeRegistro = int(input("Informe a quantidade do produto: "))

            novoRegistro = {
                'codRegistro': codRegistro,
                'nomeRegistro': nomeRegistro,
                'precoRegistro': precoRegistro,
                'categoriaRegistro': categoriaRegistro,
                'quantidadeRegistro': quantidadeRegistro,
                'dataRegistro': f"{dataLocal.day}/{dataLocal.month}/{dataLocal.year}"
            }

            vetorRegistros.append(novoRegistro)
            addRegistro(vetorRegistros)

        case 2:
            dadosUsuario = buscarRegistros()

            if len(dadosUsuario) == 0:
                print("Você não possui registros!")  
            else:
                print("Deseja ordenar seu estoque?")
                chose = int(input("1 - SIM\n2 - NÃO\n:"))
                match chose:
                    case 1:
                        lista_ordenada = ordenar_estoque(vetorRegistros)
                        exibir_estoque(lista_ordenada)
                    case 2:
                        exibir_estoque(dadosUsuario)

        case 3:
            vereficaRegistros = buscarRegistros()

            if len(vereficaRegistros) == 0:
                print("Você não possui registros")
            else:
                codRegistro = input("Informe o código do registro: ")
                indiceRegistro = filtraRegistros(codRegistro)

                if indiceRegistro == -1:
                    print("Registro não encontrado!")
                else:    
                    buscaFiltroRegistro(indiceRegistro)

        case _:
            print("Informe uma opção válida!")

    opcaoUsuario = int(input("=======\n1-Adicionar\n2-Ver registros\n3-Editar\n0-Sair\n===========\nInforme uma opção: "))
