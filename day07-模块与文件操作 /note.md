


# 第7天学习笔记：模块与文件操作

## 一、模块（Module）

### 1. 模块概念
- 模块是一个包含变量、函数、类定义的 `.py` 文件。  
- 使用模块的目的是**代码复用**和**结构清晰**。  
- 每个模块都有一个内置变量 `__name__`，当模块被直接运行时，`__name__ == "__main__"`。

### 2. 模块导入方式
```python
import 模块名
from 模块名 import 函数名, 变量名
from 模块名 import *        # 不推荐，容易命名冲突
import 模块名 as 别名
```

### 3. 模块搜索路径
Python 按以下顺序查找模块：
1. 当前目录；
2. 环境变量 `PYTHONPATH`；
3. 系统默认路径。

可用以下命令查看：
```python
import sys
print(sys.path)
```

### 4. 自定义模块
创建 `my_utils.py`：
```python
def greet(name):
    return f"你好，{name}！"
```

主程序 `main.py`：
```python
import my_utils
print(my_utils.greet("小明"))
```

### 5. `if __name__ == "__main__"` 用法
在模块内测试自己的代码：
```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(3, 5))
```

---

## 二、文件操作（File I/O）

### 1. 打开文件
```python
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()
```

### 2. 推荐写法：with语句
`with` 会自动关闭文件，即使发生异常也安全：
```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 3. 写入文件
```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
```
- `"r"`：只读  
- `"w"`：写入（覆盖旧文件）  
- `"a"`：追加  
- `"b"`：二进制模式（如 `"rb"`, `"wb"`）

### 4. 文件常用方法
| 方法 | 作用 |
|------|------|
| `read(size)` | 读取指定字节数 |
| `readline()` | 读取一行 |
| `readlines()` | 读取所有行返回列表 |
| `write(str)` | 写入字符串 |
| `seek(offset)` | 移动文件指针 |
| `tell()` | 获取当前指针位置 |

---

## 三、实践：记事本小应用

### 目标
实现一个简单命令行记事本，支持添加与读取内容。

```python
# notepad.py
import os

FILENAME = "notes.txt"

def add_note():
    note = input("请输入要添加的笔记：")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("✅ 笔记已保存。")

def read_notes():
    if not os.path.exists(FILENAME):
        print("📄 还没有笔记。")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        print("📖 当前笔记内容：")
        print(f.read())

if __name__ == "__main__":
    while True:
        choice = input("选择操作：[1]添加笔记 [2]查看笔记 [0]退出：")
        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "0":
            break
        else:
            print("输入无效，请重试。")
```

---

## 四、总结

- 模块让代码可重用、易维护。
- 文件操作是程序与外部世界交互的主要方式。
- `with open()` 是文件操作最佳实践。
- 当模块独立运行与被导入时，用 `__name__` 判断执行逻辑。