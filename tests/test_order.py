import pytest
import allure
from page_object.base_page import BasePage
from page_object.main_page import MainPage
from page_object.order_page import OrderPage
from data_test import order_1
from data_test import order_2
from page_object.locators import OrderPageLocators


class TestOrder:

    @pytest.mark.parametrize('order', [order_1, order_2])
    @allure.title("Тест-кейс: Заказ самоката. Весь флоу позитивного сценария")
    def test_order_success(self, driver, order):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.click_order_button(order.button_locator)
        base_page.wait_for_load_page(OrderPageLocators.ORDER_HEADER_USER)
        order_page.fill_in_order_data(order)
        order_page.fill_in_rent_data(order)

        assert "Номер заказа" in order_page.get_order_number(), 'В процеесе совершения заказа произошла ошибка'