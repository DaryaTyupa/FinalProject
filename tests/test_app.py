import allure
from FinalTask.FinalProgect.pages.db_steps import create_group, get_group_name
from FinalTask.FinalProgect.pages.main_page import MainPage


@allure.story('Creation of new group using database')
def test_group(driver, connect_to_db):
    """This test checks creation of group with db
    and displaying this group on admin page"""
    create_group(connect_to_db, ['Group_1'])
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open login page'):
        login_page = page.open_login_page()
    with allure.step('Login user and redirect to admin page'):
        admin_page = login_page.try_to_login()
    with allure.step('Open groups on admin page'):
        admin_groups = admin_page.open_groups()
    with allure.step('Check the created group is displayed on admin page'):
        assert 'Group_1' in admin_groups.get_first_group().text, 'no such group created'


@allure.story('Changing the group name on admin page')
def test_change_group_name(driver, connect_to_db):
    """This test checks the name of group in db after
    changing this name on admin page"""
    page = MainPage(driver)
    with allure.step('Open main page'):
        page.open()
    with allure.step('Open admin page'):
        admin_page = page.open_admin_page()
    with allure.step('Open groups on admin page'):
        admin_groups = admin_page.open_groups()
    with allure.step('Change group name'):
        change_group = admin_groups.open_change_group()
        name_field = change_group.get_group_name_field()
        name_field.send_keys('_changed')
        change_group.click_save_btn()
    with allure.step('Check the changed group name in database'):
        assert 'Group_1_changed' in get_group_name(connect_to_db)[0], 'no such group changed'

pytest tests/ --reruns 2
pytest-rerunfailures==4.1