from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_locators import OrderLocators
from selenium.webdriver.common.by import By


class SectionOrder:
    def __init__(self, driver):
        self.driver = driver
        self.button_order = OrderLocators.BUTTON_ORDER
        self.input_name = OrderLocators.INPUT_NAME
        self.input_surname = OrderLocators.INPUT_SURNAME
        self.input_address = OrderLocators.INPUT_ADDRESS
        self.input_phone = OrderLocators.INPUT_PHONE
        self.button_next = OrderLocators.BUTTON_NEXT
        self.input_metro = OrderLocators.INPUT_METRO
        self.rental_period = OrderLocators.RENTAL_PERIOD
        self.rental_data = OrderLocators.RENTAL_DATA
        self.color_scooter = OrderLocators.COLOR_SCOOTER
        self.button_order_end = OrderLocators.BUTTON_ORDER_END
        self.button_order_yes = OrderLocators.BUTTON_ORDER_YES
        self.main_logo = OrderLocators.MAIN_LOGO
        self.logo_yandex = OrderLocators.LOGO_YANDEX
        self.button_check_status = OrderLocators.BUTTON_CHECK_STATUS
        self.scooter_done = OrderLocators.SCOOTER_DONE

    def click_order(self):
        self.driver.find_element(*self.button_order).click()

    def set_name(self, name):
        self.driver.find_element(*self.input_name).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.input_surname).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.input_address).send_keys(address)

    def set_phone(self, phone):
        self.driver.find_element(*self.input_phone).send_keys(phone)

    def set_metro(self, metro):
        self.driver.find_element(*self.input_metro).send_keys(metro)
        self.driver.find_element(By.XPATH, "//*[@class='Order_Text__2broi' and (text()='Сокольники')]").click()

    def click_button_next(self):
        self.driver.find_element(*self.button_next).click()

    def set_rental_data(self):
        self.driver.find_element(*self.rental_data).click()
        self.driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--003 react-datepicker__day--outside-month']").click()

    def set_rental_period(self):
        self.driver.find_element(*self.rental_period).click()
        self.driver.find_element(By.XPATH, "//div[text()='сутки']").click()

    def set_color_scooter(self):
        self.driver.find_element(*self.color_scooter).click()

    def click_button_order_end(self):
        self.driver.find_element(*self.button_order_end).click()

    def click_button_order_yes(self):
        self.driver.find_element(*self.button_order_yes).click()
        self.driver.find_element(*self.button_check_status).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.scooter_done))

    def click_main_page(self):
        self.driver.find_element(*self.main_logo).click()

    def click_dzen_page(self, url):
        self.driver.find_element(*self.logo_yandex).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver,10).until(EC.url_to_be(url))

    def order(self, name, surname, address, phone, metro):
        self.click_order()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.click_button_next()
        self.set_rental_data()
        self.set_rental_period()
        self.set_color_scooter()
        self.click_button_order_yes()
        self.click_main_page()
        self.click_dzen_page()

