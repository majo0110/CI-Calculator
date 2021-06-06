"""
Test for calculator app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 15 == calculator.add(10,5)

    def test_subtract(self):
        assert 20 == calculator.subtract(30,10)

    def test_multiply(self):
        assert 45 == calculator.multiply(15,3)

    def test_divide(self):
        assert 10 == calculator.divide(100,10)
