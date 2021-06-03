# 改造后的切木头2
from collections import defaultdict

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
complete_price=defaultdict(int)

for i , p in enumerate(prices,1):complete_price[i]=p

print(complete_price)
solution={}

cache={}
def r(n):
    if n in cache: return cache[n]
    
    condidates= [(complete_price[n],(n,0))] + [(r(i) + r(n-i),(i,n-i)) for i in range(1,n)] 
    opt_price,split= max(condidates)
    solution[n] =split 
    cache[n]= opt_price

    return opt_price
if __name__ == '__main__':
    print(r(33))
    print(solution[33])
