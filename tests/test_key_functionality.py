import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Ключевая функциональность")
class TestKeyFunctionality:
    
    @allure.title("Тест: Переход по клику на 'Конструктор'")
    def test_click_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Перейти в ленту заказов"):
            main_page.click_order_feed()
            order_page.wait_for_visible(OrderPage.ORDER_FEED_TITLE)
        
        with allure.step("3. Вернуться в конструктор"):
            main_page.click_constructor()
            assert main_page.is_element_present(MainPage.CONSTRUCTOR_AREA)
    
    @allure.title("Тест: Переход по клику на 'Лента заказов'")
    def test_click_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Перейти в ленту заказов"):
            main_page.click_order_feed()
        
        with allure.step("3. Проверить переход"):
            order_page.wait_for_visible(OrderPage.ORDER_FEED_TITLE)
            assert "feed" in order_page.get_current_url()
    
    @allure.title("Тест: Клик на ингредиент открывает детали")
    def test_ingredient_click_opens_details(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Кликнуть на ингредиент"):
            main_page.click_ingredient()
        
        with allure.step("3. Проверить открытие модального окна"):
            assert main_page.is_modal_open()
    
    @allure.title("Тест: Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        
        with allure.step("1. Открыть главную страницу"):
            main_page.open()
        
        with allure.step("2. Открыть модальное окно ингредиента"):
            main_page.click_ingredient()
            assert main_page.is_modal_open()
        
        with allure.step("3. Закрыть модальное окно"):
            main_page.close_modal()
        
        with allure.step("4. Проверить закрытие окна"):
            assert not main_page.is_modal_open()
