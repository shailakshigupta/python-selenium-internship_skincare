from selenium.webdriver.common.by import By
from Pages.Base_page import Page




class Filter(Page):
    filter_search = (By.XPATH, "//facet-drawer[@id='FacetDrawer']")
    face_wash = (By.XPATH,"//label[@class='facet-checkbox' and @for='Filter-Product type-1']")
    apply_filter = (By.XPATH,"//button[@class='no-js-hidden button button--small']")
    set_filter = (By.XPATH,"//a[@href='/search?options%5Bprefix%5D=last&q=cure&sort_by=relevance' and @class='active-facets__button']")
    clear_filter = (By.XPATH,"//a[@href='?q=cure&options%5Bprefix%5D=last&sort_by=relevance' and @class='active-facets__button active-facets__button--dark']")
    remove_filter = (By.XPATH,"//p[text()='18 results found for “cure”' and @id='ProductCount']")


    def more_filters(self):
        self.click(*self.filter_search)

    def select_facewash(self):
        self.click(*self.face_wash)

    def apply(self):
        self.click(*self.apply_filter)


    def filter_is_set(self,expected_text):
        actual_result = self.driver.find_element(*self.set_filter).text
        assert expected_text == actual_result, f'Expected_result {expected_text}but got this as Actual_result {actual_result}'

    def clear_all(self):
        self.click(*self.clear_filter)

    def filter_removed(self, expected_text):
        actual_result = self.driver.find_element(*self.remove_filter).text
        assert expected_text == actual_result, f'Expected_result {expected_text}but got this as Actual_result {actual_result}'


