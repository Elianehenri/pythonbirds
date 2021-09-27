class Pessoa:
    def cumprimentar(self):
        return f'Ola {id(self)}'


    if __name__ == '__main__':
        P = Pessoa()
        print(Pessoa.cumprimentar(p))
        print(id(p))
        print(p.cumprimentar())


