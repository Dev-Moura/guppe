"""
POO - Métodos Mágicos

Métodos Mágicos, são todo os métodos que começam e terminam com "__"

dunder init -> ___init__()

Dunder -> Double Underscore

dunder repr -> __repr__() -> Representação do objeto

    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"


"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.titulo.paginas

    def __del__(self):
        print(f"Deletando o livro {self.titulo}")

    def __add__(self, other):
        return f"{self.titulo} e {other.titulo}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ""
            for n in range(other):
                msg += " " + str(self)
            return msg
        return "Não posso multiplicar"


livro1 = Livro("Python rocks!", "Geek University", 400)
livro2 = Livro("Inteligência Artifical com Python", "Geek university", 350)


print(livro1)
print(livro2)
