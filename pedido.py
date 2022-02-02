from datetime import date

class Pedido():
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = "NOVO"
        self.__data_finalizacao = None

    def paga(self):
        self.__status = "PAGO"

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = "ENTREGUE"

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

from abc import ABCMeta, abstractmethod
class Comando(ABCMeta):
    @abstractmethod
    def executa(self):
        pass

class Fila_de_trabalho():
    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()