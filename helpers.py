import allure
from api_client import ApiClient
import generators

class Helpers:

    @staticmethod
    # Функция регистрации пользователя через API
    def register_user():
        payload = {
                'email': generators.user_email_generator(),
                'password': 'password',
                'name': generators.user_name_generator()
            }
        email = payload['email']
        # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
        response = ApiClient.post_request_create_user(payload)
        if response.status_code != 200:
            allure.attach(
                body=response.text,
                name=f"Не удалось зарегистрировать пользователя: статус {response.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                body=response.text,
                name=f"Пользователь {email} зарегистрирован: статус {response.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )             
        # получаем accessToken пользователя
        access_token = response.json()['accessToken']
        refresh_token = response.json()['refreshToken']
        return access_token, refresh_token, email

    @staticmethod
    # Функция удаления пользователя через API
    def delete_user(access_token, email):
        response = ApiClient.request_delete_user(access_token)
        if response.status_code != 202:
            allure.attach(
                body=response.text,
                name=f"Не удалось удалить пользователя: статус {response.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                body=response.text,
                name=f"Пользователь {email} успешно удалён: статус {response.status_code}",
                attachment_type=allure.attachment_type.TEXT
            )             

    @staticmethod
    # Функция получения хэша двух ингредиентов
    def ingredients_hash():
        response = ApiClient.get_request_get_ingredients()
        ingredients_hash = [(response.json()['data'][0]['_id']), (response.json()['data'][1]['_id'])]
        return ingredients_hash

    # Оформление заказа через API и получение его номера
    @staticmethod
    def create_order_with_authorized_user(access_token):
        ingredients = Helpers.ingredients_hash()
        payload = {
            'ingredients': ingredients
            }
        response = ApiClient.post_request_create_order(payload, access_token)
        if response.status_code != 200:
                    allure.attach(
                        body=response.text,
                        name=f"Не удалось удалить создать заказ: статус {response.status_code}",
                        attachment_type=allure.attachment_type.TEXT
                    )
        order_number = response.json()['order']['number']
        return order_number

    @staticmethod
    # Функция получения наименования ингредиента для тестов
    def get_ingredient_name():
        response = ApiClient.get_request_get_ingredients()
        ingredient_name = response.json()['data'][0]['name']
        return ingredient_name