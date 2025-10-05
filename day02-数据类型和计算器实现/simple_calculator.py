# simple_calculator.py

print("=== 简单计算器 ===")

# 输入两个数字
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符 (+, -, *, /)：")
num2 = float(input("请输入第二个数字："))

# 根据运算符执行计算
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "错误：除数不能为0"
else:
    result = "错误：无效的运算符"

print(f"结果：{result}")