import unittest
from palabrasecreta import PalabraSecreta


class TestStringMethods(unittest.TestCase):

    def test_palabra_0_aciertos(self):
        p = PalabraSecreta('PERRO')
        self.assertEqual(p.__repr__(), '_ _ _ _ _')

    def test_palabra_1_acierto(self):
        p = PalabraSecreta('PERRO')
        p.adivinarLetra('E')
        self.assertEqual(p.__repr__(), '_ E _ _ _')

    def test_palabra_2_acierto(self):
        p = PalabraSecreta('PERRO')
        p.adivinarLetra('E')
        p.adivinarLetra('R')
        self.assertEqual(p.__repr__(), '_ E R R _')

    def test_palabra_2_acierto_1_fallo(self):
        p = PalabraSecreta('PERRO')
        p.adivinarLetra('E')
        p.adivinarLetra('R')
        p.adivinarLetra('A')
        self.assertEqual(p.__repr__(), '_ E R R _')

    def test_no_esta_completa(self):
        p = PalabraSecreta('PERRO')
        p.adivinarLetra('E')
        p.adivinarLetra('P')
        p.adivinarLetra('O')
        self.assertFalse(p.estaCompleta())

    def test_esta_completa(self):
        p = PalabraSecreta('PERRO')
        p.adivinarLetra('E')
        p.adivinarLetra('R')
        p.adivinarLetra('P')
        p.adivinarLetra('O')
        self.assertTrue(p.estaCompleta())

    def test_crear_palabra_secreta(self):
        p = PalabraSecreta.elegirAleatoria()
        print(p)
        self.assertIsInstance(p, PalabraSecreta)

if __name__ == '__main__':
    unittest.main()