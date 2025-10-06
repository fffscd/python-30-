for i in range(1, 10):
    for j in range(1, i + 1):  # 内层循环控制列数
        print(f"{j}×{i}={i*j}", end="\t")  # 使用制表符对齐输出
    print()  # 每行结束换行
