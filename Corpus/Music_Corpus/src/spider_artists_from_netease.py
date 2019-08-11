"""
refer:
https://github.com/Brucepk/163SingerTop50/blob/master/singers163.py
"""

from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from tqdm import tqdm

CHINESE_MEN = [1001]
CHINESE_WOMEN = [1002]
CHINESE_BAND = [1003]
HOT = [-1]
OTHERS = [0]
ATOZ = list(range(65, 91))

CHINESE_ARTISTS_CLASS = {
    '1001': 'chinese_men',
    '1002': 'chinese_women',
    '1003': 'chinese_band'
}
NAME_INITIAL_LIST = HOT + ATOZ + OTHERS

# browser = webdriver.Chrome()
# browser = webdriver.Chrome('/path/to/chromedriver')
SCRIPT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(SCRIPT_ROOT, "../utils/chromedriver")
DATA_PATH = os.path.join(SCRIPT_ROOT, '../data')

driver = webdriver.Chrome(executable_path=DRIVER_BIN)
wait = WebDriverWait(driver, 5)  # 设置等待时间


def get_singer(url, chinese_name=True):  # 返回歌手名字和歌手id
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    info = soup.select('.nm.nm-icn.f-thide.s-fc0')
    id_artist = {}
    for snames in info:
        artist_name = snames.get_text()
        if chinese_name:
            pattern = "[\u4e00-\u9fa5]+"
            regex = re.compile(pattern)
            results = regex.findall(artist_name)
            if not results:
                continue
            else:
                artist_name = ''.join(results)
        # print(artist_name)
        artist_id = str(re.findall('href="(.*?)"', str(snames))).split('=')[1].split('\'')[0]
        # id_artist.append((artist_id, artist_name))
        id_artist[artist_id] = artist_name
    return id_artist


def save_to_txt(data, save_path):
    print('保存歌手信息中...请稍后查看')
    with open(save_path, 'wt', encoding='utf8') as f:
        for artist_id, artist_name in data:
            f.write('%s\t%s\n' % (artist_id, artist_name))


def main():
    for id, cls in CHINESE_ARTISTS_CLASS.items():

        temp = {}
        for init in tqdm(NAME_INITIAL_LIST):
            url = 'https://music.163.com/#/discover/artist/cat?id=%s&initial=%s' % (id, init)
            temp.update(get_singer(url, chinese_name=False))

        id_artist = list(temp.items())
        id_artist.sort(key=lambda x: int(x[0]))

        file_name = cls + '.txt'
        save_to_txt(id_artist, save_path=os.path.join(DATA_PATH, file_name))


if __name__ == '__main__':
    main()
