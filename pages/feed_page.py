from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure
from selenium.common.exceptions import TimeoutException

class FeedPage(BasePage):

    @allure.step('Проверка загрузки страницы с лентой заказов по наличию заголовка "Лента заказов')
    def is_feed_page_opened(self):
        try:
            return self.find_element_with_wait(FeedPageLocators.LOCATOR_ORDER_FEED_TEXT)
        except Exception:
            return False    

    @allure.step('Получение значения счётчика заказов "Выполнено за всё время"')
    def get_orders_completed_total(self):
        return int(self.get_element_text(FeedPageLocators.LOCATOR_COMPLETED_TOTAL))

    @allure.step('Получение значения счётчика заказов "Выполнено за сегодня"')
    def get_orders_completed_today(self):
        return int(self.get_element_text(FeedPageLocators.LOCATOR_COMPLETED_TODAY))

    @allure.step('Получение списка из номеров заказов секции "Готовы" с удалением нулей перед номерами заказов')
    def get_order_numbers_from_done_list(self):
        # Получаем список элементов - номера заказов в секции "Готовы"
        elements = self.find_elements_with_wait(FeedPageLocators.LOCATOR_LIST_ORDERS_DONE) 
        # Создаем пустой список для добавления в него номеров заказов, приведенных к целочисленным значениям
        order_numbers = []
        # Достаём из каждого элемента списка текст - номер заказа с нулями спереди - и приводим к целочисленному виду, убрав нули
        for element in elements:
            order_numbers.append(int(element.text))
        return order_numbers

    @allure.step('Ожидание номера созданного заказа в списке из номеров заказов секции "Готовы"')
    def wait_order_number_in_done_list(self, order_number, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda d: order_number in self.get_order_numbers_from_done_list())

    @allure.step('Получение списка из номеров заказов секции "В работе" с удалением нулей перед номерами заказов')
    def get_order_numbers_from_list_in_progress(self):
        # Получаем список элементов - номера заказов в секции "В работе"
        elements = self.find_elements_with_wait(FeedPageLocators.LOCATOR_LIST_ORDERS_IN_PROGRESS) 
        # Создаем пустой список для добавления в него номеров заказов, приведенных к целочисленным значениям
        order_numbers = []
        # Достаём из каждого элемента списка текст - номер заказа с нулями спереди - и приводим к целочисленному виду, убрав нули
        for element in elements:
            order_numbers.append(int(element.text))
        return order_numbers

    @allure.step('Появление номера созданного заказа в списке из номеров заказов секции "В работе"')
    def wait_order_number_in_list_in_progress(self, order_number, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(lambda d: order_number in self.get_order_numbers_from_list_in_progress())
            return True
        except TimeoutException:
            return False
