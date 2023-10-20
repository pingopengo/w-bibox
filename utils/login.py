from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_site(browser, user, pw):
    # Click on the "Kundenkonto" button
    kundenkonto_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Kundenkonto"]'))
    )
    kundenkonto_button.click()

    time.sleep(3)

    # Click on the "Anmelden" button to navigate to the login page
    anmelden_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/backend/oauth2/login")]'))
    )
    anmelden_button.click()
    time.sleep(3)

    # Fill in the login form
    # Type the username
    username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'account'))
    )
    username_input.send_keys(user)

    # Type the password
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_input.send_keys(pw)

    # Click the "Anmelden" button
    anmelden_submit_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@name="action" and @value="login"]'))
    )
    anmelden_submit_button.click()
