import unittest
from io import StringIO
from contextlib import redirect_stdout
from CreditAccount import CreditAccount


class TestCreditAccount(unittest.TestCase):
    def setUp(self):
        # 每个测试前都会执行，用于初始化环境
        self.account = CreditAccount(owner="Alice", balance=1000, limit=800)

    def test_initialization(self):
        self.assertEqual(self.account._owner, "Alice")
        self.assertEqual(self.account.get_balance(), 1000)
        self.assertAlmostEqual(self.account._limit, 800)


if __name__ == "__main__":
    unittest.main()
