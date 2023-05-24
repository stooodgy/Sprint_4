from selenium.webdriver.common.by import By

class BasePagelocators:

    SAMOKAT_LOGO = By.XPATH, ".//*[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, ".//*[@alt='Yandex']"

class MainPagelocators:
    #Локаторы элементов главной страницы
    BUTTON_ORDER_TOP = By.CLASS_NAME, "Button_Button__ra12g"
    BUTTON_ORDER_BOTTOM = By.XPATH, ".//button[contains(@class, 'Button_Middle__1CSJM')]"
    BUTTON_ACCEPT_COOKIES = By.XPATH, ".//button[@class='App_CookieButton__3cvqF' and text()='да все привыкли']"
    QUESTION_MENU = By.XPATH, ".//div[contains(@id, 'accordion__heading-')]"
    ANSWER_MENU = By.XPATH, ".//div[contains(@id, 'accordion__panel-')]/p"

class OrderPageLocators:
    #Локаторы формы данных пользователя
    ORDER_HEADER_USER = By.XPATH, ".//div[text()='Для кого самокат']"
    FIELD_NAME = By.XPATH, ".//input[@placeholder='* Имя']"
    FIELD_SURNAME = By.XPATH, ".//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_PHONE_NUMBER = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    FIELD_METRO = By.XPATH, ".//input[@placeholder='* Станция метро']"
    BUTTON_NEXT = By.XPATH, ".//button[text()='Далее']"

    #Локаторы формы данных заказа
    ORDER_HEADER = By.XPATH, ".//div[text()='Про аренду']"
    FIELD_WHEN_TO_BRING_SCOOTER = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    FIELD_RENTAL_PERIOD = By.XPATH, ".//div[@class='Dropdown-control']"
    RENTAL_PERIOD_MENU = By.XPATH, ".//div[@class='Dropdown-menu']/div"
    FIELD_SCOOTER_COLOR = By.XPATH, ".//label[@class='Checkbox_Label__3wxSf']"
    FIELD_COMMENT_FOR_COURIER = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    BUTTON_TO_ORDER = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    BUTTON_YES = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"
    TEXT_ABOUT_ORDER = By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"

class YandexMainPageLocators:
    SEARCH_FRAME = [By.XPATH, ".//iframe[@class='dzen-search-arrow-common__frame' and @aria-label='Поиск Яндекса']"]