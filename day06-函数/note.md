# 1) 直接答案（你需要掌握的要点）

* 用 `def` 定义函数；用函数名加括号调用，如 `foo()`。
* 函数返回值用 `return`；不写 `return` 默认返回 `None`。
* **作用域遵循 LEGB**：Local → Enclosing → Global → Builtins。
* 修改外层变量：同层赋值会创建**局部**；要改全局用 `global`；要改闭包外层但非全局用 `nonlocal`。
* **避免可变对象做默认参数**（大坑），用 `None` 作为占位更安全。

---

# 2) 分步骤说明与示例

## 定义与调用

```python
def add(a, b):
    """返回两个数的和"""
    return a + b

res = add(3, 5)   # 调用
print(res)        # 8
```

## 返回多个值（其实是打包成 tuple）

```python
def stat(xs):
    return min(xs), max(xs), sum(xs)/len(xs)

lo, hi, avg = stat([3, 9, 6])  # 多重赋值解包
```

## 参数形式速览（常用的记住 4 个就行）

```python
def demo(pos1, pos2, /, kw_only=0, *args, scale=1, **kwargs):
    pass
```

* 位置参数（positional）`pos1`、`pos2`
* 仅限位置参数 `/`（了解即可）
* 可变参数 `*args`、关键字参数 `**kwargs`
* 关键字参数及默认值 `scale=1`、`kw_only=0`

## 作用域与变量查找（LEGB）

| 级别            | 含义        | 何时出现      | 示例              |
| ------------- | --------- | --------- | --------------- |
| L (Local)     | 当前函数内     | 函数体内定义的名字 | `x = 1`（在函数里）   |
| E (Enclosing) | 外层嵌套函数的局部 | 闭包情景      | 外函数里的 `x` 被内函数用 |
| G (Global)    | 模块级别      | 文件最外层定义   | `PI = 3.14`     |
| B (Builtins)  | 内建命名空间    | Python 内置 | `len`, `range`  |

**示例：局部遮蔽（shadowing）与修改外层变量**

```python
x = 10  # 全局

def f():
    x = 20       # 局部，遮蔽了全局
    return x

def g():
    global x
    x = 30       # 修改全局 x
    return x

def outer():
    y = 1
    def inner():
        nonlocal y
        y += 1   # 修改外层（但非全局）的 y
        return y
    inner(); inner()
    return y  # 3
```

## 默认参数的大坑与规避

```python
# 坑：默认参数只在函数定义时创建一次
def append_bad(item, bucket=[]):
    bucket.append(item)
    return bucket

append_bad(1)  # [1]
append_bad(2)  # [1, 2] ← 意外复用

# 正确写法
def append_ok(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

## 函数是“一等公民”

```python
def square(x): return x*x
def apply(f, x): return f(x)

apply(square, 3)  # 9  —— 函数可以作为参数/返回值
```

---

# 3) 其他视角与可选方案

* **lambda 简写**：适合很短的小函数，别滥用。

  ```python
  nums = [3, 1, 4]
  nums.sort(key=lambda x: -x)  # 按倒序值排序
  ```
* **文档字符串与类型注解**：让代码更可读、更可检查。

  ```python
  def add(a: int, b: int) -> int:
      """返回 a+b"""
      return a + b
  ```
* **闭包 vs. 类**：需要携带状态且有多种操作时，类更清晰；仅封装小状态与函数逻辑时，闭包足够优雅。

---

# 4) 立刻可执行的练习与行动清单

### 必做题（10 分钟）

1. 写 `power(base, exp=2)`，返回 `base**exp`，并给出 3 个调用示例（含默认、关键字、位置）。
2. 写 `make_counter(start=0)`，返回一个 `next()` 函数；每次调用自增并返回当前值。要求用 `nonlocal`。
3. 用**正确方式**实现 `accumulate(items, init=None)`：把 `items` 逐个累加到 list 里返回，注意避免默认参数坑。

### 进阶挑战（可选）

* 写一个带缓存的函数 `fib(n)`，用闭包保存命中表 `cache`（或用 `functools.lru_cache` 对比）。
* 实现 `compose(f, g)` 返回新函数 `h(x)=f(g(x))`，体会函数是一等公民。
 
