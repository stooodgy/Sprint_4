import allure
from page_object.locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Keys


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнить текстовые поля с данными заказчика")
    def fill_in_order_data(self, order):
        self.driver.find_element(*OrderPageLocators.FIELD_NAME).send_keys(order.name)
        self.driver.find_element(*OrderPageLocators.FIELD_SURNAME).send_keys(order.surname)
        self.driver.find_element(*OrderPageLocators.FIELD_ADDRESS).send_keys(order.address_to_take)
        self.driver.find_element(*OrderPageLocators.FIELD_METRO).send_keys(order.station + Keys.ARROW_DOWN + Keys.ENTER)
        self.driver.find_element(*OrderPageLocators.FIELD_PHONE_NUMBER).send_keys(order.phone_number)
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    @allure.step("Заполнить текстовые поля с данными заказа")
    def fill_in_rent_data(self, order):
        self.driver.find_element(*OrderPageLocators.FIELD_WHEN_TO_BRING_SCOOTER).send_keys(order.date + Keys.ENTER)
        self.driver.find_element(*OrderPageLocators.FIELD_RENTAL_PERIOD).click()
        self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_MENU)[order.period_index].click()
        self.driver.find_elements(*OrderPageLocators.FIELD_SCOOTER_COLOR)[order.color_index].click()
        self.driver.find_element(*OrderPageLocators.FIELD_COMMENT_FOR_COURIER).send_keys(order.comment)
        self.driver.find_element(*OrderPageLocators.BUTTON_TO_ORDER).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((OrderPageLocators.TEXT_ABOUT_ORDER)))
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        return self.driver.find_element(*OrderPageLocators.TEXT_ABOUT_ORDER).text

