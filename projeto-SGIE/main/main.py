import datetime

#Importando Funções Lucas
from funcoes_json import addRegistro, buscarRegistros, buscaFiltroRegistro, validarRegistro, excluiRegistro

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
print("=" * 30)
print("         MENU PRINCIPAL")
print("=" * 30)
print("1 - Adicionar")
print("2 - Ver registros")
print("3 - Editar")
print("4 - Excluir registro")
print("0 - Sair")
print("=" * 30)
opcaoUsuario = int(input("Informe uma opção: "))

while opcaoUsuario != 0:
    match opcaoUsuario:
        case 1:
            validarRegistro = 1
            while validarRegistro != 0:
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

                validaRegistro = validarRegistro()

                if validaRegistro == 0:
                    print("Registro cadastrado com sucesso!")
                else:
                    print("Já existe um mesmo registro com o mesmo código.")

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
        case 4:
            vereficaRegistros = buscarRegistros()

            if len(vereficaRegistros) == 0:
                print("Você não possui registros")
            else:
                codRegistro = input("Informe o código do registro: ")
                indiceRegistro = filtraRegistros(codRegistro)

                if indiceRegistro == -1:
                    print("Registro não encontrado!")
                else:    
                    excluiRegistro(indiceRegistro)
            

        case _:
            print("Informe uma opção válida!")

    opcaoUsuario = int(input("=======\n1-Adicionar\n2-Ver registros\n3-Editar\n0-Sair\n===========\nInforme uma opção: "))
