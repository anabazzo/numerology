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
    self.assertEqual(calcula_nome('ana claudia'), 31)

  def test_calculo_joao(self):
    self.assertEqual(calcula_nome('jõãõ'), 14)

if __name__ == '__main__':
    unittest.main()
