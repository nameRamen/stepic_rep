from pages.selenium_course import UnitLesson


class TestSeleniumCourse:

    def test_registration(self, driver):
        unittests_lesson = UnitLesson(driver, "http://suninjuly.github.io/registration2.html")
        unittests_lesson.open()
        actual_text = unittests_lesson.registration_required_fields()
        expected_text = "Congratulations! You have successfully registered!"
        assert actual_text == expected_text, "Actual text doesn't match with expected text"
