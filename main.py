from livro import Livro
from biblioteca import Biblioteca

def menu():
    print("\n===== Menu da Biblioteca =====")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Listar Livros por Autor")
    print("4. Listar Livros por Gênero")
    print("0. Sair")

if __name__ == "__main__":
    arquivo_json = "biblioteca.json"  
    biblioteca = Biblioteca(arquivo_json)

    while True:
        menu()
        escolha = input("Escolha uma opção (0-4): ")
        print()

        if escolha == "0":
            print("Saindo do programa. Até logo!")
            break
        elif escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação do livro: ")
            genero = input("Digite o gênero do livro: ")
            quantidade = int(input("Digite a quantidade disponível do livro: "))
            novo_livro = Livro(titulo, autor, ano, genero, quantidade)
            biblioteca.cadastrar_livro(novo_livro)
        elif escolha == "2":
            titulo_consulta = input("Digite o título do livro: ")
            print()
            biblioteca.consultar_livro(titulo_consulta)
        elif escolha == "3":
            autor_consulta = input("Digite o autor para listar os livros: ")
            print()
            biblioteca.listar_livros_por_autor(autor_consulta)
        elif escolha == "4":
            genero_consulta = input("Digite o gênero para listar os livros: ")
            print()
            biblioteca.listar_livros_por_genero(genero_consulta)
        else:
            print("Opção inválida. Escolha uma opção válida (0-4).")
