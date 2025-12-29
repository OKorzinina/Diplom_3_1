import pytest
import allure
from pages.order_page import OrderPage


@allure.feature("Лента заказов")
class TestOrderFeed:
    
    @allure.title("Тест: Проверка счетчиков в ленте заказов")
    def test_order_counters_display(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть ленту заказов"):
            order_page.open()
        
        with allure.step("2. Проверить отображение счетчика 'Выполнено за всё время'"):
            total_count = order_page.get_total_orders_count()
            assert total_count >= 0
        
        with allure.step("3. Проверить отображение счетчика 'Выполнено за сегодня'"):
            today_count = order_page.get_today_orders_count()
            assert today_count >= 0
    
    @allure.title("Тест: Проверка раздела 'В работе'")
    def test_orders_in_progress_section(self, driver):
        order_page = OrderPage(driver)
        
        with allure.step("1. Открыть ленту заказов"):
            order_page.open()
        
        with allure.step("2. Проверить наличие раздела 'В работе'"):
            assert order_page.is_element_present(OrderPage.IN_PROGRESS_SECTION)
