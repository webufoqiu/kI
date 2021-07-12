from sklearn.model_selection import train_test_split

import numpy as np

sample_data =np.random.random(size=(100,50))
print(sample_data)
train,test =train_test_split(sample_data,train_size=0.8)

print(test)