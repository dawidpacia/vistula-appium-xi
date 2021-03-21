import os
from appium import webdriver

# Returns abs path relative to this file and not cwd
app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

print(app_path)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['newCommandTimeout'] = 250
desired_caps['app'] = app_path

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("formula").click()
driver.find_element_by_accessibility_id("More options").click()
print("stop")
driver.quit()