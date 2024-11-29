# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


import time

url = "https://tuff-ek.com/login"
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--incognito")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")  # Start maximized
options.add_argument("--disable-infobars")


driver = webdriver.Chrome(options=options)
# driver.maximize_window()

driver.get(url)

time.sleep(1)

username = "emma4645"
password = "123123"

try:
    # Wait for the element to be present
    search_element = "van-field-1-input"
    element = driver.find_element(By.ID, search_element)
    print("Login...")
    element.send_keys(username)
    # element
except TimeoutException:
    print("Element not found within the given time", search_element)
except NoSuchElementException:
    print("Element not found")


try:
    # Wait for the element to be present
    search_element = "van-field-2-input"
    element = driver.find_element(By.ID, search_element)
    # print("password Element found", element)
    element.send_keys(password)
except TimeoutException:
    print("Element not found within the given time", search_element)
except NoSuchElementException:
    print("Element not found")

driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/button[2]').click()

time.sleep(2)

dialog = driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div[4]/div[2]')
# print('Dialog element: ', dialog)
dialog.click()

time.sleep(2)

starting_item = driver.find_element(
    By.XPATH, '(//div[@class="van-tabbar-item" and @role="tab"])[2]')
print('stating element: ', starting_item, starting_item.text)
starting_item.click()

time.sleep(4)

clickable_elements = driver.find_elements(
    By.XPATH, '//*[@onclick] | //a | //button | //div[@role="button"]')

print('Clickable elements: ', clickable_elements)
for element in clickable_elements:
    print('Clickable element: ', element, element.get_attribute('outerHTML'))


# <div data-v-20b89939 = "" class = "submit_btn" > <div data-v-20b89939 = "" class = "van-image" style = "width: 100px; height: 100px;" > <img src = "/assets/lottery_btn1-4e35cb04.png" class = "van-image__img" > <!--- -> <!--- -> </div > <p data-v-20b89939 = "" style = "position: absolute; bottom: 15px; text-align: center; left: 22%; font-size: 16px; color: rgb(255, 255, 255);" > 14 / 50 < /p > </div >
try:

    # WebDriverWait(driver, 10).until(
    #     EC.invisibility_of_element_located((By.CSS_SELECTOR, "img.i_img"))
    # )

    # Now click the desired element
    # submit_button = driver.find_element(
    #     By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div')
    # print('submit_button element: ', submit_button, submit_button.text)
    # driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    # time.sleep(1)  # Wait for the scroll action to complete

    # submit_button.click()

    submit_button = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div')
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

    # Now click the element
    # submit_button.click()
    print('submit_button element: ', submit_button, submit_button.text)
    time.sleep(5)

except TimeoutException:
    print("Element not found within the given time", submit_button)
except NoSuchElementException:
    print("Element not found")

# submit_button = driver.find_element(
#     By.CSS_SELECTOR, 'div.van-image > img.van-image__img[src="/assets/lottery_btn1-4e35cb04.png"]')

# print('submit_button element: ', submit_button, submit_button.text)
# submit_button.click()

time.sleep(5)

# go to product promotion
