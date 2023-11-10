class Livro:
    def __init__(self, titulo, autor, ano, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.quantidade = quantidade

    def obter_informacoes(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano,
            'genero': self.genero,
            'quantidade': self.quantidade
        }
