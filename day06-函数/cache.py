from functools import cache
from typing import Dict

def make_fib():
    cache:  Dict[int, int] = {0: 0, 1: 1}  # 命中表
    def fib(n: int) -> int:
        if not isinstance(n, int):
            raise TypeError("n 必须是 int")
        if n < 0:
            raise ValueError("n 不能为负数")

        # 命中则直接返回
        if n in cache:
            return cache[n]

        # 递归 + 备忘录
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib

fib = make_fib()

# 用法示例
print(fib(10))   # 55
print(fib(100))  # 354224848179261915075