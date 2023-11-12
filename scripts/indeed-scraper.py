from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import random

def get_url(position, location):
    template = "https://www.indeed.ca/jobs?q={}&l={}&sort=date"
    url = template.format(position.replace(' ', '+'),
                          location.replace(' ', '+'))
    return url

def get_job_data(driver, target_url):
    driver.get(target_url)
    time.sleep(random.uniform(9, 10.9))
    try:
        close = driver.find_element('xpath', '//*[@id="mosaic-desktopserpjapopup"]/div[1]/button')
        close.click()
    except:
        pass

    all_data = []

    job_cards = driver.find_elements('xpath', '//div[@class = "css-1m4cuuf e37uo190"]' )

    for card in job_cards:
        card.location_once_scrolled_into_view
        card.click()
        # Wait up to 5 seconds for an element to be present on the DOM of a page and visible.
        wait = WebDriverWait(driver, 4.9)
        try:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div[1]/div/div[5]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/h2")))
            # You can now interact with the element since it's visible
            job_title = element.text.strip()
            title = job_title.split('\n')   # We can stil fix this
            data = {'Job Title': title}
            print(data)
            all_data.append(data)
        except:
            # This block will be executed if the element is not visible within 10 seconds
            print("Timed out waiting for the element to become visible.")

def get_job_company(driver, target_url):
    pass


def main():
    # PROXY = ""
    # chrom_options = webdriver.ChromeOptions()
    # chrom_options.add_argument(f'--proxy-server={PROXY}')
    position = 'Software Engineer Intern'
    location = 'Vancouver, BC'
    jobs = []
    url =get_url(position, location)
    browser = webdriver.Chrome()
    for page in range(0, 50, 10):
        order_page = (url + '&start=' +str(page)) #URL
        print(order_page) # https://www.indeed.ca/jobs?q=Software+Engineer+Intern&l=Vancouver,+BC&sort=date&start=0 
        # browser.get(order_page)
        time.sleep(random.uniform(9, 10.5)) # 
        # We need to add close modal button just in case if theres notifications popped out
        get_job_data(browser, order_page)
    browser.close()

main()

