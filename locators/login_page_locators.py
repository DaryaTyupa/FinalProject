from selenium.webdriver.common.by import By


class LoginPageLocators():

    USERNAME_FIELD_LOCATOR = (By.XPATH, "//*[@id='id_username']")
    PASSWORD_FIELD_LOCATOR = (By.XPATH, "//*[@id='id_password']")
    LOGIN_BTN_LOCATOR = (By.XPATH, "//*[@value='Log in']")
