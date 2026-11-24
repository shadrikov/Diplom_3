from selenium.webdriver.common.by import By

class FeedPageLocators:

    LOCATOR_ORDER_FEED_TEXT = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]") # Текст "Лента заказов" на странице ленты заказов

    LOCATOR_COMPLETED_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]") # Количество выполненных заказов за всё время

    LOCATOR_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]") # Количество выполненных заказов за сегодня

    LOCATOR_LIST_ORDERS_DONE = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList_') and not(contains(@class,'OrderFeed_orderListReady'))]/li") # Номера заказов в секции "Готовы" 

    LOCATOR_LIST_ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li") # Номера заказов в секции "В работе"