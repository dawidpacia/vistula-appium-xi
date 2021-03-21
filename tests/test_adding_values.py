value_1 = 1
value_2 = 8


class TestCalculator:

    def test_add_value(self, driver):
        driver.find_element_by_id(f"digit_{value_1}").click()
        driver.find_element_by_id("op_add").click()
        driver.find_element_by_id(f"digit_{value_2}").click()
        driver.find_element_by_accessibility_id("equals").click()
        result = driver.find_element_by_id("result_final").text

        assert value_1 + value_2 == int(result)

    def test_divide_value(self, driver):
        driver.find_element_by_id(f"digit_{value_1}").click()
        driver.find_element_by_id("op_div").click()
        driver.find_element_by_id(f"digit_{value_2}").click()
        driver.find_element_by_accessibility_id("equals").click()
        result = driver.find_element_by_id("result_final").text

        assert value_1 / value_2 == float(result)

    def test_sub_value(self, driver):
        driver.find_element_by_id(f"digit_{value_1}").click()
        driver.find_element_by_id("op_sub").click()
        driver.find_element_by_id(f"digit_{value_2}").click()
        result = driver.find_element_by_id("result_final").text

        assert str(value_1 - value_2) == result