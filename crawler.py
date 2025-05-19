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
        print("🟡 クローラー起動中...")
        driver = webdriver.Chrome(options=options)

        driver.get("https://example.com")
        time.sleep(2)

        filename = "example.png"
        path = os.path.join(SAVE_DIR, filename)
        driver.save_screenshot(path)
        print(f"✅ スクリーンショット保存済み: {path}")

        driver.quit()

    except Exception as e:
        print(f"❌ クローラーエラー: {e}")
