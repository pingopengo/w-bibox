from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login import login_to_site
from utils.scanner import scan_pages
from utils.secrets import user, pw
from utils.png2pdf import combine_images_to_pdf

def main():
    options = Options()
    options.headless = False
    browser = webdriver.Firefox(options=options)
    browser.get("https://www.westermann.de")

    # Handle cookie overlay

    accept_cookies_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Alle akzeptieren"]')))
    accept_cookies_button.click()

    # Login to the website
    login_to_site(browser, user, pw)

    # Navigate to the book manually, scan the pages
    image_list = scan_pages(browser)

    combine_images_to_pdf(image_list, "../output/IT Berufe LF 10-12.pdf")


if __name__ == "__main__":
    main()
