# 改造后的切木头
from collections import defaultdict

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]
complete_price=defaultdict(int)
# print(complete_price)
# complete_price= {i: p for i , p in enumerate(prices,1)}
for i , p in enumerate(prices,1):complete_price[i]=p
# print([complete_price[9]])
# print([complete_price[12]])
print(complete_price)
solution={}

cache={}
def r(n):
    if n in cache: return cache[n]
    # return (max([complete_price[n]]+[r(i)+r(n-i) for i in range(1,n)] ))
    condidates= [(complete_price[n],(n,0))] + [(r(i) + r(n-i),(i,n-i)) for i in range(1,n)] 
    opt_price,split= max(condidates)
    solution[n] =split 
    cache[n]= opt_price
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
