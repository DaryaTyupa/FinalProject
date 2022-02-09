import requests
from allure_commons._allure import step


def create_user(new_user):
    response = requests.post('https://petstore.swagger.io/v2/user', json=new_user)
    return response


def login_user(username, password):
    response = requests.get(f'https://petstore.swagger.io/v2/user/login?username={username}&password={password}')
    return response


def get_user_info(username):
    response = requests.get(f'https://petstore.swagger.io/v2/user/{username}')
    return response


def do_logout():
    response = requests.get('https://petstore.swagger.io/v2/user/logout')
    return response


def del_user(username):
    response = requests.delete(f'https://petstore.swagger.io/v2/user/{username}')
    return response
