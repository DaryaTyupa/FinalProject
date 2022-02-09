from selenium.webdriver.common.by import By


class AdminPageLocators():

    GROUPS_LINK_LOCATOR = (By.XPATH, "//*[@href='/admin/auth/group/']")
    FIRST_GROUP_LOCATOR = (By.XPATH, "//*[@class='field-__str__']//a")
    NAME_FIELD_LOCATOR = (By.XPATH, "//*[@id='id_name']")
    SAVE_GROUP_BTN_LOCATOR = (By.XPATH, "//*[@value='Save']")