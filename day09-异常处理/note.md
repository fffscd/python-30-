# 第9天：异常处理（Exception Handling）

## 一、学习目标
- 理解异常的概念和类型  
- 掌握 `try`、`except`、`else`、`finally` 的使用方式  
- 能够自定义异常类  
- 熟悉文件读取异常的处理

---

## 二、异常基础概念
异常（Exception）是程序运行过程中出现的错误事件，会中断正常的执行流程。  

常见异常：
- `ValueError`：数值类型正确但值不合适  
- `TypeError`：操作或函数应用于错误类型的对象  
- `FileNotFoundError`：文件不存在  
- `ZeroDivisionError`：除数为零  
- `IndexError` / `KeyError`：索引或键不存在  

---

## 三、try-except-finally 结构
```python
try:
    # 可能出错的代码
except ExceptionType1:
    # 处理特定异常
except ExceptionType2 as e:
    # 捕获异常对象
else:
    # 未发生异常时执行
finally:
    # 无论是否出错都会执行
```

示例：
```python
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
```

---

## 四、自定义异常类
```python
class NegativeNumberError(Exception):
    """自定义异常：输入负数时触发"""
    def __init__(self, value):
        self.value = value
        super().__init__(f"不允许输入负数：{value}")
```

使用示例：
```python
def check_positive(num):
    if num < 0:
        raise NegativeNumberError(num)
    print("输入合法。")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)
```

---

## 五、文件读取异常处理
```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
except PermissionError:
    print("没有权限访问该文件。")
finally:
    print("文件读取操作完成。")
```

---

## 六、练习任务
1. 读取用户输入的文件名，尝试打开并读取内容：  
   - 若文件不存在 → 输出“文件不存在”  
   - 若文件为空 → 抛出自定义异常 `EmptyFileError` 并捕获处理  
   - 否则打印文件内容  

2. 编写单元测试验证上述功能。  
