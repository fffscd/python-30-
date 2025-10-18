import unittest
from io import StringIO
from contextlib import redirect_stdout
from SavingsAccount import SavingsAccount  

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        # 每个测试前都会执行，用于初始化环境
        self.account = SavingsAccount(owner="Alice", balance=1000, interest_rate=0.05)

    def test_initialization(self):
        self.assertEqual(self.account._owner, "Alice")
        self.assertEqual(self.account.get_balance(), 1000)
        self.assertAlmostEqual(self.account._interest_rate, 0.05)

    def test_deposit_valid(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_deposit_invalid(self):
        # 存入负数，余额不应改变
        with redirect_stdout(StringIO()) as f:
            self.account.deposit(-100)
        output = f.getvalue()
        self.assertIn("必须为正数", output)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_withdraw_valid(self):
        self.account.withdraw(400)
        self.assertEqual(self.account.get_balance(), 600)

    def test_withdraw_invalid(self):
        with redirect_stdout(StringIO()) as f:
            self.account.withdraw(2000)
        output = f.getvalue()
        self.assertIn("取款失败", output)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_add_interest(self):
        self.account.add_interest()
        # 1000 * 0.05 = 50
        self.assertAlmostEqual(self.account.get_balance(), 1050)

if __name__ == "__main__":
    unittest.main()