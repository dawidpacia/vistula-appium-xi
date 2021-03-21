import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


# Returns abs path relative to this file and not cwd
app_name = "calculator.apk"
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

print(app_path)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['newCommandTimeout'] = 250
desired_caps['app'] = app_path
desired_caps['autoGrantPermissions'] = True
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


driver.find_element_by_id("digit_2")
driver.find_element_by_accessibility_id("equals")
driver.find_element_by_xpath('//android.widget.Button[@content-desc="equals"]')
# driver.find_elements_by_class_name('android.widget.Button')
# driver.find_element_by_css_selector("[content-desc='degree mode']")
driver.find_element_by_android_uiautomator("UiSelector().text(\"DEG\")")

actions = TouchAction(driver)
actions.tap(x=1030, y=1500)
actions.perform()



driver.quit()
