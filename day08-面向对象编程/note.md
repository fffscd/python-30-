

# Day 08 - 面向对象编程（Object-Oriented Programming, OOP）

## 学习目标
- 理解面向对象编程的三大核心概念：**封装（Encapsulation）**、**继承（Inheritance）**、**多态（Polymorphism）**
- 学会定义类与对象
- 掌握构造函数 `__init__`、实例方法、类方法与静态方法
- 能够通过继承扩展功能，理解 `super()` 的作用
- 设计一个完整的“银行账户”类并实现子类继承

---

## 一、核心概念
### 1. 类与对象
- **类（Class）**：对象的蓝图或模板。
- **对象（Object）**：类的实例，拥有属性（数据）和方法（行为）。

### 2. 封装（Encapsulation）
- 通过属性和方法隐藏内部细节，只暴露必要的接口。
- 使用 `_` 或 `__` 表示受保护或私有属性。

### 3. 继承（Inheritance）
- 子类可以继承父类的属性与方法。
- 使用 `super()` 调用父类构造或方法。

### 4. 多态（Polymorphism）
- 不同子类可重写父类方法，实现相同方法名下的不同表现。

---

## 二、示例实践：银行账户系统

### 1. 基类：BankAccount
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self._owner} 存入 {amount} 元，当前余额：{self._balance}")
        else:
            print("存款金额必须为正数！")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{self._owner} 取出 {amount} 元，当前余额：{self._balance}")
        else:
            print("取款失败，余额不足或输入错误！")

    def get_balance(self):
        return self._balance
```

### 2. 子类：储蓄账户（SavingsAccount）
```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"{self._owner} 获得利息 {interest:.2f} 元，当前余额：{self._balance:.2f}")
```

### 3. 子类：信用账户（CreditAccount）
```python
class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, limit=1000):
        super().__init__(owner, balance)
        self._limit = limit

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self._limit:
            self._balance -= amount
            print(f"{self._owner} 使用信用取出 {amount} 元，当前余额：{self._balance}")
        else:
            print("超过信用额度，取款失败！")
```

---

## 三、扩展练习
1. 实现账户转账功能 `transfer(self, target_account, amount)`
2. 添加交易记录列表，保存每次操作的时间与金额
3. 为账户类添加字符串表示方法 `__str__`
4. 使用 `@property` 将余额作为只读属性

---

## 四、思考与总结
- 为什么说“类是抽象，对象是具体”？
- 封装如何提升安全性和可维护性？
- 在何种场景下使用继承而不是组合（composition）？
- 多态如何帮助我们实现灵活扩展？

---

## 五、课后练习
- 设计一个 `Student` 类，包含姓名、学号、成绩等属性。
- 编写一个 `SchoolAccount` 管理多个学生账户的类。
- 实现“添加学生”“计算平均成绩”等方法。