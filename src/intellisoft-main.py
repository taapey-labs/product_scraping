# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import time
import random
# custom functions
from scrap_functions import click_element_by_xpath, send_key_by_name, get_element_by_xpath


list_of_options = [
    "That is great! I like this, it's very good",
    "I gave it a 5-star review, it's good",
    "For me, I would recommend it to my friends",
    "A very good one, great",
    "It looks good, but I'm not familiar with it yet",
    "Generally, I am not familiar with it yet",
]


list_of_options_index = [1, 2, 3, 4, 5, 6]


def run_intellisoft(logging_check=False):

    url = "https://www.intellisoft.rest/index/user/index.html"
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

    username = "nepalsingh"
    password = "N3wP@5s123!"
    # username = "XY40"
    # password = "123123"

    # Initial click to logon to the system
    search_element = "/html/body/div/a/button"
    click_element_by_xpath(
        driver=driver, search_key='/html/body/div/a/button', sleep_time=1, debug=True)

    send_key_by_name(driver=driver, search_key='tel', value=username)
    send_key_by_name(driver=driver, search_key='pwd', value=password)

    # Initial click to logon to the system
    search_element = "/html/body/div[1]/div[2]/div[3]/button"
    click_element_by_xpath(
        driver=driver, search_key=search_element, sleep_time=1)

    time.sleep(1)
    # access loggng page
    if logging_check:
        search_element = "/html/body/footer/div/a[3]"
        click_element_by_xpath(
            driver=driver, search_key=search_element, sleep_time=1, debug=True)

        # click on submit button on logging page
        search_element = "/html/body/div[3]/div[1]/div[1]/div[2]/span[2]"
        click_element_by_xpath(
            driver=driver, search_key=search_element, sleep_time=1, debug=True)

        search_element = """//*[@id="layui-layer1"]/div/div/div[2]/div[2]/div[6]/select"""

        select_options = Select(
            driver.find_element(By.TAG_NAME, 'select'))
        driver.implicitly_wait(1)

        option_text = random.choice(list_of_options)
        print(option_text)

        select_options.select_by_visible_text(option_text)
        time.sleep(5)

        search_element = """//*[@id="layui-layer1"]/div/div/div[2]/div[2]/div[7]"""
        click_element_by_xpath(
            driver=driver, search_key=search_element, sleep_time=5)

    # click on start button
    search_element = "/html/body/footer/div/a[2]"
    click_element_by_xpath(
        driver=driver, search_key=search_element, sleep_time=1)

    # scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # click on promotion start button
    search_element = """//*[@id="autoStart"]"""
    click_element_by_xpath(
        driver=driver, search_key=search_element, sleep_time=2)

    # # check is this final and exit if it is
    # search_element = """//*[@id="layui-layer4"]/div/div/div/div[3]"""
    # final_element = get_element_by_xpath(
    #     driver=driver, search_key=search_element, sleep_time=1, debug=True)
    # print('final_element', final_element, final_element.text)

    # time.sleep(10)

    # if final_element == None:
    #     print('Final element submission is completed')
    #     driver.quit()
    #     return None

    select_options = Select(
        driver.find_element(By.TAG_NAME, 'select'))
    driver.implicitly_wait(1)

    option_text = random.choice(list_of_options)
    option_index = random.choice(list_of_options_index)
    print('option_text', option_text, 'option_index', option_index)

    select_options.select_by_visible_text(option_text)
    # select_options.select_by_index(option_text)
    time.sleep(1)

    search_element = """//*[@id="layui-layer2"]/div/div/div[2]/div[2]/div[7]"""
    click_element_by_xpath(
        driver=driver, search_key=search_element, sleep_time=1)

    # click on promotion start button
    time.sleep(1)
    driver.quit()


# go to product promotion


for i in range(35):
    run_intellisoft(logging_check=False)
    print(f"Run# --> {i}")

    # if run_intellisoft():
    #     print(f"Run# --> {i}")
    # else:
    #     print(f"Run# --> {i}...completed")
    #     break
