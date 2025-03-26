from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator) # Находит элемент на странице по локатору

    def click(self, locator):
        element = self.find_element(locator) # Кликает по элементу
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator) # Отправляет текст в поле ввода
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator) # Прокручивает страницу до элемента
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element(self, locator, timeout=10):
        # Ожидаем, пока элемент не станет видимым
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
