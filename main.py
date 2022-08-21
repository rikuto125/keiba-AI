from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

from access import race_scraping, get_html
from shutuba_table_arrange import shutuba_table_arrange

webdriver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://race.netkeiba.com/race/shutuba.html?race_id=202201020411"

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    print('スクリプトを実行します。')
    webdriver = race_scraping(webdriver, url)
    html = get_html(webdriver)
    shutuba_table_arrange(url)
    print('スクリプトを終了します。')
    webdriver.quit()
