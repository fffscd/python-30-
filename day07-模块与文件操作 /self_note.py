# notepad.py
from pathlib import Path

NOTES_PATH = Path(__file__).resolve().parent / "notes.txt"

def add_note():
    note = input("请输入要添加的笔记：")
    with open(NOTES_PATH, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("✅ 笔记已保存。")

def read_notes():
    if not NOTES_PATH.exists():
        print("📄 还没有笔记。")
        return
    with open(NOTES_PATH, "r", encoding="utf-8") as f:
        print("📖 当前笔记内容：")
        print(f.read())

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
