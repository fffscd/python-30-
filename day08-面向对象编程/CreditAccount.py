from BankAccount import BankAccount

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
