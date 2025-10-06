# 斐波那契数列
n = 10  # 输出前10个数
a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b  # 更新两个变量
    count += 1
