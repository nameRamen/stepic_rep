import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope='function')  # 'function' - используем фикстуру в каждом тесте
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()