import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class TestLiaoyuan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get("http://www.google.com")
        self.username = "dsk932015@gmail.com"
        self.password = "Dsk930123"

    def tearDown(self):
        self.driver.close()
        pass

    def test_search_liaoyuan(self):
        main_page = page.google_main_page(self.driver)
        main_page.search_input("燎原")
        main_page.click_search_button()

        result_page = page.google_result_page(self.driver)
        verify_page = result_page.search_liaoyuan()
        
        get_liaoyuan = page.liaoyuan_main_page(self.driver)
        get_liaoyuan.verify_liaoyuan()
        get_liaoyuan.click_login()

    def test_liaoyuan_login(self):
        test_login = page.login_page(self.driver)
        test_login.login_username(self.username)
        test_login.login_password(self.password)
        test_login.click_login_button()


if __name__ == "__main__":
    unittest.main() # run all tests
