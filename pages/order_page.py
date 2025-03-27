import allure
from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @allure.step
    def enter_name(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name) # Вводит имя в поле ввода

    @allure.step
    def enter_last_name(self, last_name):
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name) # Вводит фамилию в поле ввода

    @allure.step
    def enter_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address) # Вводит адрес в поле ввода

    @allure.step
    def underground_station(self):
        self.click(OrderPageLocators.UNDERGROUND_BUTTON) # Выбирает станцию метро

    @allure.step
    def select_underground_station(self):
        self.click(OrderPageLocators.UNDERGROUND_SELECT)

    @allure.step
    def date_delivery(self, data):
        self.send_keys(OrderPageLocators.DATE_SELECTION_BUTTON, data)

    @allure.step
    def date_delivery_selection(self):
        self.click(OrderPageLocators.DATE_SELECTION_BUTTON_INPUT)

    @allure.step
    def rental_period_click(self):
        self.click(OrderPageLocators.RENTAL_PERIOD)

    @allure.step
    def select_rental_period(self, period):
        if period == "one_day":
            self.click(OrderPageLocators.RENTAL_PERIOD_ONE_DAY) # Выбирает срок аренды 'сутки'
        elif period == "two_days":
            self.click(OrderPageLocators.RENTAL_PERIOD_TWO_DAY) # Выбирает срок аренды 'двое суток'

    @allure.step
    def select_scooter_color(self, color):
        if color == "black":
            self.click(OrderPageLocators.SCOOTER_COLOR_BLACK) # Выбирает цвет самоката 'черный'
        elif color == "grey":
            self.click(OrderPageLocators.SCOOTER_COLOR_GREY) # Выбирает цвет самоката 'серый'
        else:
            raise ValueError(f"Invalid rental period: {color}")

    @allure.step
    def enter_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone) # Вводит телефон в поле ввода

    @allure.step
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON) # Нажимает на кнопку 'Далее'

    @allure.step
    def click_order_button_center(self):
        self.click(OrderPageLocators.ORDER_BUTTON_MIDDLE) # Нажимает на кнопку 'Заказать' после заполнения формы

    @allure.step
    def wait_for_modal_to_appear(self):
        self.wait_for_element(self.locators.CONFIRM_ORDER_MODAL)

    @allure.step
    def click_confirm_order_button(self):
        self.wait_for_modal_to_appear()  # Ожидаем появления модального окна
        self.click(self.locators.CONFIRM_ORDER_BUTTON)

    @allure.step
    def get_success_message(self):
        return self.find_element(OrderPageLocators.SUCCESS_MESSAGE).text # Получает сообщение об успешном заказе


