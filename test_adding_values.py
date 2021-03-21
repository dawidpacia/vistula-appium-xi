

import os
from appium import webdriver

# Returns abs path relative to this file and not cwd
# app_name = "calculator.apk"
# app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))
#
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['newCommandTimeout'] = 250
# desired_caps['app'] = app_path
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


value_1 = 2
value_2 = 3


def test_add_value(driver):
    driver.find_element_by_id(f"digit_{value_1}").click()
    driver.find_element_by_id("op_add").click()
    driver.find_element_by_id(f"digit_{value_2}").click()
    driver.find_element_by_accessibility_id("equals").click()
    result = driver.find_element_by_id("result_final").text

    assert value_1 + value_2 == int(result)

def test_add_value_2(driver):
    driver.find_element_by_id(f"digit_{value_1}").click()
    driver.find_element_by_id("op_add").click()
    driver.find_element_by_id(f"digit_{value_2}").click()
    driver.find_element_by_accessibility_id("equals").click()
    result = driver.find_element_by_id("result_final").text

    assert value_1 + value_2 == int(result)
