import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="screenshot_error",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент {locator} не найден")

    @allure.step("Ввести текст в элемент {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except Exception:
            element = self.find_element(locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text.strip()

    @allure.step("Проверить наличие элемента {locator}")
    def is_element_present(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидать видимости {locator}")
    def wait_for_visible(self, locator, timeout=10):
        return self.find_element(locator, timeout)

    @allure.step("Ожидать исчезновения {locator}")
    def wait_for_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator, timeout=10):
        self.is_element_present(locator, timeout)
        return self.driver.find_elements(*locator)

