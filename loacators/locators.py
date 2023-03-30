from selenium.webdriver.common.by import By


class RegistrationLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
    EMAIL = (By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    WELCOME_TEXT = (By.TAG_NAME, "h1")


class AuthLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#ember33')
    EMAIL = (By.CSS_SELECTOR, 'input[name="login"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    MODAL_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    MODAL_WINDOW = (By.CSS_SELECTOR, 'div[class="light-tabs ember-view"]')

    ANSWER_TEXTAREA = (By.CSS_SELECTOR, 'textarea[class="ember-text-area ember-view textarea string-quiz__textarea"]')
    SEND_BUTTON = (By.CSS_SELECTOR, 'button[class="submit-submission"]')
    FEED_BACK = (By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')
    TRY_AGAIN_BUTTON = (By.CSS_SELECTOR, 'button[class="again-btn white"]')


class PageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
