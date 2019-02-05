class Close:

    def __init__(self, app):
        self.app = app

    def closeBrowser(self):
        wd = self.app.wd
        wd.quit()
