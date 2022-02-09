import requests
from allure_commons._allure import step


def create_user(new_user):
    return requests.post('https://petstore.swagger.io/v2/user', json=new_user)


def login_user(username, password):
    return requests.get(f'https://petstore.swagger.io/v2/user/login?username={username}&password={password}')


def get_user_info(username):
    return requests.get(f'https://petstore.swagger.io/v2/user/{username}')


def do_logout():
    return requests.get('https://petstore.swagger.io/v2/user/logout')


def del_user(username):
    return requests.delete(f'https://petstore.swagger.io/v2/user/{username}')
