from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


def race_scraping(main_driver, url):
    main_driver.get(url)
    time.sleep(2)
    return main_driver


def get_html(main_driver):
    # htmlを取得する
    html = main_driver.page_source
    # htmlから要素を抽出する
    soup = BeautifulSoup(html, 'html.parser')
    return soup
