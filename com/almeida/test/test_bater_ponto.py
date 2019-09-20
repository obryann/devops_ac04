from unittest import TestCase
from com.almeida.bater_ponto import BaterPonto

class test_BaterPonto(TestCase):

    def setUp (self):
        self.bater_ponto = BaterPonto()
    
    def test_soma(self):
        self.assertEqual(self.bater_ponto.soma(2), 4, "Should be 4")