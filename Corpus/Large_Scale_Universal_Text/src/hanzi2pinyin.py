from pypinyin import pinyin, lazy_pinyin, Style
import argparse
from tqdm import tqdm

# py = pinyin('中心', style=Style.TONE3, heteronym=True)
# print(py)

def get_list_from_txt_path(txt_path):
    with open(txt_path, 'rt', encoding='utf8', newline='\n') as f:
        return f.readlines()

def write_list_to_txt_path(text_list, txt_path):
    with open(txt_path, 'wt', encoding='utf8', newline='\n') as f:
        for text in text_list:
            f.write(text)
            f.write('\n')

def convert(input_dir, output_dir):
    hanzi_list = get_list_from_txt_path(input_dir)
    pinyin_list = []
    for juzi in tqdm(hanzi_list):
        pinyin_juzi = []
        for ci in juzi.split():
            
            tmp = ' '.join(zi[0] for zi in pinyin(ci, style=Style.TONE3, heteronym=False))
            # print(tmp)
            pinyin_juzi.append(tmp)


        pinyin_list.append(' '.join(pinyin_juzi))

    write_list_to_txt_path(pinyin_list, output_dir)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='convert hanzi to pinyin...')
    parser.add_argument('-I',"--input_dir", help="input dir of hanzi text", type=str)
    parser.add_argument('-O','--output_dir', help='output dir of pinyin strings', type=str)
    args = parser.parse_args()
    convert(args.input_dir, args.output_dir)