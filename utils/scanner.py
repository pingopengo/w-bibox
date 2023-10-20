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


def scan_pages(browser):
    image_list = []

    # Step 1: Store the source (URL) of the first image of the current page.
    previous_first_image_src = ""

    page = 1
    while True:
        elem = WebDriverWait(browser, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page"))  # This is a dummy element
        )
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        aps = soup.find_all('app-page')

        # Step 2: Check if the source of the first image of the current page is the same as the source of the first
        # image of the previous page.
        if aps:
            if aps:
                first_image = aps[0].find('img')
                if first_image:
                    first_image_src = first_image['src']
                else:
                    continue

            first_image_src = aps[0].find('img')['src']

            if first_image_src == previous_first_image_src:
                break

        for idx, ap in enumerate(aps):
            for img_idx, img in enumerate(ap.find_all('img')):
                r = requests.get(img['src'], stream=True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    image = Image.open(io.BytesIO(r.content))
                    image_list.append(image)
                    image_path = f"output/book1/page_{len(image_list)}.png"
                    image.save(image_path)
                else:
                    print(f"Error: {r.status_code}")

        page += 2
        browser.get("https://bibox2.westermann.de/book/5413/page/" + str(page))


    return image_list
