from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope='function')  # 'function' - используем фикстуру в каждом тесте
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())  # Инициализируем драйвер с помощью библиотеки
    driver.maximize_window()  # Устанавливаем по умолчанию окно на весь экран
    yield driver  # Предусловия окончены
    driver.quit()  # Постусловия


class Initial:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):  # Ожидаем видимости одного элемента
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):  # Ожидаем видимость нескольких
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):  # Проверяем по DOM дереву один элемент
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):  # Проверяем по DOM дереву несколько
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):  # Элемент невидим
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):  # Проверяем на кликабельность
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):  # Скролл до элемента
        self.driver.execute_script("arguments[0].scrollIntoView;", element)
