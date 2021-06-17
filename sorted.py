class Pessoa:

    def __init__(self, nome) -> None:
        self._nome = nome

    def __repr__(self) -> str:
        return self._nome

n = Pessoa('Naiara')
c = Pessoa('Carlos')
v = Pessoa('Vinícius')
m = Pessoa('Marco')

pessoas = [n,c,m,v]

print(sorted(pessoas))