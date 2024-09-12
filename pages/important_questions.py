from pages.base_page import BasePage

class SectionImportantQuestions(BasePage):
    def __init__(self, driver, question_locator, answer_locator):
        super().__init__(driver)
        self.question_locator = question_locator
        self.answer_locator = answer_locator

    def find_question_element(self):
        return self.driver.find_element(*self.question_locator)

    def scroll_to_element(self):
        super().scroll_to_element(*self.question_locator)
    def click_button(self):
        self.find_element(*self.question_locator).click()

    def wait_for_load_question(self):
        super().click_element(*self.answer_locator)

    def get_answer_text(self):
        return self.get_element_text(*self.answer_locator)

