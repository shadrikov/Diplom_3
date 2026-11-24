import requests
from data import URLs
import allure

class ApiClient:
    @staticmethod
    @allure.step("Отправляем POST-запрос на регистрацию пользователя")
    def post_request_create_user(payload):
        url = URLs.CREATE_USER
        return requests.post(url, data=payload)

    @staticmethod
    @allure.step("Отправляем DELETE-запрос на удаление пользователя")
    def request_delete_user(access_token):
        url = URLs.DELETE_USER
        return requests.delete(url, headers={'Authorization': access_token})

    @staticmethod
    @allure.step("Отправляем POST-запрос на создание заказа")
    def post_request_create_order(payload, access_token=None):
        headers = {}
        if access_token is not None:
            headers['Authorization'] = access_token
        return requests.post(URLs.CREATE_ORDER, json=payload, headers=headers)

    @staticmethod
    @allure.step("Отправляем GET-запрос на получение данных об ингредиентах")
    def get_request_get_ingredients():
        url = URLs.GET_INGREDIENTS
        return requests.get(url)