from loacators.locators import RegistrationLocators, AuthLocators, PageLocators
from pages.base_page import BasePage
import time
import math


class UnitLesson(BasePage):
    locator = RegistrationLocators()

    def fill_fields_and_get_actual_text(self):
        self.element_is_visible(self.locator.FIRST_NAME).send_keys('Roman')
        self.element_is_visible(self.locator.LAST_NAME).send_keys('Sechin')
        self.element_is_visible(self.locator.EMAIL).send_keys('RomanSechin@gmail.com')
        self.element_is_visible(self.locator.SUBMIT_BUTTON).click()
        actual_text = self.element_is_visible(self.locator.WELCOME_TEXT).text
        return actual_text


class AuthLesson(BasePage):
    locator = AuthLocators()

    def login_to_stepic(self):
        self.element_is_visible(self.locator.LOGIN_BUTTON).click()
        self.element_is_visible(self.locator.EMAIL).send_keys('romansecin474@gmail.com')
        self.element_is_visible(self.locator.PASSWORD).send_keys('Se4inromka311')
        self.element_is_visible(self.locator.MODAL_LOGIN_BUTTON).click()
        self.element_is_not_visible(self. locator.MODAL_WINDOW)

    def get_answer(self):
        answer = math.log(int(time.time()))
        self.element_is_visible(self.locator.ANSWER_TEXTAREA).send_keys(answer)
        self.element_is_clickable(self.locator.SEND_BUTTON).click()
        feed_back = self.element_is_visible(self.locator.FEED_BACK).text
        return feed_back

    def clean_result(self):
        self.element_is_visible(self.locator.TRY_AGAIN_BUTTON).click()


class MainPage(BasePage):
    locator = PageLocators()

    def go_to_login_page(self):
        self.element_is_visible(self.locator.LOGIN_LINK).click()

    def should_be_login_link(self):
        pass