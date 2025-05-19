from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

def run_crawler():
    SAVE_DIR = "static/captures"
    os.makedirs(SAVE_DIR, exist_ok=True)

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280x1024")
    options.add_argument("--user-agent=Mozilla/5.0")

    try:
        print("▶ クローラー開始")
        driver = webdriver.Chrome(options=options)
        base_url = "https://www.skylanternassociation.com/?page_id=590"
        driver.get(base_url)
        time.sleep(2)

        # 記事リンクを収集（aタグ + href含む記事へのリンク）
        links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="?p="]')
        visited = set()
        count = 1

        for link in links:
            url = link.get_attribute("href")
            if url and url not in visited:
                visited.add(url)
                print(f"📸 キャプチャ：{url}")
                driver.get(url)
                time.sleep(2)
                filename = f"article-{count:03}.png"
                driver.save_screenshot(os.path.join(SAVE_DIR, filename))
                count += 1

        driver.quit()
        print("✅ 全キャプチャ完了")

    except Exception as e:
        print(f"❌ エラー発生: {e}")
