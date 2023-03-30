import time

import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')  # 'function' - используем фикстуру в каждом тесте
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def authorization(driver):
    driver.find_element(By.CSS_SELECTOR, 'a[href="/lesson/236895/step/1?auth=login"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys('romansecin474@gmail.com')
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('Se4inromka311')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    # driver.find_element(By.CSS_SELECTOR, 'div[class="light-tabs ember-view"]')

