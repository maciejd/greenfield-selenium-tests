from locators import SuiteListLocators

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class SuiteListPage(BasePage):
    
    def add_suite(self, title):
        element = self.driver.find_element(*SuiteListLocators.SUITE_TITLE_FIELD)
        element.send_keys(title)
        element.submit()

    def is_suite_exists(self, title):
        table = self.driver.find_element(*SuiteListLocators.SUITE_LIST_TABLE)
        return title in table.text
