from selenium.webdriver.common.by import By
from Pages.Base_page import Page



class MainPage(Page):

    def open_cureskin(self):
        self.open_url('https://www.cureskin.com/')

    def search_page(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')


