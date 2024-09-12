import allure
import pytest
from locators.order_locators import OrderLocators
from src.data import TEST_DATA
from pages.order import SectionOrder


class TestOrder:

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_positive_order(self, driver, data):
        with allure.step(
            f"На странице ищем текст 'Посмотреть статус' и проверяем, что он отображается"
        ):

            order = SectionOrder(driver)
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

        assert driver.find_element(*OrderLocators.SCOOTER_DONE).is_displayed()

    @allure.title("Проверка перехода на главную")
    @allure.description(
        'На странице ищем лого "Самокат" и проверяем, что он отображается при переходе'
    )
    def test_check_main_page(self, driver):
        order = SectionOrder(driver)
        order.click_main_page()

        assert driver.find_element(*OrderLocators.CHECK_MAIN_PAGE).is_displayed()

    @allure.title("Проверка перехода на главную дзена")
    @allure.description(
        'На странице ищем кнопку "Главная" и проверяем, что она отображается'
    )
    def test_check_page_dzen(self, driver):
        order = SectionOrder(driver)
        url = "https://dzen.ru/?yredirect=true"
        order.click_dzen_page(url)
        current_url = driver.current_url

        assert current_url == url
