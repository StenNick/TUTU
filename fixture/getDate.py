class Date:

    def __init__(self, app):
        self.app = app

    def check_date(self, date_from, date_back):
        wd = self.app.wd
        wd.find_element_by_name("date_from").click()
        wd.find_element_by_name("date_from").send_keys(date_from)
        wd.find_element_by_name("date_back").click()
        wd.find_element_by_name("date_back").send_keys(date_back)