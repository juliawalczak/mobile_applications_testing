import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestingApplication(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('C:\APP\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        desired_caps['noReset'] = 'true'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_is_preference_clickable(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Preference']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='3. Preference dependencies']").click()
        checkbox = self.driver.find_element_by_xpath("//android.widget.CheckBox[@index='0']")
        is_checked = self.driver.find_element_by_xpath("//android.widget.CheckBox[@index='0']").get_attribute('checked')
        if is_checked == 'false':
            checkbox.click()

        list_checkbox = self.driver.find_elements_by_class_name("android.widget.CheckBox")
        print('Amount of checkboxes: ')
        checkbox_amount = len(list_checkbox)
        print(checkbox_amount)

        self.driver.find_element_by_xpath("//android.widget.TextView[@text='WiFi settings']").click()
        password = self.driver.find_element_by_xpath("//android.widget.TextView")
        password.send_keys('1234')
        self.driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
        self.driver.find_elements_by_class_name("android.widget.CheckBox")
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApplication)
    unittest.TextTestRunner(verbosity=2).run(suite)
