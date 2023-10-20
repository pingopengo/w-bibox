from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login import login_to_site
from utils.scanner import scan_pages
from utils.secrets import user, pw


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

    # After all pages are captured, save them as a single PDF
    image_list[0].save("output/book.pdf", save_all=True, append_images=image_list[1:])
    browser.quit()


if __name__ == "__main__":
    main()
