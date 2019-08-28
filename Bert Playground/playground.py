from bert_serving.client import BertClient
from pprint import pprint


print('something!')
with BertClient() as bc: # port=5555, port_out=5556
    print('test')
    pprint(bc.status)
    pprint(bc.server_status)
    result = bc.encode(['First do it', 'then do it right', 'then do it better'])
    print(result)
    result = bc.encode(['First do it ||| then do it right'])
    print(result)
