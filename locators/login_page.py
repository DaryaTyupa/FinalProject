from FinalTask.FinalProgect.constans import USERNAME_LOGIN, PASSWORD_LOGIN
from FinalTask.FinalProgect.locators.login_page_locators import LoginPageLocators
from FinalTask.FinalProgect.pages.admin_page import AdminPage
from FinalTask.FinalProgect.pages.base_page import BasePage


class LoginPage(BasePage):

    def try_to_login(self):
        username_field = self.find_element(LoginPageLocators.USERNAME_FIELD_LOCATOR)
        username_field.send_keys(USERNAME_LOGIN)
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(PASSWORD_LOGIN)
        login_btn = self.find_element(LoginPageLocators.LOGIN_BTN_LOCATOR)
        login_btn.click()
        return AdminPage(self.driver, self.driver.current_url)
   