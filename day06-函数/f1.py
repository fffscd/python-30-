def add(a, b):
    """返回两个数的和"""
    return a + b

res = add(3, 5)   # 调用
print(res)        # 8

def stat(xs):
    return min(xs), max(xs), sum(xs)/len(xs)

lo, hi, avg = stat([3, 9, 6])  # 多重赋值解包
print(f"{lo},{hi},{avg}")
