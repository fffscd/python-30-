from custom_excep import NegativeNumberError


def check_positive(num):
    if num < 0:
        raise NegativeNumberError(num)
    print("输入合法。")


try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)
