from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::div")
    
    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button")
    
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__')]")
