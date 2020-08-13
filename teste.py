from numerologia import calcula_nome
import unittest

class TesteNumerologia(unittest.TestCase):

  def test_calculo_a(self):
    self.assertEqual(calcula_nome('a'), 1)

  def test_calculo_b(self):
    self.assertEqual(calcula_nome('b'), 2)

  def test_calculo_ana(self):
    self.assertEqual(calcula_nome('ana'), 7)

  def test_calculo_anaclaudia(self):
    self.assertEqual(calcula_nome('ana claudia'), 4)

  def test_calculo_joao(self):
    self.assertEqual(calcula_nome('jõãõ'), 5)

  def test_calculo_ane(self):
    self.assertEqual(calcula_nome('anè'), 11)

  def test_calculo_enio(self):
    self.assertEqual(calcula_nome('ënìõ'), 7)

  def test_calculo_luis(self):
    self.assertEqual(calcula_nome('luis'), 7)

if __name__ == '__main__':
    unittest.main()
