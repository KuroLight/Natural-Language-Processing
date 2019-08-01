import pkuseg


def main():
    seg = pkuseg.pkuseg()  # 以默认配置加载模型
    text = seg.cut('打开和平经营')  # 进行分词
    print(text)


if __name__ == '__main__':
    main()
