class Page:

    def __init__(self, app):
        self.app = app

    def openPage(self, url_page):
        wd = self.app.wd
        wd.get(url_page)

