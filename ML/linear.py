from sklearn.datasets import load_boston

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dataset = load_boston()
data = dataset['data']
target = dataset['target']
columns = dataset['feature_names']

dataframe = pd.DataFrame(data)
dataframe.columns = columns
dataframe['price'] = target

print(dataframe.head())
print(dataframe.corr())
# correlation=>1  ，相关系数，如果一个值的增大，会引起另一个值一定增大，而且是定比例增大
# correlation=>0，两者之间没有任何关系
# correlation=>-1，相关系数，如果一个值的增大，会引起另一个值一定减小，而且是定比例减小

sns.heatmap(dataframe.corr())
plt.show()
# 看图，RM（平均卧室个数）和price正相关
# 看图，LSTAT（低收入人群比例）和price负相关

rm = dataframe['RM']
lstat = dataframe['LSTAT']
target= dataframe['price']
# 这两个数据对price影响最明显，用这两个数据来构造模型
# 假设是线性关系  Assume this relationship is linear 
# def model(rm, lstat,w1,w2, b):
#     return w1*rm + w2*lstat+b

#x w b都是向量，构造模型如下 
# x =>(rm ,lstat)
# w =>(w1,w2)
# np.dot()点积，w1*x1+w2*x2+b 
# 用向量模式，vectorized model,如下：

# 比如
# x=[1,2,3]
# w=[3,4,5]
# 矩阵点乘（点积）规则，n*m 点积  m* k

def model(x, w, b):
    return np.dot(x, w.T) + b


# 有了x,要预测w和b

def loss(yhat,y):
    return np.mean((yhat-y)**2)

def partial_w(x,w,b,y,yhat):
    return 2*np.mean((yhat-y)*x[0],(yhat-y)*x[1])

def partial_b(x,w,b,y,yhat):
    2*np.mean()