import allure
from page_object.base_page import BasePage
from page_object.locators import OrderPageLocators
from selenium.webdriver import Keys


class OrderPage(BasePage):

    @allure.step("Заполнить текстовые поля с данными заказчика")
    def fill_in_order_data(self, order):
        self.send_key(OrderPageLocators.FIELD_NAME, order.name)
        self.send_key(OrderPageLocators.FIELD_SURNAME, order.surname)
        self.send_key(OrderPageLocators.FIELD_ADDRESS, order.address_to_take)
        self.send_key(OrderPageLocators.FIELD_METRO, order.station + Keys.ARROW_DOWN + Keys.ENTER)
        self.send_key(OrderPageLocators.FIELD_PHONE_NUMBER, order.phone_number)
        self.click_on(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить текстовые поля с данными заказа")
    def fill_in_rent_data(self, order):
        self.send_key(OrderPageLocators.FIELD_WHEN_TO_BRING_SCOOTER, order.date + Keys.ENTER)
        self.click_on(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.find_elements(OrderPageLocators.RENTAL_PERIOD_MENU)[order.period_index].click()
        self.find_elements(OrderPageLocators.FIELD_SCOOTER_COLOR)[order.color_index].click()
        self.send_key(OrderPageLocators.FIELD_COMMENT_FOR_COURIER, order.comment)
        self.click_on(OrderPageLocators.BUTTON_TO_ORDER)
        self.wait(OrderPageLocators.TEXT_ABOUT_ORDER)
        self.click_on(OrderPageLocators.BUTTON_YES)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        return self.find_element(OrderPageLocators.TEXT_ABOUT_ORDER).text

