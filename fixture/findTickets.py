class Tickets:

    def __init__(self, app):
        self.app = app

    def find_teckets(self, city_from, city_to):
        wd = self.app.wd
        wd.find_element_by_class_name("tab_avia").click()
        wd.find_element_by_name("city_from").clear()
        wd.find_element_by_name("city_from").send_keys(city_from)
        wd.find_element_by_name("city_to").clear()
        wd.find_element_by_name("city_to").send_keys(city_to)
        # passengers
        wd.find_element_by_class_name("increase").click()


