from selenium.webdriver.common.by import By

class HomePageLocators:

    LOCATOR_CREATE_BURGER_TEXT = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]") # Текст "Соберите бургер" на главной странице

    LOCATOR_SECTION_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[contains(text(), 'Булки')]]") # Вкладка «Булки»

    LOCATOR_SECTION_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[contains(text(), 'Соусы')]]") # Вкладка «Соусы»

    LOCATOR_SECTION_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab') and .//span[contains(text(), 'Начинки')]]") # Вкладка «Начинки»

    LOCATOR_CURRENT_SECTION_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab') and contains(@class, 'tab_tab_type_current') and .//span[contains(text(), 'Булки')]]") # Текущая вкладка «Булки»

    LOCATOR_CURRENT_SECTION_SAUCES = (By.XPATH, "//div[contains(@class, 'tab_tab') and contains(@class, 'tab_tab_type_current') and .//span[contains(text(), 'Соусы')]]") # Текущая вкладка «Соусы»

    LOCATOR_CURRENT_SECTION_FILLINGS = (By.XPATH, "//div[contains(@class, 'tab_tab') and contains(@class, 'tab_tab_type_current') and .//span[contains(text(), 'Начинки')]]") # Текущая вкладка «Начинки»

    LOCATOR_INGREDIENT_DETAILS_WINDOW_IS_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened') and .//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали ингредиента')]]") # Открытое окно с деталями ингредиента

    LOCATOR_INGREDIENT_DETAILS_WINDOW_IS_CLOSED = (By.XPATH, "//section[contains(@class, 'Modal_modal') and not(contains(@class, 'opened')) and .//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали ингредиента')]]") # Открытое окно с деталями ингредиента

    LOCATOR_INGREDIENT_DETAILS_WINDOW_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # Кнопка закрытия окна с деталями ингредиента
    
    LOCATOR_INGREDIENT_AMOUNT = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]") # Количество первого ингредиента в счётчике
    
    LOCATOR_ORDER_BASKET = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]") # Корзина конструктора заказа

    LOCATOR_FIRST_INGREDIENT_FROM_LIST = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]") # Первый ингредиент в списке ингредиентов конструктора
    
    # Локатор карточки ингредиента с наименованием ингредиента
    @staticmethod
    def locate_ingredient_card_by_ingredient_name(ingredient_name):
        locator = (By.XPATH, f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[contains(text(), '{ingredient_name}')]]")
        return locator