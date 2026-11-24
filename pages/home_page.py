from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure

class HomePage(BasePage):

    @allure.step('Проверка загрузки страницы с конструктором по наличию заголовка "Соберите бургер')
    def is_home_page_opened(self):
        try:
            return self.find_element_with_wait(HomePageLocators.LOCATOR_CREATE_BURGER_TEXT)
        except Exception:
            return False
    
    @allure.step('Клик по ингредиенту в конструкторе при известном наименовании ингредиента')
    def click_ingredient(self, ingredient_name):
        locator = HomePageLocators.locate_ingredient_card_by_ingredient_name(ingredient_name)
        self.scroll_to_element(locator)
        self.js_click_element(locator)

    @allure.step('Проверка открытия окна с деталями')
    def is_ingredient_details_window_opened(self):
        try:
            return self.find_element_with_wait(HomePageLocators.LOCATOR_INGREDIENT_DETAILS_WINDOW_IS_OPENED)
        except Exception:
            return False

    @allure.step('Клик по кнопке закрытия окна с деталями')
    def click_ingredient_details_window_close_btn(self):
        self.js_click_element(HomePageLocators.LOCATOR_INGREDIENT_DETAILS_WINDOW_CLOSE_BTN) 

    @allure.step('Проверка закрытия окна с деталями')
    def is_ingredient_details_window_closed(self):
        try:
            return self.find_element_in_dom_with_wait(HomePageLocators.LOCATOR_INGREDIENT_DETAILS_WINDOW_IS_CLOSED)
        except Exception:
            return False

    @allure.step('Получение значения в счётчике ингредиента')
    def get_ingredient_amount(self):
        return int(self.get_element_text(HomePageLocators.LOCATOR_INGREDIENT_AMOUNT))

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self, ingredient_name):
        self.js_drag_and_drop_element(HomePageLocators.locate_ingredient_card_by_ingredient_name(ingredient_name), HomePageLocators.LOCATOR_ORDER_BASKET)
