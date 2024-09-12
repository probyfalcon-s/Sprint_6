import allure
from selenium import webdriver
from pages.important_questions import SectionImportantQuestions
from src.config import BASE_URL
from locators.questions_locators import Locators


class TestButtonsQuestions:

    driver = None

    @classmethod
    def setup_class(cls):
        with allure.step(f"Открываем браузер Firefox"):
            with allure.step(f"Открываем страницу"):
                cls.driver = webdriver.Firefox()
                cls.driver.get(BASE_URL)

    @classmethod
    def teardown_class(cls):
        with allure.step(f"Закрываем браузер"):
            cls.driver.quit()

    @allure.title(f"Проверка ответа у первого вопроса")
    @allure.description(
        f'На странице ищем текст "Сутки — 400 рублей" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_first(self):
        question_locator = Locators.BUTTON_QUESTION_FIRST
        answer_locator = Locators.P_ANSWER_FIRST
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert text_answer == expected_text

    @allure.title(f"Проверка ответа у второго вопроса")
    @allure.description(
        f'На странице ищем текст "Пока что у нас так: один заказ — один самокат" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_second(self):
        question_locator = Locators.BUTTON_QUESTION_SECOND
        answer_locator = Locators.P_ANSWER_SECOND
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert text_answer == expected_text

    @allure.title(f"Проверка ответа у третьего вопроса")
    @allure.description(
        f'На странице ищем текст "Допустим, вы оформляете заказ на 8 мая" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_third(self):
        question_locator = Locators.BUTTON_QUESTION_THIRD
        answer_locator = Locators.P_ANSWER_THIRD
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert text_answer == expected_text

    @allure.title(f"Проверка ответа у четвертого вопроса")
    @allure.description(
        f'На странице ищем текст "Только начиная с завтрашнего дня" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_fourth(self):
        question_locator = Locators.BUTTON_QUESTION_FOURTH
        answer_locator = Locators.P_ANSWER_FOURTH
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert text_answer == expected_text

    @allure.title(f"Проверка ответа у пятого вопроса")
    @allure.description(
        f'На странице ищем текст "Пока что нет" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_fifth(self):
        question_locator = Locators.BUTTON_QUESTION_FIFTH
        answer_locator = Locators.P_ANSWER_FIFTH
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert text_answer == expected_text

    @allure.title("Проверка ответа у шестого вопроса")
    @allure.description(
        f'На странице ищем текст "Самокат приезжает к вам с полной зарядкой" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_sixth(self):
        question_locator = Locators.BUTTON_QUESTION_SIXTH
        answer_locator = Locators.P_ANSWER_SIXTH
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert text_answer == expected_text

    @allure.title("Проверка ответа у седьмого вопроса")
    @allure.description(
        f'На странице ищем текст "Да, пока самокат не привезли." и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_seventh(self):
        question_locator = Locators.BUTTON_QUESTION_SEVENTH
        answer_locator = Locators.P_ANSWER_SEVENTH
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert text_answer == expected_text

    @allure.title("Проверка ответа у восьмого вопроса")
    @allure.description(
        f'На странице ищем текст" Да, обязательно. Всем самокатов" и проверяем, что его text_answer == expected_text'
    )
    def test_list_questions_eighth(self):
        question_locator = Locators.BUTTON_QUESTION_EIGHTH
        answer_locator = Locators.P_ANSWER_EIGHTH
        section_question = SectionImportantQuestions(
            self.driver, question_locator, answer_locator
        )
        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        expected_text = (
            "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )
        assert text_answer == expected_text
