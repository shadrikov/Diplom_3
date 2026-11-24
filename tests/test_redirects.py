import allure
from pages.header_page import HeaderPage
from pages.home_page import HomePage
from pages.feed_page import FeedPage
from data import URLs

class TestRedirects:

    @allure.title('Проверка перехода на главную страницу по клику на кнопку "Конструктор" в шапке')
    @allure.description('Открываем страницу с лентой заказа. Кликаем на кнопку "Конструктор" в шапке и проверяем, что произошёл редирект на главную страницу Stellar Burgers и что появился заголовок "Соберите бургер".')
    def test_redirect_to_home_page_by_click_on_constructor_btn(self, driver):
        header_page = HeaderPage(driver)
        header_page.driver.get(URLs.FEED_PAGE_URL)
        header_page.click_constructor_btn()
        home_page = HomePage(driver)
        assert home_page.is_home_page_opened()

    @allure.title('Проверка перехода в раздел "Лента заказов" по клику на кнопку "Лента заказов" в шапке')
    @allure.description('Открываем главную страницу. Кликаем на кнопку "Лента заказов" в шапке и проверяем, что произошёл редирект в раздел "Лента заказов".')
    def test_redirect_to_order_feed_page_by_click_on_feed_btn(self, main_page):
        driver = main_page
        header_page = HeaderPage(driver)
        header_page.click_feed_btn()
        feed_page = FeedPage(driver)
        assert feed_page.is_feed_page_opened()