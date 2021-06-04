import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

dataset = load_boston()
# print(dataset)

data =dataset['data']
target= dataset['target']
columns= dataset['feature_names']

mydataframe=pd.DataFrame(data)
mydataframe.columns=columns
mydataframe['price']=target
# print(mydataframe)
# print(mydataframe.shape)
# print(mydataframe.corr())

# print(mydataframe.corr())
# sns.heatmap(mydataframe.corr())
# plt.show()

rm=mydataframe['RM']
lstat =mydataframe['LSTAT']
# print(rm)

def model(x,w,b):
    return np.dot(x, w.T) + b
def loss(yhat, y):
    return np.mean(0.5* (yhat - y) ** 2)

def partial_w(x, y, yhat):
    return np.array([np.mean((yhat - y) * x[0]), np.mean((yhat - y) * x[1])])


def partial_b(x, y, yhat):
    return np.mean((yhat - y))


w = np.random.random_sample((1, 2)) # w normal 一行两列w1,w2
b = np.random.random() 
 
learning_rate= 1e-5

for i in range(50):
    for batch in range(len(rm)):

        index = random.choice(range(len(rm)))
        
        rm_x, lstat_x = rm[index], lstat[index]
        
        x = np.array([rm_x, lstat_x])
        
        y = target[index]

        yhat=model(x,w,b)

        loss_v= loss(yhat,y)
        
        w = w + -1 * partial_w(x, y, yhat) * learning_rate
        b = b + -1 * partial_b(x, y, yhat) * learning_rate
        
        print(loss_v)
 
