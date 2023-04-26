from Pages.main_page import MainPage
from Pages.filter_page import Filter



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.filter_page = Filter(self.driver)
        self.main_page = MainPage(self.driver)

