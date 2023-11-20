from dataclasses import dataclass
from constants import FILE_NAME

@dataclass
class Livro:
    _titulo: str
    _autor: str
    _ano: int
    _genero: str
    _quantidade: int

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, value: str):
        self._save_data()
        self._titulo = value

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, value: str):
        self._save_data()
        self._autor = value

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, value: int):
        self._save_data()
        self._ano = value

    @property
    def genero(self) -> str:
        return self._genero

    @genero.setter
    def genero(self, value: str):
        self._save_data()
        self._genero = value

    @property
    def quantidade(self) -> str:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value: int) -> str:
        self._save_data()
        self._quantidade = value

    def _save_data(self) -> None:
        with open(FILE_NAME, 'r+') as arquivo:
            books: list[dict] = json.load(arquivo)

            new_books = []
            for book in books:
                if not (self._titulo in list(book.keys())):
                    new_books.append(book)
                else:
                    new_books.append(self.obter_informacoes())

            json.dump(new_books, arquivo)

    def obter_informacoes(self):
        return { 
            self._titulo: [self._autor, self._ano, self._genero, self._quantidade]
        }
