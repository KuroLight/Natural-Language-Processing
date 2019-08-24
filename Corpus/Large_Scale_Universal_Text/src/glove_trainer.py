from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

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