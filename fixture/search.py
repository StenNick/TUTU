class Search:

    def __init__(self, app):
        self.app = app

    def search(self):
        wd = self.app.wd
        wd.find_element_by_class_name("j-submit_button")