#Henrique - Ordenar estoque
#CÓDIGO TESTE 
import json





def ordenar_estoque(estoque, criterio):
    if criterio == 'categoria':
        return sorted(estoque, key = lambda x: x['categoria'])
    elif criterio == 'quantidade':
        return sorted(estoque, key = lambda x: x['quantidade'])
    elif criterio == 'preco':
        opcao = int(input("Digite (1) para CRESCENTE\nDigite (2) para DECRESCENTE\n"))
        if opcao == 1:
            #ORDEM CRESCENTE
            return sorted(estoque, key=lambda item: item["preco"])
        elif opcao == 2:
            #ORDEM DECRESCENTE
            return sorted(estoque, key=lambda item: item["preco"], reverse=True)
    else:
        raise ValueError("Critério inválido.")


with open('dados.json', 'r', encoding='utf-8') as arquivo:
    estoque = json.load(arquivo)

# Teste
ordenado = ordenar_estoque(estoque, 'preco')  # Troque o critério aqui

# Mostrar resultado
for item in ordenado:
    print(item)


#estoque_teste = [
#    {"nome": "Mouse", "categoria": "Periféricos", "quantidade": 30, "preco": 79.90},
#    {"nome": "Notebook", "categoria": "Informática", "quantidade": 5, "preco": 3599.00},
#    {"nome": "Teclado", "categoria": "Periféricos", "quantidade": 15, "preco": 129.90},
#]

#ordenado = ordenar_estoque(estoque_teste, "preco")
#for item in ordenado:
#    print(item)