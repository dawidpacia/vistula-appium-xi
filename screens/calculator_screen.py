class CalculatorScreen:

    def __init__(self, driver):
        self.driver = driver

    def add_values(self, value_1, value_2):
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id("op_add").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()

    def divide_values(self, value_1, value_2):
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id("op_div").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()

    def sub_values(self, value_1, value_2):
        self.driver.find_element_by_id(f"digit_{value_1}").click()
        self.driver.find_element_by_id("op_sub").click()
        self.driver.find_element_by_id(f"digit_{value_2}").click()

    def get_result(self):
        self.driver.find_element_by_accessibility_id("equals").click()
        result = self.driver.find_element_by_id("result_final").text
        result = result.replace("−", "-")
        return result
