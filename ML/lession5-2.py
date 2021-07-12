from numpy.core.fromnumeric import size
from icecream import ic
import numpy as np

def one_hot(elements):
    pure = list(set(elements))
    vectiors=[]
    # indices=[pure.index(e) for e in elements]
    for e in elements:
        vec =[0]*len(pure)
        vec[pure.index(e)]=1
        vectiors.append(vec)
    return vectiors

ic(one_hot(['北京','上海','广州','重庆']))

def normalize(x):
    return (x-np.min(x))/(np.max(x)-np.min(x))

def standarlize(x):
    return (x-np.mean(x))/(np.std(x))


x= [12324,45243,32343] #3维向量x
y= [0,0,1,0,0] #分类，5分类

x= normalize(x)
# x= standarlize(x)
x= np.array(x)
weights=np.random.random(size=(3,5))  

yhat= np.dot(x,weights)
ic(yhat)
#算子,logits  

#例如 ，将x向量（10维）辩证logits算子（3维），再把logits算子,编程概率分布
#通过softmax把算子变成概率分布

def softmax(x):
    # x-= np.max(x)
    return np.exp(x)/np.sum(np.exp(x))

ic(softmax(yhat))

#逻辑回归的LOSS函数

def cross_entropy(yhat,y):
    return -np.sum(y_i * np.log(yhat_i) for y_i,yhat_i in zip(y,yhat))


ic(cross_entropy(softmax(yhat),y))