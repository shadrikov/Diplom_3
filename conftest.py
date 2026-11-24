import pytest
from selenium import webdriver
from data import URLs
from helpers import Helpers

# Фикстура создания объекта драйвера
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

# Фикстура загрузки главной страницы
@pytest.fixture()
def main_page(driver):
    driver.get(URLs.HOME_PAGE_URL)
    return driver

# Фикстура cоздания нового пользователя на всю сессию и удаления его после тестов
@pytest.fixture(scope="session")
def create_user():
    # создаём пользователя
    access_token, refresh_token, email = Helpers.register_user()
    yield access_token, refresh_token
    # удаляем пользователя после теста
    Helpers.delete_user(access_token, email)

# Фикстура входа в аккаунт уже зарегистрированным пользователем путём добавления токенов в localStorage и перезагрузки страницы
@pytest.fixture(scope="function")
def login_profile(driver, create_user):
    access_token, refresh_token = create_user
    driver.get(URLs.HOME_PAGE_URL)
    driver.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);"
        "window.localStorage.setItem('refreshToken', arguments[1]);", 
        access_token, refresh_token)
    driver.refresh()
    yield driver, access_token

# Фикстура получения наименования существующего ингредиента
@pytest.fixture(scope="function")
def ingredient_name():
    return Helpers.get_ingredient_name()
