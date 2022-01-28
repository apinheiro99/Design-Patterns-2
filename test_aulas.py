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