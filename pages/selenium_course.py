from loacators.locators import UnittestLocators
from pages.base_page import Initial


class UnitLesson(Initial):
    locator = UnittestLocators()

    def registration_required_fields(self):
        self.element_is_visible(self.locator.FIRST_NAME).send_keys('Roman Sechin')
        self.element_is_visible(self.locator.EMAIL).send_keys('RomanSechin@gmail.com')
        self.element_is_visible(self.locator.SUBMIT_BUTTON).click()
        actual_text = self.element_is_visible(self.locator.WELCOME_TEXT).text
        return actual_text
