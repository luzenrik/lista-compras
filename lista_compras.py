import os


# Caminho do arquivo de lista de compras
ARQUIVO_LISTA = 'lista_compras.txt'

def exibir_lista(lista_compras):
    """
    Exibe todos os itens da lista de compras.
    """
    print("Lista de Compras:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")
def adicionar_item():

def remover_item():
    
def salvar_lista(): 
          
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