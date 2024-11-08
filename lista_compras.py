import os


#nome do arquivo que armazenará a lista de compras
ARQUIVO_LISTA = 'lista_compras.txt'

#Funçao exibir lista
def exibir_lista(lista_compras):
    """
    Exibe todos os itens da lista de compras.
    """
    print("Lista de Compras:")
    """Utiliza o função enumerate para iterar sobre a lista de compras e obter o índice (i) e o valor (item) de cada item.
    O parâmetro start=1 faz com que o índice comece em 1, em vez de 0."""
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item}")

#Função add item na lista
def adicionar_item(lista_compras):
    """
    Adiciona um novo item à lista de compras.
    """
    item = input("Digite o item para adicionar: ")
    """Adiciona o item à lista de compras."""
    lista_compras.append(item)
    print(f"Item '{item}' adicionado")

#Função de removaer item da lista
def remover_item(lista_compras):
    """
    Remove um item específico da lista de compras.
    """
    exibir_lista(lista_compras)
    """Solicita ao usuário que digite o número do item a ser removido.
    Converte a entrada em um número inteiro (int) e subtrai 1 para ajustar ao índice da lista."""
    indice = int(input("Digite o número do item para remover: ")) - 1
    """Verifica se o índice está dentro do intervalo válido (0 até o tamanho da lista - 1)."""
    if 0 <= indice < len(lista_compras):
        """Remove o item no índice especificado da lista.
        Armazena o item removido na variável item_removido."""
        item_removido = lista_compras.pop(indice)
        print(f"Item '{item_removido}' removido")
    else:
        print("Índice inválido.")
    
#Salva arquivos na lista
def salvar_lista(lista_compras):
    """
    Salva a lista de compras em um arquivo de texto.
    """
    """Abre o arquivo de lista de compras em modo de escrita ('w').
    O with garante que o arquivo seja fechado automaticamente após sua utilização."""
    with open(ARQUIVO_LISTA, 'w') as arquivo:
        """Itera sobre cada item da lista de compras."""
        for item in lista_compras:
            """Escreve cada item da lista no arquivo, seguido de uma quebra de linha (\n)."""
            arquivo.write(f"{item}\n")
    print("Lista salva com sucesso!") 

# Função de mostrar lista
def carregar_lista():
    """
    Carrega a lista de compras de um arquivo de texto.
    """
    lista_compras = []
    #Verifica se o arquivo de lista de compras existe.
    if os.path.exists(ARQUIVO_LISTA):
        """Abre o arquivo de lista de compras em modo de leitura ('r').
        O with garante que o arquivo seja fechado automaticamente após sua utilização."""
        with open(ARQUIVO_LISTA, 'r') as arquivo:
            """Itera sobre cada linha do arquivo."""
            for linha in arquivo:
                """Remove espaços em branco no início e fim da linha com strip().
                Adiciona a linha processada à lista de compras."""
                lista_compras.append(linha.strip())
                """Retorna a lista de compras carregada do arquivo."""
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