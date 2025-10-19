from __future__ import annotations


class EmptyFileError(Exception):
    """自定义异常：当文件存在但内容为空时抛出。"""
    pass


def read_file_content(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if content == "":
        raise EmptyFileError("文件为空")
    return content


def cli() -> None:
    filename = input("请输入文件名: ").strip()
    try:
        content = read_file_content(filename)
        print(content, end="" if content.endswith("\n") else "\n")
    except FileNotFoundError:
        print("文件不存在")
    except PermissionError:
        print("没有权限访问该文件")
    except EmptyFileError:
        print("文件为空")


if __name__ == "__main__":
    cli()