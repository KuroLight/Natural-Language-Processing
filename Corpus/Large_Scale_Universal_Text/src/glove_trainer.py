from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
from hanzi2pinyin import *

glove_input_file = '../data/rmrb2014_vectors_glove.txt'
word2vec_output_file = '../data/rmrb2014_vectors_glove2word2vec.txt'

(count, dimensions) = glove2word2vec(glove_input_file, word2vec_output_file)
print(count, '\n', dimensions)

# 加载模型
glove_model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
# 获得单词 # wei4 的词向量
zi_vec = glove_model['wei4']
print(zi_vec)
# 获得单词 # wei4 的最相似向量的词汇
print(glove_model.most_similar('wei4'))

words = get_list_from_txt_path('../data/rmrb2014_vocab_glove.txt')
with open('../data/rmrb2014_vocab_glove2word2vec.txt', 'wt') as f:
    f.write('<S>')
    f.write('\n')
    f.write('</S>')
    f.write('\n')
    f.write('<UNK>')
    f.write('\n')  # bilm-tf 要求vocab有这三个符号，并且在最前面
    for word in words:
        f.write(word.strip().split()[0])
        f.write('\n')
