from FinalTask.SDA.locators.admin_page_locators import AdminPageLocators
from FinalTask.SDA.pages.base_page import BasePage


class AdminPage(BasePage):

    def open_groups(self):
        groups_link = self.find_element(AdminPageLocators.GROUPS_LINK_LOCATOR)
        groups_link.click()
        return AdminPage(self.driver, self.driver.current_url)

    def get_first_group(self):
        return self.find_element(AdminPageLocators.FIRST_GROUP_LOCATOR)

    def open_chage_group(self):
        group_link = AdminPage.get_first_group(self)
        group_link.click()
        return AdminPage(self.driver, self.driver.current_url)

    def get_group_name_field(self):
        return self.find_element(AdminPageLocators.NAME_FIELD_LOCATOR)

    def click_save_btn(self):
        save_btn = self.find_element(AdminPageLocators.SAVE_GROUP_BTN_LOCATOR)
        save_btn.click()
        return AdminPage(self.driver, self.driver.current_url)