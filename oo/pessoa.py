class Pessoa:
    def __init__(self):
        self.nome = None

    def cumprimentar(self):
        return f'Ola {id(self)}'


    if __name__ == '__main__':
        p = Pessoa()
        print(Pessoa.cumprimentar(p))
        print(id(p))
        print(p.cumprimentar())
        print(p.nome)
        p.nome = 'Eliane'
        print(p.nome)


