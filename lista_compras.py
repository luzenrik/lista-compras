import os


#nome do arquivo que armazenará a lista de compras
ARQUIVO_LISTA = 'lista_compras.txt'

#funçao exibir lista
def exibir_lista(lista_compras):
    """
    Exibe todos os itens da lista de compras.
    """
    print("Lista de Compras:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")

#função add item na lista
def adicionar_item():
    """
    Adiciona um novo item à lista de compras.
    """
    item = input("Digite o item para adicionar: ")
    lista_compras.append(item)
    print(f"Item '{item}' adicionado")

#função de removaer item da lista
def remover_item():
    """
    Remove um item específico da lista de compras.
    """
    exibir_lista(lista_compras)
    indice = int(input("Digite o número do item para remover: ")) - 1
    if 0 <= indice < len(lista_compras):
        item_removido = lista_compras.pop(indice)
        print(f"Item '{item_removido}' removido")
    else:
        print("Índice inválido.")
    
#salva arquivos na lista
def salvar_lista(lista_compras):
    """
    Salva a lista de compras em um arquivo de texto.
    """
    with open(ARQUIVO_LISTA, 'w') as arquivo:
        for item in lista_compras:
            arquivo.write(f"{item}\n")
    print("Lista salva com sucesso!") 

# função de mostrar lista
def carregar_lista():
    """
    Carrega a lista de compras de um arquivo de texto.
    """
    lista_compras = []
    if os.path.exists(ARQUIVO_LISTA):
        with open(ARQUIVO_LISTA, 'r') as arquivo:
            for linha in arquivo:
                lista_compras.append(linha.strip())
    return lista_compras

# funcão principal em loop
def main():
    lista_compras = carregar_lista()

    while True:
        print("\nOpções:")
        print("1. Exibir lista")
        print("2. Adicionar item")
        print("3. Remover item")
        print("4. Salvar lista")
        print("5. Sair")

        opcao = input("Digite a opção: ")

        if opcao == '1':
            exibir_lista(lista_compras)
        elif opcao == '2':
            adicionar_item(lista_compras)
        elif opcao == '3':
            remover_item(lista_compras)
        elif opcao == '4':
            salvar_lista(lista_compras)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == '__main__':
    main()