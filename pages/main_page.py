import allure
from selenium.common import TimeoutException
from locators.main_page_locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    @allure.step
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        self.locators = MainPageLocators()

    @allure.step
    def click_order_button_above(self):
        self.click(MainPageLocators.ORDER_BUTTON_ABOVE) # Нажимает на кнопку 'Заказать' вверху страницы

    @allure.step
    def click_order_button_down(self):
        # Прокручиваем страницу до кнопки
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)  # Нажимает на кнопку 'Заказать' внизу страницы

        # Теперь кликаем по кнопке
        self.click(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step
    def click_yandex_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.locators.YANDEX_BUTTON)
        )
        button.click()

    @allure.step
    def click_scooter_button(self):
        self.click(self.locators.SCOOTER_BUTTON)

    @allure.step
    def scroll_to_faq_text(self):
        self.scroll_to_element(self.locators.FAQ_TEXT) # Прокручивает до секции FAQ

    @allure.step
    def expand_question(self, question_text):
        try:
            # Получаем локатор вопроса с подставленным текстом
            question_locator = (self.locators.FAQ_QUESTIONS[0],
                                self.locators.FAQ_QUESTIONS[1].format(question_text))  # Раскрывает вопрос FAQ по тексту

            # Ожидаем и кликаем по вопросу
            question = self.wait.until(EC.element_to_be_clickable(question_locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
            question.click()
            return True
        except TimeoutException:
            available_questions = [q.text for q in self.driver.find_elements(*self.locators.FAQ_QUESTIONS)]
            raise ValueError(f"Вопрос '{question_text}' не найден. Доступные вопросы: {available_questions}")

    @allure.step
    def get_answer_text(self, question_text):
        try:
            # Формируем локатор ответа для конкретного вопроса
            answer_locator = (self.locators.FAQ_ANSWER[0],
                              self.locators.FAQ_ANSWER[1].format(question_text))    # Получает текст ответа для указанного вопроса

            # Ожидаем и возвращаем текст ответа
            answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
            return answer.text
        except TimeoutException:
            raise ValueError(f"Ответ на вопрос '{question_text}' не найден или не отображается")