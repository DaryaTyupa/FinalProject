import allure

from pages.http_steps import create_user, login_user, get_user_info, do_logout, del_user


@allure.story('Creation of new user')
def test_create_user():
    """This test checks creation of user by status_code and user_id"""
    new_user = {
        "id": 666,
        "username": "Group_1",
        "firstName": "Daria",
        "lastName": "Andrei",
        "email": "tms@tut.by",
        "password": "1234567890",
        "phone": "987654321",
        "userStatus": 0
    }
    with allure.step('Send request. Check the status code'):
        assert create_user(new_user).status_code == 200, 'wrong status code'
    with allure.step('Check user id in response body'):
        assert '666' in create_user(new_user).text, 'no such user id'


@allure.story('Login new user')
def test_login_user():
    """This test checks user login"""
    username = 'Group_1'
    password = '1234567890'
    with allure.step('Send request. Check the status code'):
        assert login_user(username, password).status_code == 200, 'wrong status code'
    with allure.step('Check message in response body'):
        assert 'logged in user session' in login_user(username, password).text, 'user wasn\'t login'


@allure.story('Get user information')
def test_get_user_info():
    """This test checks user information"""
    username = 'Group_1'
    with allure.step('Send request. Check the status code'):
        assert get_user_info(username).status_code == 200, 'wrong status code'
    with allure.step('Check user information in response body'):
        assert 'Daria' in get_user_info(username).text and 'Andrei' in get_user_info(
            username).text, 'no such user information'


@allure.story('User logout')
def test_user_logout():
    """This test checks user logout"""
    with allure.step('Send request. Check the status code'):
        assert do_logout().status_code == 200, 'wrong status code'
    with allure.step('Check message in response body'):
        assert 'ok' in do_logout().text, 'user wasn\'t logout'


@allure.story('Delete user')
def test_del_user():
    """This test checks user delete"""
    username = 'Group_1'
    with allure.step('Send request. Check the status code'):
        assert del_user(username).status_code == 200, 'wrong status code'
    with allure.step('Check the name of deleted user in response body'):
        assert 'Group_1' in del_user(username).text, 'user wasn\'t delete'
