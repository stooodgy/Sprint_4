import allure
from urls import Urls
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from page_object.locators import OrderPageLocators
from page_object.locators import MainPagelocators
from page_object.locators import YandexMainPageLocators


class TestSiteLogo:

    @allure.title("Тест-кейс: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_click_logo_samokat(self, driver):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.click_order_button(MainPagelocators.BUTTON_ORDER_TOP)
        base_page.wait_for_load_page(OrderPageLocators.ORDER_HEADER_USER)
        base_page.click_on_samkat_logo()

        assert driver.current_url == Urls.MAIN_PAGE_URL, 'Текущая страница не является гланой страницой «Самоката»'

    @allure.title("Тест-кейс: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса")
    def test_click_logo_yandex(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_yandex_logo()
        base_page.switch_to_new_window()
        base_page.wait_for_load_page(YandexMainPageLocators.SEARCH_FRAME)

        assert driver.current_url == Urls.YANDEX_MAIN_PAGE_URL, 'Текущая страница не является гланой страницой Яндекса'