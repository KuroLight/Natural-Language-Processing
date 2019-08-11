"""
refer:
https://github.com/Brucepk/163SingerTop50/blob/master/singers163.py
"""

# coding:utf-8
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from utils import *
from tqdm import tqdm

SCRIPT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(SCRIPT_ROOT, "../utils/chromedriver")
DATA_PATH = os.path.join(SCRIPT_ROOT, '../data')
driver = webdriver.Chrome(executable_path=DRIVER_BIN)
wait = WebDriverWait(driver, 1)  # 设置等待时间 5


def get_song_names(artist_id, chinese_name=True):
    top50url = 'http://music.163.com/#/artist?id={}'.format(artist_id)
    driver.get(top50url)
    driver.switch_to.frame('g_iframe')
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    song_info = soup.select('div div div span a b')
    song_names = re.findall('title="(.*?)"', str(song_info))

    if not chinese_name:
        return song_names

    song_names_chinese = []
    for song_name in song_names:
        pattern = "[\u4e00-\u9fa5]+"
        regex = re.compile(pattern)
        results = regex.findall(song_name)
        if not results:
            pass
        else:
            song_name = ''.join(results)
            song_names_chinese.append(song_name)

    return song_names_chinese


def main():
    for artist_file_name in ['chinese_women']:  # 'chinese_band','chinese_men','chinese_women'
        id_names = read_list_from_txt(os.path.join(DATA_PATH, artist_file_name + '.txt'))
        song_file_name = os.path.join(DATA_PATH, artist_file_name + '_songs.txt')

        if os.path.exists(song_file_name):
            check_ids = [line.strip().split()[0] for line in read_list_from_txt(song_file_name)]
        else:
            check_ids = []
        for line in tqdm(id_names):
            line = line.strip()
            # print(line)
            artist_id, artist_name = line.split('\t')
            if artist_id in check_ids:
                continue
            # print(artist_id, artist_name)
            song_names = get_song_names(artist_id, chinese_name=False)
            # print(song_names)
            with open(song_file_name, 'at', encoding='utf8') as f:
                f.write('%s\t%s\t%s\n' % (artist_id, artist_name, '\t'.join(song_names)))


if __name__ == '__main__':
    main()
