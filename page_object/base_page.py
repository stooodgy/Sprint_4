import allure
from page_object.locators import BasePagelocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать на логотип самоката")
    def click_on_samkat_logo(self):
        return self.driver.find_element(*BasePagelocators.SAMOKAT_LOGO).click()

    @allure.step("Нажать на логотип Яндекса")
    def click_on_yandex_logo(self):
        return self.driver.find_element(*BasePagelocators.YANDEX_LOGO).click()

    def wait_for_load_page(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Переключение на открывшуюся вкладку")
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
