import random
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from access import race_scraping

webdriver = webdriver.Chrome(ChromeDriverManager().install())

# netkeibaのdbのurl
url = "https://db.netkeiba.com/"

# urlをゲットしてsleep
webdriver = race_scraping(webdriver, url)

# レースをクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="page"]/div[1]/ul/li[7]/a')
elem.click()
time.sleep(2)

# 詳細検索をクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="db_search_form"]/form/div/ul/li[1]/a')
elem.click()
time.sleep(2)

# 競争種別芝をクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="check_track_1"]')
elem.click()
time.sleep(2)

# 競争種別ダートをクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="check_track_2"]')
elem.click()
time.sleep(2)

# 競争種別障害をクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="check_track_3"]')
elem.click()
time.sleep(2)

# 期間をselectする
# 2022年1月から2022年12月までを選択する optionの部分で2~13で月を指定
start_year = webdriver.find_element(By.XPATH,
                                    '//*[@id="db_search_detail_form"]/form/table/tbody/tr[3]/td/select[1]/option[2]')
start_year.click()
time.sleep(2)

start_month = webdriver.find_element(By.XPATH,
                                     '//*[@id="db_search_detail_form"]/form/table/tbody/tr[3]/td/select[2]/option[2]')
start_month.click()
time.sleep(1)

end_year = webdriver.find_element(By.XPATH,
                                  '//*[@id="db_search_detail_form"]/form/table/tbody/tr[3]/td/select[3]/option[2]')
end_year.click()
time.sleep(2)

end_month = webdriver.find_element(By.XPATH, '//*[@id="db_search_detail_form"]/form/table/tbody/tr[3]/td/select['
                                             '4]/option[13]')
end_month.click()
time.sleep(1)

# 競馬場を選択
# 1~10のリストを作成
list_ = []
for i in range(1, 11):
    list_.append(str(i).zfill(2))

for i in list_:
    elem = webdriver.find_element(By.XPATH, '//*[@id="check_Jyo_' + i + '"]')
    elem.click()
    time.sleep(random.randint(1, 2))

# 検索件数100をクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="db_search_detail_form"]/form/table/tbody/tr[11]/td/select/option[3]')
elem.click()
time.sleep(2)

# 検索をクリック
elem = webdriver.find_element(By.XPATH, '//*[@id="db_search_detail_form"]/form/div/input[1]')
elem.click()
time.sleep(2)

# htmlを取得する
html = webdriver.page_source
time.sleep(2)
# htmlから要素を抽出する
soup = BeautifulSoup(html, 'html.parser')

# raceと文字列が含まれるaタグを取得する
a_tags = soup.find_all('a')

# class="pager"のtextを取得する
pager = soup.find_all('div', class_='pager')
text = pager[0].text.split("件")[0]
text = text.replace(",", "")
kensu = int(text)
if kensu > 100:
    pages = kensu // 100
else:
    pages = 1

# idを取得する
race_id_list = []  # id格納先
for page in range(0, pages, 1):
    # aタグのリストを取得する
    a_tags_list = []
    for a_tag in a_tags:
        # html型のaタグを文字列型に変換する
        if "race/20" in str(a_tag):
            a_tags_list.append(a_tag.get('href'))

    # a_tags_listからrace_idを取り出す
    for i in a_tags_list:
        # "/"で区切り配列２にidがある
        split_data = i.split("/")
        race_id_list.append(split_data[2])

    # ページ遷移 pagesが2以上かを判定し１なら遷移しない
    if pages != 1:
        if page == 0:
            elem = webdriver.find_element(By.XPATH, '//*[@id="contents_liquid"]/div[2]/a')
            elem.click()
            time.sleep(5)

        else:
            elem = webdriver.find_element(By.XPATH, '//*[@id="contents_liquid"]/div[2]/a[2]')
            elem.click()
            time.sleep(5)

print(race_id_list)

# race_id_listをpickleファイルに
race_id_pickle = pd.DataFrame(race_id_list)
race_id_pickle.columns = ["race_id"]
race_id_pickle.to_pickle("race_id_list).pickle")

webdriver.quit()
