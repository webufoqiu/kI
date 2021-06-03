# 改造后的切木头3
from collections import defaultdict
from functools import lru_cache

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
complete_price=defaultdict(int)

for i , p in enumerate(prices,1):complete_price[i]=p

print(complete_price)
solution={}



@lru_cache(maxsize=2**10)
def r(n):
    # if n in cache: return cache[n]
    
    condidates= [(complete_price[n],(n,0))] + [(r(i) + r(n-i),(i,n-i)) for i in range(1,n)] 
    opt_price,split= max(condidates)
    solution[n] =split 
   
    return opt_price

# 分析切木头的过程
def parse_solution(n,cut_solution):
    left,right= cut_solution[n]
    if left==0 or right==0: return [left,right]
    else:
        return parse_solution(left,cut_solution) +parse_solution(right,cut_solution)

if __name__ == '__main__':
    print(r(158))
    print(parse_solution(158,solution))
