from selenium.webdriver.common.by import By

class HeaderPageLocators:

    LOCATOR_CONSTRUCTOR_BTN = (By.XPATH, "//ul/li/a[@href='/']") # Кнопка «Конструктор»

    LOCATOR_FEED_BTN = (By.XPATH, "//ul/li/a[@href='/feed']") # Кнопка «Лента заказов»