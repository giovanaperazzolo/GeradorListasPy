# Cria uma classe ListaToDo para representar cada lista de tarefas
class ListaToDo:
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

# Cria uma classe GerenciadorToDo para gerenciar as listas de tarefas
class GerenciadorToDo:
    def __init__(self):
        self.listas = {}

    def criar_lista(self, nome):
        lista = ListaToDo(nome)
        self.listas[nome] = lista

    def adicionar_item(self, nome_lista, item):
        lista = self.listas.get(nome_lista)
        if lista is not None:
            lista.adicionar_item(item)

# Função principal do programa
def main():
    gerenciador = GerenciadorToDo()

    # Loop principal do programa
    while True:
        print("Escolha uma opção:")
        print("1 - Criar lista")
        print("2 - Adicionar item a lista")
        print("3 - Sair")

        opcao = input()

        if opcao == "1":
            nome_lista = input("Digite o nome da lista: ")
            gerenciador.criar_lista(nome_lista)

        elif opcao == "2":
            nome_lista = input("Digite o nome da lista: ")
            item = input("Digite o nome do item: ")
            gerenciador.adicionar_item(nome_lista, item)

        elif opcao == "3":
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Imprime as listas e seus itens
    print("Listas de tarefas:")
    for lista in gerenciador.listas.values():
        print("- {}".format(lista.nome))
        for item in lista.itens:
            print("  - {}".format(item))

if __name__ == "__main__":
    main()
