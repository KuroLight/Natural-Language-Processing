import requests
from pprint import pprint
import re
from utils import *
import os
from pypinyin import lazy_pinyin

# print(os.getcwd())


def get_singer_names(page_path, name_path):
    r = requests.get(page_path)
    r.encoding='utf8'
    text = r.text.split('\n')
    # print(text)

    records = []

    for line in text:
        line = line.strip()
        # print(line)
        """
        <li><a href="/singer/c1/singer_31915.html">阿俊</a></li>
        <li><a href="/singer/9b/singer_15890.html">阿科</a></li>
        <li><a href="/singer/9b/singer_15011.html">阿拉腾傲刀</a></li>
        <li><a href="/singer/63/singer_32466.html">阿来</a></li>
        <li><a href="/singer/18/singer_33249.html">阿赖</a></li>
        <li><a href="/singer/c1/singer_31312.html">a蓝</a></li>
        <li><a href="/singer/c2/singer_12213.html">阿郎</a></li>
        """
        search_object = re.search(r'html">([\u4e00-\u9fa5]+)</a></li>', line)
        if search_object:
            # print("search_object.group() : ", search_object.group())
            # print("search_object.group(1) : ", search_object.group(1))
            records.append('%s' % (search_object.group(1)))
        else:
            # print("No match!!")
            pass

    records = list(set(records))
    records.sort(key=lambda record: lazy_pinyin(record)[0][0])
    print(records)
    write_list_to_txt(records, name_path)

def get_songs_by_name(singer_name):
    pass

if __name__ == '__main__':
    # get_singer_names(page_path='https://www.1ting.com/group/group0_1.html', name_path='data/chinese_men.txt')
    get_singer_names(page_path='https://www.1ting.com/group/group0_2.html', name_path='data/chinese_women.txt')
    pass
