import allure

from pages.http_steps import create_user, login_user, get_user_info, do_logout, del_user


@allure.story('Creation of new user')
def test_create_user():
    """This test checks creation of user by status_code and user_id"""
    new_user = {
        "id": 666,
        "username": "Username_1",
        "firstName": "Daria",
        "lastName": "Tyupa",
        "email": "tms@tut.by",
        "password": "1234567890",
        "phone": "987654321",
        "userStatus": 0
    }
    response = create_user(new_user)
    with allure.step('Send request. Check the status code'):
        assert response.status_code == 200, 'wrong status code'
    with allure.step('Check user id in response body'):
        assert '666' in response.text, 'no such user id'


@allure.story('Login new user')
def test_login_user():
    """This test checks user login"""
    username = 'Username_1'
    password = '1234567890'
    response = login_user(username, password)
    with allure.step('Send request. Check the status code'):
        assert response.status_code == 200, 'wrong status code'
    with allure.step('Check message in response body'):
        assert 'logged in user session' in response.text, 'user wasn\'t login'


@allure.story('Get user information')
def test_get_user_info():
    """This test checks user information"""
    username = 'Username_1'
    response = get_user_info(username)
    with allure.step('Send request. Check the status code'):
        assert response.status_code == 200, 'wrong status code'
    with allure.step('Check user information in response body'):
        assert 'Daria' in response.text and 'Tyupa' in response.text, 'no such user information'


@allure.story('User logout')
def test_user_logout():
    """This test checks user logout"""
    response = do_logout()
    with allure.step('Send request. Check the status code'):
        assert response.status_code == 200, 'wrong status code'
    with allure.step('Check message in response body'):
        assert 'ok' in response.text, 'user wasn\'t logout'


@allure.story('Delete user')
def test_del_user():
    """This test checks user delete"""
    username = 'Username_1'
    response = del_user(username)
    with allure.step('Send request. Check the status code'):
        assert response.status_code == 200, 'wrong status code'
    with allure.step('Check the name of deleted user in response body'):
        assert username in response.text, 'user wasn\'t delete'
