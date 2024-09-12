from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class SectionImportantQuestions:
    def __init__(self, driver, question_locator, answer_locator):
        self.driver = driver
        self.question_locator = question_locator
        self.answer_locator = answer_locator

    def scroll_to_element(self):
        element = self.driver.find_element(*self.question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    def click_button(self):
        self.driver.find_element(*self.question_locator).click()

    def wait_for_load_question(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.answer_locator))

    def get_answer_text(self):
        return self.driver.find_element(*self.answer_locator).text

