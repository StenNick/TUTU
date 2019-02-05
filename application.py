# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def openPage(self):
        wd = self.wd
        wd.get("https://www.tutu.ru/")

    def find_teckets(self, city_from, city_to):
        wd = self.wd
        wd.find_element_by_class_name("tab_avia").click()
        wd.find_element_by_name("city_from").clear()
        wd.find_element_by_name("city_from").send_keys(city_from)
        wd.find_element_by_name("city_to").clear()
        wd.find_element_by_name("city_to").send_keys(city_to)
        # passengers
        wd.find_element_by_class_name("increase").click()

    def check_date(self, date_from, date_back):
        wd = self.wd
        wd.find_element_by_name("date_from").click()
        wd.find_element_by_name("date_from").send_keys(date_from)
        wd.find_element_by_name("date_back").click()
        wd.find_element_by_name("date_back").send_keys(date_back)

    def search(self):
        wd = self.wd
        wd.find_element_by_class_name("j-submit_button")


    def closeBrowser(self):
        self.wd.quit()


