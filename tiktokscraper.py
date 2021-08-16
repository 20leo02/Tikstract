from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import sys


def extract_video_url(tiktok_url):
    """Extracts a URL directing to an isolated TikTok video, given a TikTok
    URL.
    :param tiktok_url: A URL leading to a TikTok video
    :type tiktok_url: String
    :returns
    """
    try:
        page = urlopen(tiktok_url)
    except:
        sys.exit("Error opening the URL.")

    soup = BeautifulSoup(page, 'html.parser')
    content = soup.findAll("div")
    # video_url = content.find("video").get("src")
    print(content)

    # return url

def get_tiktok(url):
    pass


url = "https://www.tiktok.com/@vinsmoke.marcus/video/6971563278279380229?lang=en&is_copy_url=1&is_from_webapp=v1"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

assert "TikTok" in driver.title

try:
    page = urlopen(url)
except:
    sys.exit("Error opening the URL.")

soup = BeautifulSoup(page, 'html.parser')
content = soup.find_all("div")
# video_url = content.find("video").get("src")
print(content)
