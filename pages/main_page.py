import data.data
from generator.generator import generate_person
from loacators.locators import RegistrationLocators, AuthLocators, LoginPageLocators, MainPageLocators
from pages.base_page import BasePage
import time
import math


class RegistrationLesson(BasePage):
    locator = RegistrationLocators()

    def fill_fields_and_get_actual_text(self):
        person_info = next(generate_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        self.element_is_visible(self.locator.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locator.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locator.EMAIL).send_keys(email)
        self.element_is_visible(self.locator.SUBMIT_BUTTON).click()
        return self.element_is_visible(self.locator.WELCOME_TEXT).text


class AuthLesson(BasePage):
    locator = AuthLocators()

    def login_to_stepic(self):
        self.element_is_visible(self.locator.LOGIN_BUTTON).click()
        self.element_is_visible(self.locator.EMAIL).send_keys(data.data.LOGIN)
        self.element_is_visible(self.locator.PASSWORD).send_keys(data.data.PASSWORD)
        self.element_is_visible(self.locator.MODAL_LOGIN_BUTTON).click()
        self.element_is_not_visible(self.locator.MODAL_WINDOW)

    def get_feedback(self):
        answer = math.log(int(time.time()))
        self.element_is_visible(self.locator.ANSWER_TEXTAREA).send_keys(answer)
        self.element_is_clickable(self.locator.SEND_BUTTON).click()
        # self.element_is_visible(self.locator.TRY_AGAIN_BUTTON).click()
        return self.element_is_visible(self.locator.FEED_BACK).text


class MainPage(BasePage):
    locator = MainPageLocators()

    def go_to_login_page(self):
        self.element_is_visible(self.locator.LOGIN_LINK).click()
        # alert = self.driver.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.element_is_present(self.locator.LOGIN_LINK), "Login link is not presented"


class LoginPage(BasePage):
    locator = LoginPageLocators()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        expected_url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        current_url = self.get_current_page_url()
        assert expected_url == current_url, "Current url doesn't match with expected url"

    def should_be_login_form(self):
        assert self.element_is_visible(self.locator.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.element_is_visible(self.locator.REGISTRATION_FORM), "Registration form not found"
