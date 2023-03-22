import unittest
from selenium import webdriver

class SauceDemoTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_empty_username_password(self):
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element_by_id("user-name")
        password_input = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        username_input.send_keys("")
        password_input.send_keys("")
        login_button.click()
        error_message = self.driver.find_element_by_css_selector("h3[data-test='error']")
        self.assertEqual("Epic sadface: Username is required", error_message.text)

    def test_empty_password(self):
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element_by_id("user-name")
        password_input = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        username_input.send_keys("standard_user")
        password_input.send_keys("")
        login_button.click()
        error_message = self.driver.find_element_by_css_selector("h3[data-test='error']")
        self.assertEqual("Epic sadface: Password is required", error_message.text)

    def test_locked_user(self):
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element_by_id("user-name")
        password_input = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        username_input.send_keys("locked_out_user")
        password_input.send_keys("secret_sauce")
        login_button.click()
        error_message = self.driver.find_element_by_css_selector("h3[data-test='error']")
        self.assertEqual("Epic sadface: Sorry, this user has been locked out.", error_message.text)

    #def test_red_x_icon(self):
        #self.driver.get("https://www.saucedemo.com/")
        #username_input = self.driver.find_element_by_id("user-name")
        #password_input = self.driver.find_element_by_id