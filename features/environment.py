import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from App.Application import Application




def browser_init(context,test_internship):
    """
    :param context: Behave context
    """
    #chrome
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    #firefox
    service = Service('/Users/shailakshigupta/Desktop/Automation/Internship/CureSkin/python-selenium-internship_skincare/geckodriver')
    #context.driver = webdriver.Firefox(service=service)

    #Browserstack

    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': test_internship
        }
    }
    bs_user = 'shailakshigupta_4TDvia'
    bs_key = 'RhTQonfqSMEE9uXiwRmw'

    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)



    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')

    #context.driver = webdriver.Chrome(chrome_options=options,service=service)

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.App = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)



def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)



def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()