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