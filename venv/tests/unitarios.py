import unittest
import tkinter as tk
import calculator_factories


class TestCalculatorFactories(unittest.TestCase):

    def test_makeapp(self):
        self.assertIsInstance(calculator_factories.make_app(), tk.Tk)


if __name__ == '__main__':
    unittest.main()
