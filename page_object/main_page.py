import allure
from page_object.base_page import BasePage
from page_object.locators import BasePagelocators
from page_object.locators import OrderPageLocators
from page_object.locators import YandexMainPageLocators
from page_object.locators import MainPagelocators
from selenium.webdriver.common.by import By
from data_test import QuestionsAnswersDictionary


class MainPage(BasePage):

    @allure.step("Принять куки")
    def accept_cookie(self):
        self.click_on(MainPagelocators.BUTTON_ACCEPT_COOKIES)

    @allure.step("Нажать на кнопку заказа")
    def click_order_button(self, button = MainPagelocators.BUTTON_ORDER_TOP):
        self.click_on(button)
        self.wait(OrderPageLocators.ORDER_HEADER_USER)

    @allure.step("Нажать на логотип Самоката")
    def click_samokat_logo(self):
        self.click_on(BasePagelocators.SAMOKAT_LOGO)
        self.wait(MainPagelocators.BUTTON_ORDER_TOP)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on(BasePagelocators.YANDEX_LOGO)
        self.switch_to_new_window()
        self.wait(YandexMainPageLocators.SEARCH_FRAME)

    @allure.step("Переход к вопросу из раздела 'Вопросы о важном'")
    def click_on_questions_about_important(self, question_index):
        self.find_elements(MainPagelocators.QUESTION_MENU)[question_index].click()
        self.wait((By.XPATH, MainPagelocators.QUESTION_MENU[1]))

    @allure.step("Сравнение вопроса и полученного ответа раздела 'Вопросы о важном'")
    def comparison_questions_and_answers(self, question_index):
        actual_result = self.wait_presence_of_all_elements_located(MainPagelocators.ANSWER_MENU)[question_index].text
        expected_result = QuestionsAnswersDictionary.dictionary_question_and_answers[self.wait_presence_of_all_elements_located(MainPagelocators.QUESTION_MENU)[question_index].text]
        return actual_result == expected_result