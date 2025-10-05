import operator


print("计算器测试")
# 输入两个数字
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符：")
num2 = float(input("请输入第二个数字："))

if (operator == "+"):
    result = num1 + num2
if (operator == "-"):
    result = num1 - num2
if (operator == "/"):
    if (num2 == 0):
        result = "非法操作"
    else:
        result = num1 / num2
if (operator == "*"):
    result = num1 * num2

print(result)


