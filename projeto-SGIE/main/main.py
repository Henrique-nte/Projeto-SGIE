import datetime

#Importando Funções 
from funcoes_json import addRegistro, buscarRegistros, buscaFiltroRegistro
from funcoes_json import validarRegistro, excluiRegistro, buscaRegistrosFiltrados
from funcoes_json import ordenar_estoque, exibir_estoque
from funcoes_json import filtraRegistros

dataLocal = datetime.datetime.now()
vetorRegistros = []

#Carrega registros já existentes
dadosUsuario = buscarRegistros()
if len(dadosUsuario) != 0:
    vetorRegistros.extend(dadosUsuario)
    addRegistro(vetorRegistros)

#Menu principal
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
            validaRegistro = 1
            while validaRegistro != 0:
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

                validaRegistro = validarRegistro(novoRegistro)

                if validaRegistro == 1:
                    vetorRegistros.append(novoRegistro)
                    addRegistro(vetorRegistros)
                    print("Registro cadastrado com sucesso!")
                    validaRegistro = 0
                else:
                    print("Já existe um mesmo registro com o mesmo código.")

        case 2:
            dadosUsuario = buscarRegistros()

            if len(dadosUsuario) == 0:
                print("Você não possui registros!")  
            else:
                print("Deseja ordenar seu estoque?")
                chose = int(input("1 - Ver estoque ordenado\n2 - Filtrar a partir de datas, categorias, ou pelo código\n3 - Ver todos os registros sem ordenação\n:"))
                match chose:
                    case 1:
                        lista_ordenada = ordenar_estoque(dadosUsuario)
                        exibir_estoque(lista_ordenada)
                    case 2:
                        escolhaFiltro = int(input("1 - Categorias\n2 - Datas\n3-Código do item\nEscolha o seu filtro: "))
                        
                        match escolhaFiltro:
                            case 1:
                                categoriasFiltro = input("Informe o filtro da categoria: ")
                                situacaoFiltrada = buscaRegistrosFiltrados(categoriasFiltro.lower(), "categoriaRegistro")

                                if(situacaoFiltrada == 0):
                                    print("Não possui registros a partir desse filtro!")
                                else:
                                    exibir_estoque(situacaoFiltrada)

                            case 2:
                                dataFiltro = input("Informe o filtro da data: ")
                                situacaoFiltrada = buscaRegistrosFiltrados(dataFiltro, "dataRegistro")
                                
                                if(situacaoFiltrada == 0):
                                    print("Não possui registros a partir desse filtro!")
                                else:
                                    exibir_estoque(situacaoFiltrada)

                            case 3:
                                codFiltro = input("Informe o código do item para filtrar: ")
                                situacaoFiltrada = buscaRegistrosFiltrados(codFiltro, "codRegistro")
                                
                                if(situacaoFiltrada == 0):
                                    print("Não possui registros a partir desse filtro!")
                                else:
                                    exibir_estoque(situacaoFiltrada)
                            
                            case _:
                                print("Opção inválida!")

                    case 3:
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
                codRegistro = input("Informe o código do registro para excluir: ")
                indiceRegistro = filtraRegistros(codRegistro)

                if indiceRegistro == -1:
                    print("Registro não encontrado!")
                else:
                    confirmacao = int(input("Deseja realmente excluir esse registro? (1 - Sim | Para cancelar, informe outro número): "))
                    if confirmacao == 1:    
                        excluiRegistro(indiceRegistro)
                        print("Registro excluido com sucesso!")
                    else:
                        print("Voltando...\n")

        case _:
            print("Informe uma opção válida!")

    #Menu alternativo
    print("=" * 30)
    print("1 - Adicionar")
    print("2 - Ver registros")
    print("3 - Editar")
    print("4 - Excluir registro")
    print("0 - Sair")
    print("=" * 30)
    opcaoUsuario = int(input("Informe uma opção: "))