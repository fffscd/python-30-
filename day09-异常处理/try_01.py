try:
    x = int(input("输入一个整数: "))
    result = 10 / x
except ValueError:
    print("输入的不是整数！")
except ZeroDivisionError:
    print("除数不能为0！")
else:
    print("计算结果:", result)
finally:
    print("程序执行结束。")