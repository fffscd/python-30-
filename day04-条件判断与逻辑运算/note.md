# 登录验证脚本
🧠 条件判断笔记（Python）

一、基本结构

if 条件表达式:
    执行语句1
elif 其他条件:
    执行语句2
else:
    执行语句3

执行逻辑：
	•	先判断第一个条件是否为 True；
	•	若为真，执行对应代码块；
	•	否则依次判断后续 elif；
	•	若所有条件都为假，则执行 else。

⸻

二、常见逻辑运算符

运算符	含义	示例	结果
and	逻辑与（两者都真）	a > 0 and b > 0	True 当 a、b 都大于 0
or	逻辑或（任意为真）	a > 0 or b > 0	True 当任一大于 0
not	逻辑非（取反）	not a > 0	True 当 a ≤ 0


⸻

三、条件表达式（又叫“三元表达式”）

简写 if-else 的形式：

result = "合格" if score >= 60 else "不合格"


⸻

四、嵌套判断

可以在 if 内部再写 if，用于更复杂的逻辑。

if username == "admin":
    if password == "123456":
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名不存在")


⸻

五、布尔值与隐式真值判断

Python 中以下值会被视为 False：
	•	0、0.0
	•	""（空字符串）
	•	[]、()、{}（空容器）
	•	None
	•	False

示例：

if not username:
    print("用户名不能为空")


⸻

六、综合示例

age = int(input("请输入年龄: "))

if age < 0:
    print("输入无效")
elif age < 18:
    print("未成年")
elif 18 <= age < 60:
    print("成年人")
else:
    print("老年人")


⸻

七、思维要点
	1.	条件越复杂越要分层写清楚，避免一行塞太多逻辑。
	2.	逻辑运算优先级： not > and > or。
	3.	短路机制：
	•	and 遇到第一个 False 就停止；
	•	or 遇到第一个 True 就停止。

