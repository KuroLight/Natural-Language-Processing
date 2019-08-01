"""
分词
pinyin 变化距离
"""

import pkuseg  # https://github.com/lancopku/PKUSeg-python
import dimsim  # https://github.com/System-T/DimSim


def main():
    seg = pkuseg.pkuseg()  # 以默认配置加载模型
    text = seg.cut('打开荣耀侵权')  # 进行分词
    print(text)

    # seg = pkuseg.pkuseg(model_name='medicine')  # 程序会自动下载所对应的细领域模型
    # text = seg.cut('我爱北京天安门')  # 进行分词
    # print(text)
    #
    # seg = pkuseg.pkuseg(postag=True)  # 开启词性标注功能
    # text = seg.cut('我爱北京天安门')  # 进行分词和词性标注
    # print(text)

    print(dimsim.get_distance("荣耀侵权", "荣耀亲选"))
    print(dimsim.get_distance("荣耀", "荣耀"))
    print(dimsim.get_distance("侵权", "亲选"))
    print(dimsim.get_distance("侵", "亲"))
    print(dimsim.get_distance("权", "选"))

    print(dimsim.get_distance('垃圾', '辣鸡'))
    print(dimsim.get_distance('垃', '辣'))
    print(dimsim.get_distance('圾', '鸡'))

    print(dimsim.get_distance('经营', '精英'))
    print(dimsim.get_distance('经', '精'))
    print(dimsim.get_distance('营', '英'))


if __name__ == '__main__':
    main()
