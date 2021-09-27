class Pessoa:
    def cumprimentar(self):
        return 'Olá {id(self)}'


    if __name__ == '__main__':
        p =Pessoa()
        print(Pessoa.cumprimentar(p))
        print(id())
        print(p.cumprimentar())



