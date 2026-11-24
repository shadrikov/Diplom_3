from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
import allure

class HeaderPage(BasePage):

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        return self.js_click_element(HeaderPageLocators.LOCATOR_CONSTRUCTOR_BTN) # Выбран js-скрипт для клика, т.к. в Firefox падают тесты с обычным кликом

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_feed_btn(self):
        return self.js_click_element(HeaderPageLocators.LOCATOR_FEED_BTN) # Выбран js-скрипт для клика, т.к. в Firefox падают тесты с обычным кликом