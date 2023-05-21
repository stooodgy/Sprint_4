import allure
from page_object.locators import MainPagelocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from data_test import QuestionsAnswersDictionary


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принять куки")
    def accept_cookie(self):
        self.driver.find_element(*MainPagelocators.BUTTON_ACCEPT_COOKIES).click()

    @allure.step("Нажать на кнопку заказа")
    def click_order_button(self, button):
        self.driver.find_element(*button).click()

    @allure.step("Переход к вопросу из раздела 'Вопросы о важном'")
    def click_on_questions_about_important(self, question_index):
        button = self.driver.find_elements(*MainPagelocators.QUESTION_MENU)
        button[question_index].click()
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, MainPagelocators.QUESTION_MENU[1])))

    def get_element(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step("Сравнение вопроса и полученного ответа раздела 'Вопросы о важном'")
    def comparison_questions_and_answers(self, question_index):
        actual_result = self.get_element(MainPagelocators.ANSWER_MENU)[question_index].text
        expected_result = QuestionsAnswersDictionary.dictionary_question_and_answers[self.get_element(MainPagelocators.QUESTION_MENU)[question_index].text]
        return actual_result == expected_result


