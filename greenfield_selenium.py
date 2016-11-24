from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

#DOCKER HOST URL
DOCKER_HOST_IP = '192.168.0.88'

class GreenfieldTests(unittest.TestCase):
        
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

    def tearDown(self):
        self.driver.close()

    def test_title(self):
        driver = self.driver
        driver.get('http://' + DOCKER_HOST_IP + ':8080/greenfield/suite/')
        assert "Greenfield Test Management" in driver.title

if __name__ == "__main__":
    unittest.main()
