# Diplom_3 Автотесты для учебного сервиса Stellar Burgers

Проект представляет собой набор автоматизированных тестов для учебного сервиса, реализованных на стеке **Python + Selenium + pytest + Allure + requests + Faker**. Архитектура проекта построена по паттерну **Page Object Model (POM)** с вынесением локаторов в отдельные файлы для удобства поддержки.

## Структура проекта
```text
Diplom_3/
├── allure_results/             # Папка для хранения результатов отчётов Allure
├── locators/                   # Локаторы элементов
│   ├── header_page_locators.py
│   ├── home_page_locators.py
│   └── feed_page_locators.py
├── pages/                      # Page Objects (классы страниц)
│   ├── base_page.py            # Базовый класс со вспомогательными методами
│   ├── header_page.py          # Логика шапки страницы
│   ├── home_page.py            # Логика главной страницы конструктора
│   └── feed_page.py            # Логика страницы "Лента заказов"
├── tests/                      # Тестовые сценарии
│   ├── test_feed.py            # Тесты раздела "Лента заказов"
│   ├── test_ingredients.py     # Тесты ингредиентов в конструкторе заказов
│   └── test_redirects.py       # Тесты редиректов в шапке
├── .gitignore                  # Игнорируемые файлы для git
├── conftest.py                 # Фикстуры
├── data.py                     # Тестовые данные и константы, URL'ы
├── generators.py               # Генераторы данных
├── helpers.py                  # Вспомогательные функции
├── api_client.py               # API клиент
├── requirements.txt            # Зависимости проекта
└── README.md                   # Документация
```
## Требования к окружению

Для запуска проекта требуется:
- Python
- Установленный браузер Google Chrome
- Установленный браузер Mozilla Firefox

## Установка и настройка

Установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

## Запуск тестов с генерацией отчёта Allure

Для получения подробного отчёта необходимо добавить флаг --alluredir:
```bash
pytest --alluredir=allure_results
```

## Просмотр отчёта Allure

После успешного прогона тестов сгенерируйте и откройте отчёт:
```bash
allure serve allure_results
```