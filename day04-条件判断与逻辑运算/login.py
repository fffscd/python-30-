
# 假设数据库中已有的用户名和密码
username_db = "admin"
password_db = "123456"

# 最大尝试次数
max_attempts = 3
attempts = 0
is_locked = False

while attempts < max_attempts and not is_locked:
    # 用户输入
    username_input = input("请输入用户名: ")
    password_input = input("请输入密码: ")
    # 判断逻辑
    if username_input == username_db and password_input == password_db:
        print("✅ 登录成功！欢迎回来。")
    else:
        if username_input == username_db and password_input != password_db:
            print("❌ 密码错误，请重试。")
        elif username_input != username_db and password_input == password_db:
            print("❌ 用户名不存在。")
        else:
            print("⚠️ 用户名和密码都不正确。")
        attempts += 1
        if (attempts >= max_attempts):
            is_locked = True;


# 如果循环正常结束但没成功登录
if is_locked:
    print("系统提示：为安全起见，您的账号暂时锁定。")
