import allure
from pages.home_page import HomePage

class TestIngredients:

    @allure.title('Появление всплывающего окна с деталями при клике по ингредиенту в конструкторе')
    @allure.description('Нажимаем на ингредиент в конструкторе. Проверяем, что появилось всплывающее окно с информацией об ингредиенте.')
    def test_ingredient_details_window_opens_by_click_on_ingredient(self, main_page, ingredient_name):
        driver = main_page
        home_page = HomePage(driver)
        home_page.click_ingredient(ingredient_name)
        window_is_opened = home_page.is_ingredient_details_window_opened()
        assert window_is_opened

    @allure.title('Закрытие всплывающего окна с деталями при клике по крестику')
    @allure.description('Нажимаем на нгредиент в конструкторе. Открывается всплывающее окно с информацией об ингредиенте. Закрываем окно кликом по крестику.')
    def test_ingredient_details_window_closes_by_click_on_cross_icon(self, main_page, ingredient_name):
        driver = main_page
        home_page = HomePage(driver)
        home_page.click_ingredient(ingredient_name)
        home_page.click_ingredient_details_window_close_btn()
        window_is_closed = home_page.is_ingredient_details_window_closed()
        assert window_is_closed

    @allure.title('Счётчик ингредиента увеличивается при добавлении его в заказ')
    @allure.description('Перетаскиваем ингредиент в конструкторе в заказ. Проверяем, что счётчик ингредиента увеличился.')
    def test_ingredient_amount_increases_by_adding_ingredient_to_order(self, main_page, ingredient_name):
        driver = main_page
        home_page = HomePage(driver)
        amount_before = home_page.get_ingredient_amount()
        home_page.add_ingredient_to_order(ingredient_name)
        amount_after = home_page.get_ingredient_amount()
        assert amount_before < amount_after