from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username_field = By.ID, "username"
        self.password_field = By.ID, "password"
        self.login_button = By.XPATH, "//button[@type='submit']"
        self.success_message = By.ID, "//*[@id='account-detail-section']/div[1]/h1"

    def enter_username(self, username):
        self.wait_for_element(self.username_field).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.password_field).send_keys(password)

    def click_login(self):
        self.wait_for_element(self.login_button).click()

    def is_login_successful(self):
        try:
            self.wait_for_element(self.success_message)
            return True
        except TimeoutException:
            return False


