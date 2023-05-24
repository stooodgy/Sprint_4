import pytest
import allure
from page_object.base_page import BasePage
from page_object.main_page import MainPage


class TestQestionsAboutImportant:

    @pytest.mark.parametrize('question_index', [0, 1, 2, 3, 4, 5, 6, 7])
    @allure.title("Тест-кейс: 'Проверка списка в разделе 'Вопросы о важном'")
    def test_questions_answers(self, driver, question_index):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookie()
        base_page.scroll_down()
        main_page.click_on_questions_about_important(question_index)

        assert main_page.comparison_questions_and_answers(question_index), 'Значение ответа не сопадает со значением в словаре dictionary_question_and_answers'