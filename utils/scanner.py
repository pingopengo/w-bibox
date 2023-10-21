from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io
import requests
import os


def scan_pages(browser):
    image_list = []
    previous_first_image_src = ""
    page = 1

    while True:
        # Wait for page to load
        WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page"))
        )

        # Parse the page
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        aps = soup.find_all('app-page')

        # Get the first image's source URL
        if aps:
            first_image = aps[0].find('img')
            if first_image:
                first_image_src = first_image['src']
                print(first_image_src)
                if first_image_src == previous_first_image_src:
                    break
            else:
                continue

        # Save images
        for ap in aps:
            for img in ap.find_all('img'):
                r = requests.get(img['src'], stream=True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    image = Image.open(io.BytesIO(r.content))
                    image_path = f"output/ItBerufe1012/page_{len(image_list) + 1}.png"
                    image.save(image_path)
                    image_list.append(image_path)  # Store the path instead of the image object
                    if isinstance(image, Image.Image):
                        image.close()

                else:
                    print(f"Error: {r.status_code} for image {img['src']}")

        # Update the previous first image's source URL
        previous_first_image_src = first_image_src

        # Go to the next page
        page += 2
        browser.get(f"https://bibox2.westermann.de/book/5417/page/{page}")

    return image_list
