from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
# import time
import random


def get_element_by_xpath(driver, search_key, sleep_time=0, debug=False):
    try:
        element = driver.find_element(By.XPATH, search_key)
        # element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, search_key))
        # )
        driver.implicitly_wait(sleep_time)
        if debug:
            print(f"get_element_by_xpath...{search_key}")
        return element
    except TimeoutException:
        print(f"Element not found within the given time {search_key}")
        return None
    except NoSuchElementException:
        print(f"Element not found {search_key}")
        return None


def get_element_by_id(driver, search_key, sleep_time=0, debug=False):
    try:
        # element = driver.find_element(By.ID, search_key)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, search_key))
        )
        driver.implicitly_wait(sleep_time)
        if debug:
            print(f"get_element_by_xpath...{search_key}")
        return element
    except TimeoutException:
        print(f"Element not found within the given time {search_key}")
        return None
    except NoSuchElementException:
        print(f"Element not found {search_key}")
        return None


def click_element_by_id(driver, search_key, sleep_time=0, debug=False):
    try:
        # Wait for the element to be present
        element = driver.find_element(By.ID, search_key)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, search_key))
        )
        print(f"{search_key} ...element... {element}")
        element.click()
        driver.implicitly_wait(sleep_time)
        if debug:
            print(f"click_element_by_ID...{search_key}")
    except TimeoutException:
        print(f"Element not found within the given time {search_key}")
        return None
    except NoSuchElementException:
        print(f"Element not found {search_key}")
        return None


def click_element_by_xpath(driver, search_key, sleep_time=0, debug=False):
    try:
        # Wait for the element to be present
        element = driver.find_element(By.XPATH, search_key)
        element.click()
        driver.implicitly_wait(sleep_time)
        if debug:
            print(f"click_element_by_xpath...{search_key}")
    except TimeoutException:
        print(f"Element not found within the given time {search_key}")
        return None
    except NoSuchElementException:
        print(f"Element not found {search_key}")
        return None


def click_element_by_name(driver, search_key, sleep_time=0, debug=False):
    try:
        element = driver.find_element(By.NAME, search_key)
        element.click()
        driver.implicitly_wait(sleep_time)
        # time.sleep(sleep_time)

        # WebDriverWait(timeout=sleep_time)
        if debug:
            print(f"click_element_by_name...{search_key}")
    except TimeoutException:
        print("Element not found within the given time", search_key)
        return None
    except NoSuchElementException:
        print(f"Element not found, {search_key}")
        return None


def send_key_by_id(driver, search_key, value, debug=False):
    try:
        element = driver.find_element(By.ID, search_key)
        if debug:
            print(f"send_key_by_name...{search_key} {value}, {element}")
        element.send_keys(value)
        return element
    except TimeoutException:
        print("Element not found within the given time", search_key)
        return None
    except NoSuchElementException:
        print(f"Element not found {search_key}")
        return None


def send_key_by_name(driver, search_key, value, debug=False):
    try:
        element = driver.find_element(By.NAME, search_key)
        element.send_keys(value)
        if debug:
            print(f"send_key_by_name...{search_key}")
        return element
    except TimeoutException:
        print("Element not found within the given time", search_key)
        return None
    except NoSuchElementException:
        print(f"Element not found {search_key}")
        return None


def select_element_from_dropdown(driver=None, tag_name='select', list_of_options=[], debug=False, sleep_time=0):
    try:
        select_options = Select(
            driver.find_element(By.TAG_NAME, tag_name))
        driver.implicitly_wait(sleep_time)
        option_text = random.choice(list_of_options)
        if debug:
            print(option_text)
        select_options.select_by_visible_text(option_text)
        driver.implicitly_wait(sleep_time)
        return option_text
    except TimeoutException:
        print("Element not found within the given time", tag_name)
        return None
    except NoSuchElementException:
        print(f"Element not found {tag_name}")
        return None
