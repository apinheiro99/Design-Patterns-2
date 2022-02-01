class Impressao():

    def __init__(self):
        self.__expressao = ""

    @property
    def expressao(self):
        return self.__expressao

    def clear(self):
        self.__expressao = ""

    def visita_subtracao(self, subtracao):
        print("(",end="")
        self.__expressao += "("
        subtracao.expressao_esquerda.aceita(self)
        print("-",end="")
        self.__expressao += "-"
        subtracao.expressao_direita.aceita(self)
        print(")",end="")
        self.__expressao += ")"

    def visita_soma(self, soma):
        print("(",end="")
        self.__expressao += "("
        soma.expressao_esquerda.aceita(self)
        print("+",end="")
        self.__expressao += "+"
        soma.expressao_direita.aceita(self)
        print(")",end="")
        self.__expressao += ")"

    def visita_numero(self, numero):
        print(numero.avalia(),end="")
        self.__expressao += str(numero.avalia())