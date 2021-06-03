prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33]

from collections import defaultdict
from functools import lru_cache  # least recent used 最近最少使用

complete_price = {i + 1: p for i, p, in enumerate(prices)}

complete_price = defaultdict(int)   # 不存在的时候赋值==0

for i , p in enumerate(prices):complete_price[i+1] = p

solution = {}

cache = {}   # 解决重复问题

@lru_cache(maxsize=2**10)   # 用于优化，解决程序运算慢的问题
def r(n):
    # if n in cache: return cache[n]   # 和cache[n] = optimal_price使用修饰器替代

    # 时间复杂度：2*（n-1）*2*（n-2) * ... = 2^n*n!

    # candiates = [complete_price[n]]
    #
    # for i in range(1, n):
    #     left = i
    #     right = n- i
    #
    #     total_r = complete_price[left], + complete_price[right]
    #     total_r = r(left)  +  r(right)
    #     candiates.append(total_r)
    #
    # return max(candiates)

    # return max([complete_price[n]] + [r(i) + r(n-i) for i in range(1,n)])

# 下面这种写法才是通用的写法
    candidates = [(complete_price[n], (n, 0))] + [(r(i) + r(n-i), (i, n-i)) for i in range(1,n)]
    optimal_price , split = max(candidates)

    solution[n] = split
    # cache[n] = optimal_price
    return optimal_price

def parse_solution(n, cut_solution):   # 把每一步分割出来
    left, right = cut_solution[n]
    if left == 0 or right == 0: return [left+ right, 0]
    else:
        return parse_solution(left, cut_solution) + parse_solution(right , cut_solution)

if __name__ == '__main__':
    # print(r(8))
    # print((solution[8]))
    print(r(33))
    print(parse_solution(33, solution))

# print(complete_price[9])
# print(complete_price[30])