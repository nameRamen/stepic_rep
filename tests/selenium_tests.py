import time
from math import sin, log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/explicit_wait2.html")
wait(driver, timeout=12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), text_="$100"))
book_button = driver.find_element(By.CSS_SELECTOR, "#book")
book_button.click()
x = driver.find_element(By.CSS_SELECTOR, "#input_value")
answer_field = driver.find_element(By.CSS_SELECTOR, "#answer")
answer = log(abs(12 * sin(int(x.text))))
answer_field.send_keys(answer)
submit_button = wait(driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#solve")))
submit_button.click()
time.sleep(5)
alert_obj = driver.switch_to.alert
msg = alert_obj.text
print(msg)
