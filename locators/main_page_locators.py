from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_ABOVE = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_DOWN = (By.XPATH, "//button[contains(text(), 'Заказать') and contains(@class, 'Button_UltraBig__UU3Lp')]")
    SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    FAQ_TEXT = (By.XPATH, "//div[text()='Вопросы о важном']")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']")
    FAQ_ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='{}']/parent::div/following-sibling::div/p")
