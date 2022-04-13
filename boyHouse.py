from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
btn = browser.find_element_by_id("book")
btn.click()

x_element = browser.find_element(By.ID, "input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);",  x_element)
x = x_element.text
y = calc(x)
input3 = browser.find_element(By.ID, "answer")
input3.send_keys(y)

button1 = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);",  button1)
button1.click()





