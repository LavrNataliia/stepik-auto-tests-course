from selenium import webdriver
import math

browser = webdriver.Chrome()

link = browser.get("http://suninjuly.github.io/redirect_accept.html")
btn = browser.find_element_by_xpath("/html/body/form/div/div/button")
btn.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print(y)

browser.find_element_by_id("answer").send_keys(y)

button = browser.find_element_by_tag_name("button")
button.click()
