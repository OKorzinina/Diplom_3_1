from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_inProgress__')]")
