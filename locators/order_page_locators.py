from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    UNDERGROUND_BUTTON = (By.XPATH, "//input[@placeholder='* Станция метро']")
    UNDERGROUND_SELECT = (By.XPATH, "//div[text()='Красносельская']")
    FURTHER_BUTTON = (By.CSS_SELECTOR, ".Button_Middle__1CSJM")
    DATE_SELECTION_BUTTON = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_SELECTION_BUTTON_INPUT = (By.XPATH, "//div[@aria-label='Choose воскресенье, 23-е марта 2025 г.']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_TWO_DAY = (By.XPATH, "//div[text()='двое суток']")
    SCOOTER_COLOR_BLACK = [By.ID, "black"]
    SCOOTER_COLOR_GREY = [By.ID, "grey"]

    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    CONFIRM_ORDER_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")