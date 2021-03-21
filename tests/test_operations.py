class TestCalculator:

    def test_add_value(self, calculator):
        calculator.add_values(1, 2)
        result = calculator.get_result()
        assert int(result) == 3

    def test_divide_value(self, calculator):
        calculator.divide_values(1, 2)
        result = calculator.get_result()
        assert float(result) == 0.5

    def test_sub_value_positive(self, calculator):
        calculator.sub_values(5, 1)
        result = calculator.get_result()
        assert result == "4"

    def test_sub_value_negative(self, calculator):
        calculator.sub_values(1, 5)
        result = calculator.get_result()
        assert result == "-4"
