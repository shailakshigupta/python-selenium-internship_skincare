from selenium.webdriver.common.by import By
from Pages.Base_page import Page
from selenium.webdriver.support import expected_conditions as EC, wait



class Filter(Page):
    #filter_search = (By.XPATH, "//facet-drawer[@id='FacetDrawer']")
    filter_search = (By.CSS_SELECTOR, ".mobile-facets__wrapper")
    face_wash = (By.CSS_SELECTOR,".mobile-facets__label")
    apply_filter = (By.CSS_SELECTOR, "div.no-js-hidden.mobile-facets__footer button")
    # set_filter = (By.XPATH,"//a[@href='/search?options%5Bprefix%5D=last&q=cure&sort_by=relevance' and @class='active-facets__button']")
    set_filter = (By.CSS_SELECTOR, 'a.active-facets__button[href*="/search?q=cure&sort_by=relevance"]')
    clear_filter = (By.XPATH,"//a[@href='?q=cure&options%5Bprefix%5D=last&sort_by=relevance' and @class='active-facets__button active-facets__button--dark']")
    remove_filter = (By.XPATH,"//p[text()='18 results found for “cure”' and @id='ProductCount']")
    product_type = (By.XPATH,'//details[@class="mobile-facets__details js-filter" and @data-index="mobile-1"]')
    filter_search_mobile = (By.XPATH,'//span[@class="mobile-facets__open button button--small button--full-width"]')

    def more_filters(self):
        self.click(*self.filter_search)

    def more_filters_mobile(self):
        #self.click(*self.filter_search_mobile)
        self.wait_for_element_click(*self.filter_search_mobile)

    def product(self):
        self.click(*self.product_type)

    def select_facewash(self):
        self.wait_for_element_click(By.XPATH, '//summary[@class="mobile-facets__summary"]//span[contains(text(), "Product type")]')
        self.wait_for_element_click(*self.face_wash)

    def click_on_apply(self):
        self.wait_for_element_click(*self.apply_filter)

    def filter_is_set(self,expected_text):
        actual_result = self.driver.find_element(*self.set_filter).text
        assert expected_text == actual_result, f'Expected_result {expected_text}but got this as Actual_result {actual_result}'

    def clear_all(self):
        self.click(*self.clear_filter)

    def filter_removed(self, expected_text):
        actual_result = self.driver.find_element(*self.remove_filter).text
        assert expected_text == actual_result, f'Expected_result {expected_text}but got this as Actual_result {actual_result}'


