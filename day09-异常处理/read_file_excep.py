from sys import exception

try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
except PermissionError:
    print("文件无权限。")
finally:
    print("文件读取操作完成。")
     