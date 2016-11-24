from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import page

#DOCKER HOST URL
DOCKER_HOST_IP = '192.168.0.88'

class GreenfieldTests(unittest.TestCase):
        
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get('http://' + DOCKER_HOST_IP + ':8080/greenfield/suite/')

    def tearDown(self):
        self.driver.close()

    def test_title(self):
        assert "Greenfield Test Management" in self.driver.title

    def test_add_new_suite(self):
        suite_list_page = page.SuiteListPage(self.driver)
        suite_list_page.add_suite('New test suite')
        assert suite_list_page.is_suite_exists('New test suite')

if __name__ == "__main__":
    unittest.main()
