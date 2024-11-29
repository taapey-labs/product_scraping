from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os


def scraping_linkedin(keyword, location):
    url = f"https://www.linkedin.com/jobs/search/?keywords={
        keyword}&location={location}"
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    driver.get(url)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    print(soup)
    time.sleep(10)
    # driver.quit()


if __name__ == '__main__':
    keyword = "python developer"
    location = "Worldwide"
    scraping_linkedin(keyword, location)
