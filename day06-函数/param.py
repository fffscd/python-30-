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


#print(x);
#g();
#print(x);

print("------")
print(f());
print(x);