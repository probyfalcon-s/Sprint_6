from selenium.webdriver.common.by import By

class OrderLocators:
    #page_order_1
    BUTTON_ORDER = By.XPATH, "//button[text()='Заказать']"
    INPUT_NAME = By.XPATH, "//input[@type='text' and @placeholder='* Имя']"
    INPUT_SURNAME = By.XPATH, "//input[@type='text' and @placeholder='* Фамилия']"
    INPUT_ADDRESS = By.XPATH, "//input[@type='text' and @placeholder='* Адрес: куда привезти заказ']"
    INPUT_PHONE = By.XPATH, "//input[@type='text' and @placeholder='* Телефон: на него позвонит курьер']"
    INPUT_DATA = By.XPATH, "//button[text()='* Когда привезти самокат']"
    INPUT_METRO = By.XPATH, "//input[@placeholder='* Станция метро']"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"
    #page_order_2
    RENTAL_DATA = By.XPATH, "//input[@type='text' and @placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD = By.XPATH, "//div[text()='* Срок аренды']"
    COLOR_SCOOTER = By.XPATH, "//input[@id='black']"
    BUTTON_ORDER_END = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"
    BUTTON_ORDER_YES = By.XPATH, "//button[text()='Да']"
    ORDER_DONE = By.XPATH, "//div[text()='Заказ оформлен']"
    MAIN_LOGO = By.XPATH, "//img[@alt='Scooter']"
    CHECK_MAIN_PAGE = By.XPATH, "//div[text()='Привезём его прямо к вашей двери,']"
    LOGO_YANDEX = By.XPATH, "//img[@alt='Yandex']"
    BUTTON_CHECK_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"
    SCOOTER_DONE = By.XPATH, "//div[text()='Самокат на складе']"


