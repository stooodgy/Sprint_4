import allure
from urls import Urls
from page_object.main_page import MainPage


class TestSiteLogo:

    @allure.title("Тест-кейс: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_click_logo_samokat(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        main_page.click_samokat_logo()

        assert driver.current_url == Urls.MAIN_PAGE_URL, 'Текущая страница не является гланой страницой «Самоката»'

    @allure.title("Тест-кейс: если нажать на логотип Яндекса, в новом окне откроется главная страница Яндекса")
    def test_click_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()

        assert driver.current_url == Urls.YANDEX_MAIN_PAGE_URL, 'Текущая страница не является гланой страницой Яндекса'