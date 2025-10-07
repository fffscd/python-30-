from pathlib import Path

data_path = Path(__file__).resolve().parent / "data.txt"
with data_path.open("r", encoding="utf-8") as f:  # 使用脚本所在目录中的数据文件
    content = f.read()
print(content)


with open(data_path, "a", encoding="utf-8") as f:
    f.write("Hello, Python!\n")