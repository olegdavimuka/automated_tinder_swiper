import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

FACEBOOK_EMAIL = os.environ.get("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.environ.get("FACEBOOK_PASSWORD")

# Setting up Selenium
chrome_driver_path = "C:\Coding\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.set_window_size(800, 1000)
driver.get("http://www.tinder.com")
time.sleep(2)

# Logging in to Tinder
login_button = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/div/main/div/div[2]/div/div['
                                             '3]/div/div/button[2]')
login_button.click()
time.sleep(2)

more_options_button = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/button')
if more_options_button.text == "More Options":
    more_options_button.click()
    time.sleep(2)

facebook_login_button = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div['
                                                      '2]/button')
facebook_login_button.click()
time.sleep(2)

# switching windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Facebook authorization
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys(FACEBOOK_EMAIL)
password_input = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_input.send_keys(FACEBOOK_PASSWORD)
login_button3 = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
login_button3.click()
time.sleep(5)

# Accepting notifications at start
driver.switch_to.window(base_window)
cookies_allow_button = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[2]/div/div/div[1]/button')
cookies_allow_button.click()
time.sleep(2)
location_allow_button = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]')
location_allow_button.click()
time.sleep(2)
notifications_allow_button = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]')
notifications_allow_button.click()
time.sleep(2)

# Dismissing
dismiss_button = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/div/main/div/div/div[1]/div/div['
                                               '4]/div/div[2]/button')
while True:
    dismiss_button.click()
    time.sleep(2)
