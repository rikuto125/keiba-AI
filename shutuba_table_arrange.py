from bs4 import BeautifulSoup
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import pandas as pd


def shutuba_table_arrange(url):
    # htmlからpandasで表を作成する
    df = pd.read_html(url)[0]
    print(df)
