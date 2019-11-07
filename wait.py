from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element_by_id("book")
button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print(y)

browser.find_element_by_id("answer").send_keys(y)

button1 = browser.find_element_by_id("solve")
button1.click()

# browser.implicitly_wait(5)
# browser.get("http://suninjuly.github.io/wait1.html")
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")

# assert "successful" in message.text
