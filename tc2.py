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
        desired_caps['app'] = PATH('C:\APP\ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['noReset'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_fill_form(self):
        self.driver.find_element_by_xpath("//android.widget.Button[@text='Add Contact']").click()
        contact_name = self.driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
        contact_name.send_keys('Julia')
        contact_number = self.driver.find_element_by_id("contactPhoneEditText")
        contact_number.send_keys('123456')
        contact_mail = self.driver.find_element_by_id("contactEmailEditText")
        contact_mail.send_keys('julia@wp.pl')

        self.assertEqual("Julia", contact_name.text)
        self.assertEqual("123456", contact_number.text)
        self.assertEqual("julia@wp.pl", contact_mail.text)

        self.driver.find_element_by_xpath("//android.widget.Button[@text='Save']").click()
        sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApplication)
    unittest.TextTestRunner(verbosity=2).run(suite)
