import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from urls import Urls


class OrderPage(BasePage):
    
    @allure.step("Открыть ленту заказов")
    def open(self):
        self.driver.get(Urls.ORDER_FEED_URL)
        self.wait_for_visible(OrderPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Получить количество 'Выполнено за всё время'")
    def get_total_orders_count(self):
        count_text = self.get_text(OrderPageLocators.TOTAL_ORDERS)
        return int(count_text.replace(',', ''))
    
    @allure.step("Получить количество 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        count_text = self.get_text(OrderPageLocators.TODAY_ORDERS)
        return int(count_text.replace(',', ''))
