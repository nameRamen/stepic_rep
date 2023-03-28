from selenium.webdriver.common.by import By


class UnittestLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '[placeholder="Input your name"]')
    EMAIL = (By.CSS_SELECTOR, '[placeholder="Input your email"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button")
    WELCOME_TEXT = (By.TAG_NAME, "h1")
