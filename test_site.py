from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser


def test_open_Forgote_password(browser):
    browser.get('https://test.hu-li.com/en/auth/login')
    forgot_password = browser.find_element(By.LINK_TEXT, 'Forgot password?')
    forgot_password.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Forgot password?'