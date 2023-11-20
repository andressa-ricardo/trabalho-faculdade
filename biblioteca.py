import json
from livro import Livro
from constants import FILE_NAME

class Biblioteca:
    def __init__(self):
        self.livros: list[Livro] = []
        self.carregar_dados()

    def cadastrar_livro(self, livro):
        for saved_book in self.livros:
            if livro.titulo in saved_book.titulo:
                print("Livro já cadastrado.")
                return
        self.livros.append(livro)
        self.salvar_dados()
        print(f"Livro '{livro.titulo}' cadastrado com sucesso!")

    def consultar_livro(self, titulo):
        for livro in self.livros:
            if titulo in livro.titulo:
                self.exibir_informacoes(livro)
                return
        print("Livro não encontrado.")

    def listar_livros_por_autor(self, autor):
        found_one = False
        for livro in self.livros:
            if autor.lower() in livro.autor.lower():
                self.exibir_informacoes(livro)
                if not found_one:
                    found_one = True
        if not found_one:
            print(f"Nenhum livro encontrado do autor {autor}.")

    def listar_livros_por_genero(self, genero):
        found_one = False
        for livro in self.livros:
            if genero.lower() in livro.genero.lower():
                self.exibir_informacoes(livro)
                if not found_one:
                    found_one = True
        if not found_one:
            print(f"Nenhum livro encontrado no gênero {genero}.")

    def salvar_dados(self):
        with open(FILE_NAME, 'w') as arquivo:
            dicts = {}
            for livro in self.livros:
                dicts[livro.titulo] = livro.obter_informacoes()[livro.titulo]
            json.dump(dicts, arquivo)
        print("Dados salvos com sucesso!")

    def carregar_dados(self):
        try:
            with open(FILE_NAME, 'r') as arquivo:
                livros = json.load(arquivo)
                for titulo, values in zip(livros, livros.values()):
                    autor, ano, genero, quantidade = values
                    self.livros.append(
                        Livro(titulo, autor, ano, genero, quantidade)
                    )

            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            self.livros = []
            print("Arquivo não encontrado. Nenhum dado carregado.")

    def exibir_informacoes(self, livro: Livro):
        print(f"Título: {livro.titulo}")
        print(f"Autor: {livro.autor}")
        print(f"Ano de Publicação: {livro.ano}")
        print(f"Gênero: {livro.genero}")
        print(f"Quantidade disponível: {livro.quantidade}\n")