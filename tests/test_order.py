import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import Urls

class TestOrder:
    @allure.title
    def test_order_above(self, driver):
        # Открытие главной страницы
        driver.get(Urls.MAIN_PAGE)

        main_page = MainPage(driver)

        # Нажимаем на кнопку "Заказать" вверху страницы
        main_page.click_order_button_above()

        # Переход на страницу оформления заказа
        order_page = OrderPage(driver)

        # Заполнение формы заказа
        order_page.enter_name("Иван")
        order_page.enter_last_name("Иванов")
        order_page.enter_address("Москва, ул. Ленина")
        order_page.underground_station()
        order_page.select_underground_station()
        order_page.enter_phone("+7934567890")
        order_page.click_next_button()
        order_page.date_delivery("23.03.2025")
        order_page.date_delivery_selection()
        order_page.rental_period_click()
        order_page.select_rental_period("one_day")
        order_page.select_scooter_color("black")
        order_page.click_order_button_center()
        order_page.click_confirm_order_button()
        # Проверка успешного заказа
        success_message = order_page.get_success_message()
        assert success_message.startswith("Заказ оформлен")

    @allure.title
    def test_order_down(self, driver):
        # Открытие главной страницы
        driver.get(Urls.MAIN_PAGE)

        main_page = MainPage(driver)

        # Нажимаем на кнопку "Заказать" внизу страницы
        main_page.click_order_button_above()

        # Переход на страницу оформления заказа
        order_page = OrderPage(driver)

        # Заполнение формы заказа
        order_page.enter_name("Иванна")
        order_page.enter_last_name("Иванова")
        order_page.enter_address("Москва, ул. Пушкина")
        order_page.underground_station()
        order_page.select_underground_station()
        order_page.enter_phone("+7944567890")
        order_page.click_next_button()
        order_page.date_delivery("25.03.2025")
        order_page.date_delivery_selection()
        order_page.rental_period_click()
        order_page.select_rental_period("two_days")
        order_page.select_scooter_color("grey")
        order_page.click_order_button_center()
        order_page.click_confirm_order_button()
        # Проверка успешного заказа
        success_message = order_page.get_success_message()
        assert success_message.startswith("Заказ оформлен")


