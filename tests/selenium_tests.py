import unittest

from selenium.webdriver.common.by import By
import time
from pages.selenium_course import UnitLesson
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def test_reg_unit(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]')
        input1.send_keys("Roman Sechin")
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input2.send_keys("RomanSechin@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Doesn't match")


if __name__ == "__main__":
    unittest.main()

    # def test_registration(self, driver):
    #     unittests_lesson = UnitLesson(driver, "http://suninjuly.github.io/registration2.html")
    #     unittests_lesson.open()
    #     actual_text = unittests_lesson.registration_required_fields()
    #     expected_text = "Congratulations! You have successfully registered!"
    #     self.assertEqual(actual_text, expected_text, "Actual text doesn't match with expected text")
