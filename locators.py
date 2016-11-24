from selenium.webdriver.common.by import By

class SuiteListLocators(object):

    SUITE_TITLE_FIELD = (By.ID, 'title')
    SUITE_LIST_TABLE = (By.XPATH, '//table')
