class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("存入金额必须为正数")
            return
        self._balance += amount
        print(f"{self._owner} 存入 {amount} 元，当前余额：{self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"{self._owner} 取出 {amount} 元，当前余额：{self._balance}")
        else:
            print("取款失败，余额不足或输入错误！")

    def get_balance(self):
        return self._balance


    
