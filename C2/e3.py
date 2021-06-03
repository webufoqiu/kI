import random
# 梯度下降演示
# 有loss函数,找到一个k值，是的loss函数值最小
# alpha稳定器
# 偏导大于0说明递增，偏导小于0说明递减，让k逆向递进

def loss(k):
    return 3*k**2 +7*k-10

def partial(k):
    return 6*k+7

k=random.randint(-10,10)
alpha =1e-3

for i in range(10000):
    k=k+(-1)*partial(k)*alpha
    print(k,loss(k))


