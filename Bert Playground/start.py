from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer

model_dir = '../../bert_model/chinese_wwm_ext_L-12_H-768_A-12'
args = get_args_parser().parse_args(['-model_dir', model_dir,
                                     '-port', '5555',
                                     '-port_out', '5556',
                                     '-max_seq_len', 'NONE',
                                     '-mask_cls_sep',
                                     '-cpu'])
server = BertServer(args)
server.start()


# BertServer.shutdown(port=5555)
# server.shutdown()