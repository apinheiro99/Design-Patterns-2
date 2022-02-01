from unittest import TestCase

class Test_aulas(TestCase):

    def test_Classe_contrato(self):
        from datetime import date
        from contrato import Historico, Contrato

        historico = Historico()

        contrato = Contrato(
            data = date.today(),
            cliente = "Flavio Almeida",
            tipo = "NOVO"
        )

        print (contrato.tipo)
        self.assertEqual(contrato.tipo, "NOVO")


        contrato.avanca()
        print (contrato.tipo)
        self.assertEqual(contrato.tipo, "EM ANDAMENTO")

        historico.adiciona_estado(contrato.salva_estado())

        contrato.avanca()
        print (contrato.tipo)
        self.assertEqual(contrato.tipo, "ACERTADO")

        historico.adiciona_estado(contrato.salva_estado())

        contrato.avanca()
        print (contrato.tipo)
        self.assertEqual(contrato.tipo, "CONCLUIDO")

        historico.adiciona_estado(contrato.salva_estado())

        contrato.restaura_estado(historico.obtem_estado(1))
        print (contrato.tipo)
        self.assertEqual(contrato.tipo, "ACERTADO")

        contrato.restaura_estado(historico.obtem_estado(0))
        print (contrato.tipo)
        self.assertEqual(contrato.tipo, "EM ANDAMENTO")

    def test_Classe_Soma(self):
        from operacoes import Soma, Numero

        expressao_esquerda = Soma(Numero(10), Numero(20))
        expressao_direita = Soma(Numero(5), Numero(2))
        expressao_conta = Soma (expressao_esquerda, expressao_direita)
        print (expressao_conta.avalia())

        self.assertEqual(expressao_conta.avalia(), 37)

    def test_Classe_Subtracao(self):
        from operacoes import Subtracao, Numero

        expressao_esquerda = Subtracao(Numero(10), Numero(20))
        expressao_direita = Subtracao(Numero(5), Numero(2))
        expressao_conta = Subtracao(expressao_esquerda, expressao_direita)
        print (expressao_conta.avalia())

        self.assertEqual(expressao_conta.avalia(), -13)

    def test_Classe_Subtracao_com_atributo(self):
        from operacoes import Subtracao, Numero
        from impressao import Impressao

        expressao_esquerda = Subtracao(Numero(10), Numero(20))
        expressao_direita = Subtracao(Numero(5), Numero(2))
        expressao_conta = Subtracao (expressao_esquerda, expressao_direita)
        print (expressao_conta.avalia())

        impressao = Impressao()
        expressao_conta.aceita(impressao)
        self.assertEqual(impressao.expressao, "((10-20)-(5-2))")

    def test_Classe_Soma_com_atributo(self):
        from operacoes import Soma, Numero
        from impressao import Impressao

        expressao_esquerda = Soma(Numero(10), Numero(20))
        expressao_direita = Soma(Numero(5), Numero(2))
        expressao_conta = Soma (expressao_esquerda, expressao_direita)
        print (expressao_conta.avalia())

        impressao = Impressao()
        expressao_conta.aceita(impressao)
        self.assertEqual(impressao.expressao, "((10+20)+(5+2))")

    def test_Classe_Soma_e_Subtracao_com_atributo_1(self):
        from operacoes import Soma, Subtracao, Numero
        from impressao import Impressao

        expressao_esquerda = Soma(Numero(10), Numero(20))
        expressao_direita = Subtracao(Numero(5), Numero(2))
        expressao_conta = Soma (expressao_esquerda, expressao_direita)
        print (expressao_conta.avalia())

        impressao = Impressao()
        expressao_conta.aceita(impressao)
        self.assertEqual(impressao.expressao, "((10+20)+(5-2))")

    def test_Classe_Soma_e_Subtracao_com_atributo_2(self):
        from operacoes import Soma, Subtracao, Numero
        from impressao import Impressao

        expressao_esquerda = Subtracao(Numero(10), Numero(20))
        expressao_direita = Subtracao(Numero(5), Numero(2))
        expressao_conta = Soma (expressao_esquerda, expressao_direita)
        print (expressao_conta.avalia())

        impressao = Impressao()
        expressao_conta.aceita(impressao)
        self.assertEqual(impressao.expressao, "((10-20)+(5-2))")

    def test_Classe_Soma_e_Subtracao_com_atributo_3(self):
        from operacoes import Soma, Subtracao, Numero
        from impressao import Impressao

        expressao_esquerda_1 = Subtracao(Numero(10), Numero(20))
        expressao_direita_1 = Subtracao(Numero(5), Numero(2))
        expressao_conta_1 = Soma (expressao_esquerda_1, expressao_direita_1)

        expressao_esquerda_2 = Soma(Numero(11), Numero(22))
        expressao_direita_2 = Soma(Numero(3), Numero(7))
        expressao_conta_2 = Subtracao (expressao_esquerda_2, expressao_direita_2)

        expressao_conta = Soma(expressao_conta_1, expressao_conta_2)

        print (expressao_conta.avalia())

        impressao = Impressao()
        expressao_conta.aceita(impressao)
        self.assertEqual(impressao.expressao, "(((10-20)+(5-2))+((11+22)-(3+7)))")