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


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test_is_notification_test(self):
        self.driver.open_notifications()
        sleep(2)
        list = self.driver.find_elements_by_class_name("android.widget.TextView")
        sleep(3)
        title = False
        body = False
        for el in list:
            #print el
            text = el.text

            if text == 'USB debugging connected':
                print text
                title = True

            elif text == 'Tap to disable USB debugging.':
                print text
                body = True

        self.assertTrue(title)
        self.assertTrue(body)

        self.driver.press_keycode(4)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingApplication)
    unittest.TextTestRunner(verbosity=2).run(suite)
