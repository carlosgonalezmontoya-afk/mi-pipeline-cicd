import unittest
from app import saludar

class TestApp(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludar("Carlos"), "Hola, Carlos")

if __name__ == '__main__':
    unittest.main()