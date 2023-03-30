import pytest

from pages.selenium_course_page import UnitLesson, AuthLesson, MainPage


class TestSeleniumCourse:

    @pytest.mark.xfail
    @pytest.mark.parametrize('link', ['registration1', 'registration2'])
    def test_registration_page(self, driver, link):
        unittests_lesson = UnitLesson(driver, f"http://suninjuly.github.io/{link}.html")
        unittests_lesson.open()
        actual_text = unittests_lesson.fill_fields_and_get_actual_text()
        expected_text = "Congratulations! You have successfully registered!"
        assert actual_text == expected_text, "Actual text doesn't match with expected text"

    @pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_stepic_parametrization(self, driver, link):
        parametrization_lesson = AuthLesson(driver, f'https://stepik.org/lesson/{link}/step/1')
        parametrization_lesson.open()
        parametrization_lesson.login_to_stepic()
        actual = parametrization_lesson.get_answer()
        parametrization_lesson.clean_result()
        expected = 'Correct!'
        assert actual == expected, "Feed back is incorrect"

    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, "http://selenium1py.pythonanywhere.com/")
        page.open()
        page.go_to_login_page()