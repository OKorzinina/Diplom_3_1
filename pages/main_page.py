import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):
    
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(Urls.BASE_URL)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Нажать 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_AREA)
    
    @allure.step("Нажать 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
    
    @allure.step("Нажать 'Личный кабинет'")
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.click(MainPageLocators.FLUORESCENT_BUN)
        self.wait_for_visible(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Проверить открытие модального окна")
    def is_modal_open(self):
        return self.is_element_present(MainPageLocators.INGREDIENT_MODAL)
