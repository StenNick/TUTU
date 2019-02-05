"""
тут нету вызова webdriver'a
для доступа к драйверу, мы обращаемся к модулю Application
данный модуль мы вызываем в __init__ модуля Application
после чего получаем доступ к драйверу
"""
class Page:

    def __init__(self, app): # этот модуль вызвали в Application, и ссылаемся на него для вызова драйвера
        self.app = app

    def openPage(self, url_page):
        wd = self.app.wd # обращаемся к модулую Application
        wd.get(url_page)

