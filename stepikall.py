# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# ---------------------------------

# from selenium import webdriver
# import pyperclip
# import time
# import math
#
# def calc(x):
# 	return str( math.log (abs ( 12 * math.sin( x ) ) ) )
#
# link='http://suninjuly.github.io/alert_accept.html'
#
#
# try:
#    browser=webdriver.Chrome()
#    browser.get(link)
#    browser.find_element_by_css_selector('button').click()
#    confirm = browser.switch_to.alert
#    confirm.accept()
#    x_string = browser.find_element_by_id("input_value")
#    x_number = int(x_string.text)
#    answer = calc(x_number)
#    input_answer = browser.find_element_by_id("answer")
#    input_answer.send_keys(answer)
#    send_button = browser.find_element_by_class_name("btn-primary")
#    send_button.click()
#    alert = browser.switch_to.alert
#    alert_text = alert.text
#    addToClipBoard = alert_text.split(': ')[-1]
#    pyperclip.copy(addToClipBoard)
#
# finally:
#     time.sleep(5)
#     browser.quit()

# ------------------------------

# from selenium import webdriver
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(x))))
#
# link='http://suninjuly.github.io/redirect_accept.html'
#
# try:
#     browser=webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_css_selector('button').click()
#
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x_string = browser.find_element_by_id("input_value")
#     x_number = int(x_string.text)
#     answer = calc(x_number)
#     input_answer = browser.find_element_by_id("answer").send_keys(answer)
#     send_button = browser.find_element_by_class_name("btn-primary").click()
#
#
#
# finally:
#     time.sleep(10)
#     browser.quit()

# -------------------------

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(x))))
#
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option('w3c', False)
#
# link='http://suninjuly.github.io/explicit_wait2.html'
#
# try:
#     browser=webdriver.Chrome()
#     browser.get(link)
#
#     book_button=browser.find_element_by_id('book')
#     price=WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.ID, "price"), "$100")
#     )
#     book_button.click()
#
#     x_string = browser.find_element_by_id("input_value")
#     x_number = int(x_string.text)
#     answer = calc(x_number)
#     input_answer = browser.find_element_by_id("answer").send_keys(answer)
#     send_button = browser.find_element_by_id("solve").click()
#
#
# finally:
#     time.sleep(20)
#     browser.quit()

# --------------------

