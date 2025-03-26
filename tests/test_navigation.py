import allure
from data.urls import Urls
from pages.main_page import MainPage
class Test_Navigation:
    @allure.title("Проверка на переход по новой вкладке")
    def test_yandex_button(self, driver):
        # Открытие страницы заказа
        driver.get(Urls.ORDER_PAGE)

        main_page = MainPage(driver)
        main_page.click_yandex_button() # Нажимаем на кнопку "Яндекс"
        current_url = driver.current_url  # Получаем текущий URL после клика

        assert current_url == Urls.ORDER_PAGE, (
            f"Ожидалось остаться на странице заказа ({Urls.ORDER_PAGE}), " # Проверка, что мы на главной странице
            f"но текущий URL: {current_url}"
        )

    @allure.title("Проверка на переход на главную страницу")
    def test_scooter_button(self, driver):
        # Открытие страницы заказа
        driver.get(Urls.ORDER_PAGE)

        main_page = MainPage(driver)
        main_page.click_scooter_button() # Нажимаем на кнопку "Самокат"
        current_url = driver.current_url # Получаем текущий URL после клика

        assert current_url == Urls.MAIN_PAGE, (
            f"Ожидалось, что мы будем на {Urls.MAIN_PAGE}, "  # Проверка, что мы на главной странице
            f"но текущий URL {current_url}"
        )


