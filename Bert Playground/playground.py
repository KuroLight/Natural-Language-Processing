from bert_serving.client import BertClient
from pprint import pprint
from sklearn.metrics.pairwise import cosine_similarity

# print('something!')
with BertClient() as bc:  # port=5555, port_out=5556
    # print('test')
    # pprint(bc.status)
    # pprint(bc.server_status)

    # result = bc.encode(['First do it', 'then do it right', 'then do it better'])
    # print(result)
    # result = bc.encode(['First do it ||| then do it right'])
    # print(result)

    result = bc.encode(['猫吃什么', '狗吃什么'])
    # print(result.shape)
    pprint(result[0])
    sim = cosine_similarity(result[0].reshape(1, -1), result[1].reshape(1, -1))
    print(sim)

    result = bc.encode(['猫吃什么', '猫做什么'], show_tokens=True)
    # print(result.shape)
    # sim = cosine_similarity(result[0].reshape(1, -1), result[1].reshape(1, -1))
    # print(sim)
    print(result)

    result = bc.encode(['猫吃什么 ||| 猫做什么'], show_tokens=True)
    print(result)