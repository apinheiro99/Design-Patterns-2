from asyncore import file_dispatcher
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

from abc import ABC, abstractmethod
class Comando(ABC):

    @abstractmethod
    def executa(self):
        pass

class Finaliza_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()

class Paga_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()

class Fila_de_trabalho():
    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()

if __name__ == "__main__":

    pedido1 = Pedido("Flavio", 200)
    pedido2 = Pedido("Almeida", 400)

    fila_de_trabalho = Fila_de_trabalho()

    comando1 = Finaliza_pedido(pedido1)
    comando2 = Paga_pedido(pedido1)
    comando3 = Finaliza_pedido(pedido2)

    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()

    print(pedido1.status)
    print(pedido2.status)