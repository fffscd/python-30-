class NegativeNumberError(Exception):
    def __init__(self, value):
        self.vale = value
        super().__init__(f"不允许输入负数：{value}")