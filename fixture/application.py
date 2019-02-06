# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.openSession import Page
from fixture.findTickets import Tickets
from fixture.getDate import Date
from fixture.search import Search
from fixture.closeSession import Close

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.openSession = Page(self)
        self.findTickets = Tickets(self)
        self.getDate = Date(self)
        self.search = Search(self)
        self.closeSession = Close(self)




