# HELP

## hanzi to pinyin



## glove

- open folder /GloVe and file demo.sh
- delete download text8 part
- modify "CORPUS=rmrb2014_pinyin.txt"
- nohup bash demo.sh > glove.train.out 2>&1 &
- get embedding file "vectors.txt/bin" and "vocab.txt"
- use gensim to modify glove vectors into word2vec, modify "vocab.txt" as well (add \<S> \</S> \<UNK>)


## elmo

- modify "train_elmo.py" under /bin
    -  load_vocab的第二个参数应该改为None
    - n_gpus CUDA_VISIBLE_DEVICES 根据自己需求改
    - n_train_tokens 可改可不改，影响的是输出信息。要查看自己语料的行数，可以通过wc -l corpus.txt 查看。
    - 我没改这一条 (option的修改，将char_cnn部分都注释掉，其他根据自己需求修改
- modify “training.py" under /bilm
    - LanguageModel class
    - _build_word_embeddings
    - add pretrained glove into code
    - save final embedding
    - n_gpus 暂时发现不能是0，不然计算后n_tokens_per_batch==0会崩溃。尝试在GPU上面计算。
- train
    - nohup python -u bin/train_elmo.py --train_prefix='rmrb2014_pinyin.txt' --vocab_file rmrb2014_vocab_glove2word2vec.txt --save_dir . >bilm_out.txt 2>&1 &

## nohup
nohup command > myout.file 2>&1 &
nohup bash demo.sh > glove.train.out 2>&1 &

## references

 - http://www.linzehui.me/2018/08/05/%E7%A2%8E%E7%89%87%E7%9F%A5%E8%AF%86/%E5%A6%82%E4%BD%95%E8%AE%AD%E7%BB%83GloVe%E4%B8%AD%E6%96%87%E8%AF%8D%E5%90%91%E9%87%8F/
 - http://www.linzehui.me/2018/08/12/%E7%A2%8E%E7%89%87%E7%9F%A5%E8%AF%86/%E5%A6%82%E4%BD%95%E5%B0%86ELMo%E8%AF%8D%E5%90%91%E9%87%8F%E7%94%A8%E4%BA%8E%E4%B8%AD%E6%96%87/

