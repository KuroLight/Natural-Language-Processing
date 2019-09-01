#!/usr/bin/env bash
bert-serving-start \
    -model_dir '../../bert_model/chinese_wwm_ext_L-12_H-768_A-12' \
    -num_worker 4 \
    -pooling_strategy NONE \
    -show_tokens_to_client