'''
Mateus Henrique Alves da Silva - 1801536
'''

import calculadora
from unittest import TestCase
import unittest

apontarErro = False


class Testes(TestCase):
    def testeSoma1(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(31, 24, "soma")
        self.assertEqual(result, 55)

    def testeSoma2(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(10, 20, "soma")
        self.assertEqual(result, 30)

    def testeSoma3(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(1000, 666, "soma")
        self.assertEqual(result, 1666)

    def testeSoma4(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(231, 232, "soma")
        self.assertEqual(result, 463)

    def testeSoma5(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(1356.54, 1245.77, "soma")
        self.assertEqual(result, 2602.31)

    def testeSubtracao1(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(10, 105, "subtracao")
        self.assertEqual(result, -95)

    def testeSubtracao2(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(50, 50, "subtracao")
        self.assertEqual(result, 0)

    def testeSubtracao3(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(500, 400, "subtracao")
        self.assertEqual(result, 100)

    def testeSubtracao4(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(333, 33, "subtracao")
        self.assertEqual(result, 300)

    def testeSubtracao5(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(1625.41, 852.32, "subtracao")
        self.assertEqual(result, 773.09)

    def testeMultiplicacao1(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(50, 3, "multiplicacao")
        self.assertEqual(result, 150)

    def testeMultiplicacao2(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(18, 7, "multiplicacao")
        self.assertEqual(result, 126)

    def testeMultiplicacao3(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(1000, 1000, "multiplicacao")
        self.assertEqual(result, 1000000)

    def testeMultiplicacao4(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(39, 51, "multiplicacao")
        self.assertEqual(result, 1989)

    def testeMultiplicacao5(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(42.2, 12.5, "multiplicacao")
        self.assertEqual(result, 527.5)

    def testeDivisao1(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(250, 4, "divisao")
        self.assertEqual(result, 62.5)

    def testeDivisao2(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(36, 9, "divisao")
        self.assertEqual(result, 4)

    def testeDivisao3(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(1000, 8, "divisao")
        self.assertEqual(result, 125)

    def testeDivisao4(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(2706, 12, "divisao")
        self.assertEqual(result, 225.5)

    def testeDivisao5(self):
        calcular = calculadora.Calculadora()
        result = calcular.calcular(781, 782, "divisao")
        self.assertEqual(result, 0.9987212276214834)


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Testes)
    unittest.TextTestRunner(verbosity=2,
                            failfast=apontarErro).run(suite)


if __name__ == "__main__":
    runTests()
