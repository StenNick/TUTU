# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest


class test_init_main_test(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.wd.maximize_window()

    def test_group(self):
        wd = self.wd
        wd.get("https://www.tutu.ru/")
        wd.find_element_by_class_name("tab_avia").click()
        time.sleep(1)
        wd.find_element_by_name("city_from").clear()
        wd.find_element_by_name("city_from").send_keys("Москва")
        time.sleep(1)
        wd.find_element_by_name("city_to").clear()
        wd.find_element_by_name("city_to").send_keys("Санкт-Петербург")
        time.sleep(1)

        wd.find_element_by_name("date_from").click()
        wd.find_element_by_name("date_from").send_keys("25.03.2019")
        time.sleep(1)
        wd.find_element_by_name("date_back").click()
        wd.find_element_by_name("date_back").send_keys("05.05.2019")



        # passengers
        wd.find_element_by_class_name("increase").click()

        # find tickets
        wd.find_element_by_class_name("j-submit_button")


    def tearDown(self):
        self.wd.quit()


if __name__=='__main__':
    unittest.main()