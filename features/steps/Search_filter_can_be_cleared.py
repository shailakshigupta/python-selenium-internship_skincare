from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open cureskin page')
def open_cureskin(context):
    context.driver.get('https://www.cureskin.com/')

@when('Open search results page')
def search_page(context):
    context.driver.get('https://shop.cureskin.com/search?q=cure')
    #context.driver.find_element(By.XPATH,'//input[@id="Search-In-Template"]')


@when('Click More Filters - Facewash')
def more_filters(context):
    #context.driver.find_element(By.XPATH, "//facet-drawer[@id='FacetDrawer']").click()
    #sleep(2)
    context.App.filter_page.more_filters()


@when('Click on facewash')
def select_facewash(context):
    #context.driver.find_element(By.XPATH,"//label[@class='facet-checkbox' and @for='Filter-Product type-1']" ).click()
    sleep(2)
    context.App.filter_page.select_facewash()

@when('Click on apply')
def apply(context):
    #context.driver.find_element(By.XPATH,"//button[@class='no-js-hidden button button--small']").click()
    sleep(2)
    context.App.filter_page.apply()

@when('Verify filter is "{expected_result}" set')
def filter_is_set(context,expected_result):
    context.App.filter_page.filter_is_set(expected_result)
    #filter = context.driver.find_element(By.XPATH,"//a[@href='/search?options%5Bprefix%5D=last&q=cure&sort_by=relevance' and @class='active-facets__button']" ).text
    #print(filter)
    #assert filter == Face Wash, f'Expected Face Wash, but got {filter}'


@when('Click to "clear all"')
def clear_all(context):
    #context.driver.find_element(By.XPATH,"//a[@href='?q=cure&options%5Bprefix%5D=last&sort_by=relevance' and @class='active-facets__button active-facets__button--dark']" ).click()
    sleep(2)
    context.App.filter_page.clear_all()



@then("Verify filter is removed with '{expected_result}'")
def filter_removed(context,expected_result):
    context.App.filter_page.filter_removed(expected_result)
    #no_filter = context.driver.find_element(By.XPATH,"//p[text()='18 results found for “cure”' and @id='ProductCount']" ).text
    #print(no_filter)
    sleep(2)


