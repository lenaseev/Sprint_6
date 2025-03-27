
import allure
from selenium.common import TimeoutException
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage

class MainPage(BasePage):
    @allure.step("Инициализация главной страницы")
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_button_above(self):
        self.click(self.locators.ORDER_BUTTON_ABOVE)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_down(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_DOWN)
        self.click(self.locators.ORDER_BUTTON_DOWN)

    @allure.step("Нажать кнопку 'Яндекс'")
    def click_yandex_button(self):
        self.click_element_when_clickable(self.locators.YANDEX_BUTTON)

    @allure.step("Нажать кнопку 'Самокат'")
    def click_scooter_button(self):
        self.click(self.locators.SCOOTER_BUTTON)

    @allure.step("Прокрутить к разделу FAQ")
    def scroll_to_faq_text(self):
        self.scroll_to_element(self.locators.FAQ_TEXT)

    @allure.step("Раскрыть вопрос FAQ")
    def expand_question(self, question_text):
        try:
            question_locator = (self.locators.FAQ_QUESTIONS[0],
                               self.locators.FAQ_QUESTIONS[1].format(question_text))
            self.scroll_to_element(question_locator)
            self.click_element_when_clickable(question_locator)
            return True
        except TimeoutException:
            available_questions = [q.text for q in self.find_elements(self.locators.FAQ_QUESTIONS)]
            raise ValueError(f"Вопрос '{question_text}' не найден. Доступные вопросы: {available_questions}")

    @allure.step("Получить текст ответа на вопрос")
    def get_answer_text(self, question_text):
        try:
            answer_locator = (self.locators.FAQ_ANSWER[0],
                            self.locators.FAQ_ANSWER[1].format(question_text))
            return self.get_element_text_when_visible(answer_locator)
        except TimeoutException:
            raise ValueError(f"Ответ на вопрос '{question_text}' не найден или не отображается")

    @allure.step("Нажать кнопку Яндекса и получить итоговый URL")
    def click_yandex_and_get_final_url(self):
        self.click(self.locators.YANDEX_BUTTON)
        self.switch_to_new_tab()
        return self.get_url_after_redirect()

