import json
from livro import Livro

class Biblioteca:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.carregar_dados()

    def cadastrar_livro(self, livro):
        if livro.titulo not in self.livros:
            self.livros[livro.titulo] = livro.obter_informacoes()
            self.salvar_dados()
            print(f"Livro '{livro.titulo}' cadastrado com sucesso!")
        else:
            print("Livro já cadastrado.")

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            info_livro = self.livros[titulo]
            self.exibir_informacoes(info_livro)
        else:
            print("Livro não encontrado.")

    def listar_livros_por_autor(self, autor):
        livros_autor = [livro for livro in self.livros.values() if livro['autor'] == autor]
        if livros_autor:
            for info_livro in livros_autor:
                self.exibir_informacoes(info_livro)
        else:
            print(f"Nenhum livro encontrado do autor {autor}.")

    def listar_livros_por_genero(self, genero):
        livros_genero = [livro for livro in self.livros.values() if livro['genero'] == genero]
        if livros_genero:
            for info_livro in livros_genero:
                self.exibir_informacoes(info_livro)
        else:
            print(f"Nenhum livro encontrado no gênero {genero}.")

    def salvar_dados(self):
        with open(self.arquivo, 'w') as arquivo:
            json.dump(self.livros, arquivo)
        print("Dados salvos com sucesso!")

    def carregar_dados(self):
        try:
            with open(self.arquivo, 'r') as arquivo:
                self.livros = json.load(arquivo)
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            self.livros = {}
            print("Arquivo não encontrado. Nenhum dado carregado.")

    def exibir_informacoes(self, info_livro):
        print(f"Título: {info_livro['titulo']}")
        print(f"Autor: {info_livro['autor']}")
        print(f"Ano de Publicação: {info_livro['ano']}")
        print(f"Gênero: {info_livro['genero']}")
        print(f"Quantidade disponível: {info_livro['quantidade']}\n")
