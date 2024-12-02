a: int = 1
b: float
c: str
d: bool

e: list[int] = [1, 2]

# keyの型とvalueの型を指定する
# 辞書型のキーが文字列で、値が真偽値の場合
f: dict[str, bool] = {"Flag": True}

from typing import Literal

# リテラル型
# 指定した値しか入らない
# Javaでいうところのenum
g: Literal["OK", "NG"] = "OK"


def sample(x: str) -> bool:
    return True
