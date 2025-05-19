import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def run_crawler():
    SAVE_DIR = "static/captures"
    os.makedirs(SAVE_DIR, exist_ok=True)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280x1024")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123 Safari/537.36")

    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://example.com")  # 安定するサイトでテスト
        time.sleep(2)
        screenshot_path = os.path.join(SAVE_DIR, "example.png")
        driver.save_screenshot(screenshot_path)
        print(f"✅ Screenshot saved to {screenshot_path}")
        driver.quit()
    except Exception as e:
        print(f"❌ クローラーエラー: {e}")
