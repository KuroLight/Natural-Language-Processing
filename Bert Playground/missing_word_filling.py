"""
https://stackoverflow.com/questions/54978443/predicting-missing-words-in-a-sentence-natural-language-processing-model
"""

import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM
import numpy as np

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging


# logging.basicConfig(level=logging.INFO)

def get_top_n_idx(arr, n):
    """
    https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
    :param arr:
    :param n:
    :return:
    """
    # return np.argpartition(arr, -n)[-n:]
    arr = np.asarray(arr)
    return arr.argsort()[-n:][::-1]


pretrained_model_path = '../../bert_model/pytorch-transformers/chinese_wwm_ext_pytorch'
# Load pre-trained model tokenizer (vocabulary)
tokenizer = BertTokenizer.from_pretrained(
    pretrained_model_name_or_path=pretrained_model_path)  # bert-base-uncased  bert-base-chinese

# text = '[CLS] I want to [MASK] the car because it is cheap . [SEP]'
# text = '[CLS] 给 我 播 放 一 首 [MASK] [MASK] [MASK] 的 告 白 气 球 [SEP]'
texts = [
    '[CLS] 给 我 播 放 一 首 周 杰 [MASK] 的 告 白 气 球 [SEP]',
    '[CLS] 给 我 播 放 一 首 [MASK] 杰 伦 的 告 白 气 球 [SEP]',
    '[CLS] 给 我 播 放 一 首 周 [MASK] 伦 的 告 白 气 球 [SEP]'
]


def guess_single_word(text):
    tokenized_text = tokenizer.tokenize(text)
    print(tokenized_text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    print(indexed_tokens)
    masked_index = tokenized_text.index('[MASK]')
    print(masked_index)

    # Create the segments tensors.
    segments_ids = [0] * len(tokenized_text)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    print(tokens_tensor, segments_tensors)

    # Load pre-trained model (weights)
    model = BertForMaskedLM.from_pretrained(pretrained_model_name_or_path=pretrained_model_path)
    model.eval()

    # Predict all tokens
    with torch.no_grad():
        predictions = model(tokens_tensor, segments_tensors)

    print(predictions.shape)
    pre_idxs = get_top_n_idx(predictions[0, masked_index], 5)
    print(pre_idxs)
    print(tokenizer.convert_ids_to_tokens(np.asarray(pre_idxs)))

    predicted_index = torch.argmax(predictions[0, masked_index]).item()
    print(predicted_index)
    predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]

    print(predicted_token)


for t in texts:
    guess_single_word(text=t)
