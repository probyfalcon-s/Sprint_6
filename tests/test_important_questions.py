import allure
from pages.important_questions import SectionImportantQuestions
from locators.questions_locators import Locators
import pytest


questions_and_answers = {
    "first": (
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        Locators.BUTTON_QUESTION_FIRST,
        Locators.P_ANSWER_FIRST,
    ),
    "second": (
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        Locators.BUTTON_QUESTION_SECOND,
        Locators.P_ANSWER_SECOND,
    ),
    "third": (
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        Locators.BUTTON_QUESTION_THIRD,
        Locators.P_ANSWER_THIRD,
    ),
    "fourth": (
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        Locators.BUTTON_QUESTION_FOURTH,
        Locators.P_ANSWER_FOURTH,
    ),
    "fifth": (
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        Locators.BUTTON_QUESTION_FIFTH,
        Locators.P_ANSWER_FIFTH,
    ),
    "sixth": (
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        Locators.BUTTON_QUESTION_SIXTH,
        Locators.P_ANSWER_SIXTH,
    ),
    "seventh": (
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        Locators.BUTTON_QUESTION_SEVENTH,
        Locators.P_ANSWER_SEVENTH,
    ),
    "eighth": (
        "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        Locators.BUTTON_QUESTION_EIGHTH,
        Locators.P_ANSWER_EIGHTH,
    ),
}


class TestButtonsQuestions:

    @pytest.mark.parametrize("question_key", questions_and_answers.keys())
    def test_list_questions(self, driver, question_key):
        with allure.step(f"Проверка ответа у вопроса"):
            expected_text, question_locator, answer_locator = questions_and_answers[
                question_key
            ]

        section_question = SectionImportantQuestions(
            driver, question_locator, answer_locator
        )

        section_question.scroll_to_element()
        section_question.click_button()
        section_question.wait_for_load_question()
        text_answer = section_question.get_answer_text()
        with allure.step(
            f"На странице ищем текст и проверяем, что его text_answer == expected_text"
        ):
            assert text_answer == expected_text
