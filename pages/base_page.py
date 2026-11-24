from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Получение элемента с ожиданием его видимости')
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Получение существующего в DOM элемента')
    def find_element_in_dom_with_wait(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))    

    @allure.step('Клик по элементу, когда он становится кликабельным')
    def click_element_with_wait(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Проверка, что открыт нужный URL')
    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False 

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Получение набора элементов с ожиданием их видимости')
    def find_elements_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Клик по элементу, если он перекрыт другим элементом')
    def js_click_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Сработал только такой способ с js-скриптом, найденный в интернете, Firefox не хочет перетаскивать другими способами
    @allure.step('Перетаскивание элемента из одного места в другое')
    def js_drag_and_drop_element(self, source_element_locator, target_element_locator):
        source = self.find_element_with_wait(source_element_locator)
        target = self.find_element_with_wait(target_element_locator)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var rect = target.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true, cancelable: true,
                clientX: rect.left + rect.width / 2,
                clientY: rect.top + rect.height / 2,
                dataTransfer: dataTransfer}));
            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true, cancelable: true,
                clientX: rect.left + rect.width / 2,
                clientY: rect.top + rect.height / 2,
                dataTransfer: dataTransfer}));
            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true, dataTransfer: dataTransfer}));
        """, source, target)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)