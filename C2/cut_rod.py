from collections import defaultdict

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
complete_price=defaultdict(int)
# print(complete_price)
# complete_price= {i: p for i , p in enumerate(prices,1)}
for i , p in enumerate(prices,1):complete_price[i]=p
# print([complete_price[9]])
# print([complete_price[12]])
print(complete_price)
def r(n):
    condidates =[complete_price[n]]
    # 若n=8,候选价格condidates列表中，存[20]
    for i in range(1,n):
        left = i
        right= n-i
        # total_r =complete_price[left]+complete_price[right]
        total_r = r(left)+r(right)
        # 循环拆分8米的木头，1 7 ,2 6 ,3 5,4,4 ,5,3 6,2 7,1 
        condidates.append(total_r)
        #循环把拆分的结果压入候选列表condidates中
    return max(condidates)
    # 返回候选列表中最大值

if __name__ == '__main__':
    print(r(8))
