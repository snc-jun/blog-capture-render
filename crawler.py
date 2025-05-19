import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_crawler():
    SAVE_DIR = "static/captures"
    os.makedirs(SAVE_DIR, exist_ok=True)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280x1024")

    driver = webdriver.Chrome(options=options)

    # まずはテストでexample.comをキャプチャ
    driver.get("https://example.com")
    time.sleep(2)
    driver.save_screenshot(os.path.join(SAVE_DIR, "example.png"))

    driver.quit()
