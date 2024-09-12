import allure
import pytest
from selenium import webdriver
from src.config import BASE_URL
from locators.order_locators import OrderLocators
from src.data import TEST_DATA
from pages.order import SectionOrder


class TestOrder:

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

    @allure.title("Проверка создания заказа")
    @allure.description(
        'На странице ищем текст "Посмотреть статус" и проверяем, что он отображается'
    )
    @pytest.mark.parametrize("data", TEST_DATA)
    def test_positive_order(self, data):
        order = SectionOrder(self.driver)
        order.click_order()
        name = data["name"]
        surname = data["surname"]
        address = data["address"]
        phone = data["phone"]
        metro = data["metro"]

        order.set_name(name)
        order.set_surname(surname)
        order.set_address(address)
        order.set_phone(phone)
        order.set_metro(metro)
        order.click_button_next()
        order.set_rental_data()
        order.set_rental_period()
        order.set_color_scooter()
        order.click_button_order_end()
        order.click_button_order_yes()

        assert self.driver.find_element(*OrderLocators.SCOOTER_DONE).is_displayed()

    @allure.title("Проверка перехода на главную")
    @allure.description(
        'На странице ищем лого "Самокат" и проверяем, что он отображается при переходе'
    )
    def test_check_main_page(self):
        order = SectionOrder(self.driver)
        order.click_main_page()

        assert self.driver.find_element(*OrderLocators.CHECK_MAIN_PAGE).is_displayed()

    @allure.title("Проверка перехода на главную дзена")
    @allure.description(
        'На странице ищем кнопку "Главная" и проверяем, что она отображается'
    )
    def test_check_page_dzen(self):
        order = SectionOrder(self.driver)
        url = "https://dzen.ru/?yredirect=true"
        order.click_dzen_page(url)
        current_url = self.driver.current_url

        assert current_url == url
