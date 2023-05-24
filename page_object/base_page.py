import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Кликнуть на элемент")
    def click_on(self, locator):
        return self.driver.find_element(*locator).click()

    @allure.step("Вставить данные в поле")
    def send_key(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    def wait_presence_of_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step("Переключение на открывшуюся вкладку")
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
