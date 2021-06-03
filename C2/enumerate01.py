seq = ['one', 'two', 'three']
print(enumerate(seq))
for i, element in enumerate(seq):
    print(i, element)

# enumerate(sequence,[start=0]) 
# 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。
# sequence -- 一个序列、迭代器或其他支持迭代对象。
# start -- 下标起始位置。

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
a=list(enumerate(seasons))
b=list(enumerate(seasons, start=1))  
print(a)
print(b)
