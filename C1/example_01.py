"""
LSTM,Transfer去做
GPT-2

"""
import random
grammar="""
句子= 主 谓 宾 
谓= 吃| 喝| 玩 
宾= 足球| 桃子 
主= 你| 我 | 他 
"""

# def gen_verb():
#     return random.choice(' 吃| 喝| 玩'.split('|'))

# def 生成宾语():
#     return random.choice(' 足球 | 桃子'.split('|'))

# print(gen_verb()+生成宾语())
gram_gen =dict()

for line in grammar.split('\n'):
    if not line.strip(): continue
    # print(line)
    
    smst,expr=line.split('=')
    expressions= expr.split('|')
    # print("expreesions:",expressions)
    gram_gen[smst]= [e.strip() for e in expressions]

print(gram_gen)

def gen_sen(gram,target="句子"):
    if target not in gram: return target
    exp = random.choice(gram[target])
    # print(exp)
    return ''.join([gen_sen(gram,e)  for e in exp.split()])

print(gen_sen(gram_gen))
