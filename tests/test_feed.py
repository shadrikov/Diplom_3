import allure
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from helpers import Helpers

class TestFeed:

    @allure.title('Счётчик "Выполнено за всё время" увеличивается при создании нового заказа')
    @allure.description('Регистрируем пользователя, авторизуемся созданным пользователем. ' \
    'Запоминаем значение счётчика "Выполнено за всё время" в Ленте заказов. ' \
    'Создаём новый заказ, запоминаем его номер. ' \
    'Когда в блоке номеров заказов "Готовы" появится номер созданного заказа, проверяем увеличение значения счётчика "Выполнено за всё время".')
    def test_total_completed_amount_increases_by_making_order(self, login_profile):
        driver, access_token = login_profile
        header_page = HeaderPage(driver)
        header_page.click_feed_btn()
        feed_page = FeedPage(driver)
        feed_page.is_feed_page_opened()
        amount_before = feed_page.get_orders_completed_total()
        order_number = Helpers.create_order_with_authorized_user(access_token)
        feed_page.wait_order_number_in_done_list(order_number)
        amount_after = feed_page.get_orders_completed_total()
        assert amount_after > amount_before

    @allure.title('Счётчик "Выполнено за сегодня" увеличивается при создании нового заказа')
    @allure.description('Регистрируем пользователя, авторизуемся созданным пользователем. ' \
    'Запоминаем значение счётчика "Выполнено за сегодня" в Ленте заказов. ' \
    'Создаём новый заказ, запоминаем его номер. ' \
    'Когда в блоке номеров заказов "Готовы" появится номер созданного заказа, проверяем увеличение значения счётчика "Выполнено за сегодня".')
    def test_today_completed_amount_increases_by_making_order(self, login_profile):
        driver, access_token = login_profile
        header_page = HeaderPage(driver)
        header_page.click_feed_btn()
        feed_page = FeedPage(driver)
        feed_page.is_feed_page_opened()
        amount_before = feed_page.get_orders_completed_today()
        order_number = Helpers.create_order_with_authorized_user(access_token)
        feed_page.wait_order_number_in_done_list(order_number)
        amount_after = feed_page.get_orders_completed_today()
        assert amount_after > amount_before

    @allure.title('Номер заказа появляется в разделе "В работе" после оформления')
    @allure.description('Регистрируем пользователя, авторизуемся созданным пользователем. ' \
    'Создаём новый заказ, запоминаем его номер. ' \
    'Проверяем наличие номера созданного заказа в секции "В работе".')
    def test_section_in_progress_contains_order_number_after_making_order(self, login_profile):
        driver, access_token = login_profile
        header_page = HeaderPage(driver)
        header_page.click_feed_btn()
        feed_page = FeedPage(driver)
        feed_page.is_feed_page_opened()
        order_number = Helpers.create_order_with_authorized_user(access_token)
        is_order_in_progress = feed_page.wait_order_number_in_list_in_progress(order_number)
        assert is_order_in_progress