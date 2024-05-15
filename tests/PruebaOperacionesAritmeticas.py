import unittest
from src.OperacionesAritmeticas import OperacionesAritmeticas

class PruebasOperacionesAritmeticas(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operacion = OperacionesAritmeticas()
        sumando1 = 12
        sumando2 = 14
        resultadoEsperado = 26

        #Do
        resultadoActual = operacion.suma(sumando1, sumando2)


        #Assert
        self.assertEqual(resultadoEsperado, resultadoActual)  # add assertion here

    def test_resta_dosNumeros_retornaResta(self):
        # Arrange
        operacion = OperacionesAritmeticas()
        minuendo = 12
        sustraendo = 14
        resultadoEsperado = -2

        # Do
        resultadoActual = operacion.resta(minuendo, sustraendo)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
