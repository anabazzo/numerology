from numerologia import calcula_nome
import unittest

class TesteNumerologia(unittest.TestCase):

  def test_calculo(self):
    self.assertEqual(calcula_nome(), True)

if __name__ == '__main__':
    unittest.main()
