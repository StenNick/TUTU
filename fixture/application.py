# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver # единожды передаем вызов вэбдрайвера и используем его в фикстурах
from fixture.openSession import Page
from fixture.findTickets import Tickets
from fixture.getDate import Date
from fixture.search import Search
from fixture.closeSession import Close
# тут у нас вызываемые фикстуры

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)
        self.openSession = Page(self) # тут дали досту к драйверу модулю SessionHelper
        self.findTickets = Tickets(self)
        self.getDate = Date(self)
        self.search = Search(self)
        self.closeSession = Close(self)


"""
в __init'e__ мы вызываем модули и передаем их как вызов функций из фикстур
для их вызова мы импортируем модули из папки fixture в наш модуль Application
каждая фикстура выполняет свою роль, порядок вызова играет роль лишь в модуле test\ test_init_tests.py

"""




