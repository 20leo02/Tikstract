from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import requests


def init_driver():
    """Initializes driver."""
    opts = FirefoxOptions()

    opts.add_argument("--headless")
    opts.add_argument("--test-type")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--incognito")
    opts.add_argument("--start-maximized")
    opts.add_argument("--no-sandbox")
    opts.add_argument('window-size=1920,1080')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--allow-running-insecure-content')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument('--disable-extensions')
    opts.add_argument('disable-infobars')

    firefoxpath = '/Users/leo/browser/geckodriver'
    driver = webdriver.Firefox(options=opts, executable_path=firefoxpath)
    return driver

def download_tiktok(link):
    """Downloads the tiktok.
    :param link: URL to the tiktok
    :type link: String"""
    driver = init_driver()

    X_PATH_TT = '//span[1]//div[1]//div[1]//div[5]//div[1]//div[1]//div[1]//span[2]'
    driver.get(link)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, X_PATH_TT)))
    tiktok = driver.find_element(By.XPATH, X_PATH_TT)
    prevSibling = tiktok.find_element_by_xpath('.//preceding-sibling::*')
    downloadlink = prevSibling.get_attribute('src')
    driver.close()

    r = requests.head(link)
    cookies = r.cookies.get_dict()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "v16-web.tiktok.com",
        "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Referer": f"{link}"}

    r = requests.get(downloadlink, headers=headers,cookies=cookies)
    with open('tiktok.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)