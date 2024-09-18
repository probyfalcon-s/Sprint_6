import pytest
import allure
from selenium import webdriver
from src.config import BASE_URL


@pytest.fixture
def driver():
    with allure.step("Создание драйвера"):
        firefox = webdriver.Firefox()
        firefox.get(BASE_URL)

        yield firefox

        firefox.quit()
