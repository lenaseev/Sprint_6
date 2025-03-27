import allure
from data.urls import Urls
from pages.main_page import MainPage

class Test_Navigation:
    @allure.title("Проверка на переход по новой вкладке")
    def test_yandex_button(self, driver):
        driver.get(Urls.ORDER_PAGE)

        main_page = MainPage(driver)

        try:
            final_url = main_page.click_yandex_and_get_final_url()
            assert "dzen.ru" in final_url, f"Финальный URL: {final_url}"
        finally:
            main_page.close_current_tab()
    @allure.title("Проверка на переход на главную страницу")
    def test_scooter_button(self, driver):
        # Открытие страницы заказа
        driver.get(Urls.ORDER_PAGE)

        main_page = MainPage(driver)
        main_page.click_scooter_button() # Нажимаем на кнопку "Самокат"

        current_url = main_page.get_current_url() # Получаем текущий URL после клика

        assert current_url == Urls.MAIN_PAGE, (
            f"Ожидалось, что мы будем на {Urls.MAIN_PAGE}, "  # Проверка, что мы на главной странице
            f"но текущий URL {current_url}"
        )


