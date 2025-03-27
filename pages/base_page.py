
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def click_element_when_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_element_text_when_visible(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text

    # def execute_script(self, script, *args):
    #     return self.driver.execute_script(script, *args)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        new_window = self.driver.window_handles[-1] # Переключиться на новую вкладку
        self.driver.switch_to.window(new_window)
        return self.driver.current_url

    def close_current_tab(self):
        self.driver.close() # Закрыть текущую вкладку

    def get_url_after_redirect(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(  # Получить URL
            lambda d: d.current_url != 'about:blank'
        )
        return self.driver.current_url