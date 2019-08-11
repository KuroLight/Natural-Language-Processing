def write_list_to_txt(l, txt_path):
    with open(txt_path, 'wt', encoding='utf8') as f:
        for line in l:
            f.write(line + '\n')


def read_list_from_txt(txt_path):
    with open(txt_path, 'rt', encoding='utf-8') as f:
        return f.readlines()
