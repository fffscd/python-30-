# 子类：储蓄账户（SavingsAccount）
from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"{self._owner} 获得利息 {interest:.2f} 元，当前余额：{self._balance:.2f}")
