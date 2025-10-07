import os
from pathlib import Path

FILENAME = Path(__file__).resolve().parent / "notes.txt"


def add_note():
    note = input("请输入你的笔记:")
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("笔记已经保存")


def read_notes():
    if not FILENAME.exists:
        print("📄 还没有笔记。")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        print("当前笔记内容：")
        print(f.read)


if __name__ == "__main__":
    while True:
        choice = input("选择操作：[1]添加笔记 [2]查看笔记 [0]退出：")
        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "0":
            break
        else:
            print("输入无效，请重试。")

