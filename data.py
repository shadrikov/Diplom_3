class URLs:

    HOME_PAGE_URL = 'https://stellarburgers.education-services.ru/' # Главная страница

    FEED_PAGE_URL = f'{HOME_PAGE_URL}feed' # Лента заказов

    CREATE_USER = f'{HOME_PAGE_URL}api/auth/register' # Ручка API создания пользователя
    
    DELETE_USER = f'{HOME_PAGE_URL}api/auth/user' # Ручка API удаления пользователя

    CREATE_ORDER = f'{HOME_PAGE_URL}api/orders' # Ручка API создания заказа

    GET_INGREDIENTS = f'{HOME_PAGE_URL}api/ingredients' # Ручка API получения хэша ингредиентов