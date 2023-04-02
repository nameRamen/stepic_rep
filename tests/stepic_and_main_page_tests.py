import pytest

from pages.main_page import RegistrationLesson, AuthLesson, MainPage, LoginPage


class TestStepicCourse:

    @pytest.mark.parametrize('link', ['registration1', 'registration2'])
    def test_registration_page(self, driver, link):
        page = RegistrationLesson(driver, f"http://suninjuly.github.io/{link}.html")
        page.open()
        actual_text = page.fill_fields_and_get_actual_text()
        expected_text = "Congratulations! You have successfully registered!"
        assert actual_text == expected_text, "Actual text doesn't match with expected text"

    @pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_stepic_parametrization(self, driver, link):
        page = AuthLesson(driver, f'https://stepik.org/lesson/{link}/step/1')
        page.open()
        page.login_to_stepic()
        actual_feedback = page.get_feedback()
        expected_feedback = 'Correct!'
        assert actual_feedback == expected_feedback, "Feed back is incorrect"


class TestMainPage:

    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, "http://selenium1py.pythonanywhere.com/")
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()
