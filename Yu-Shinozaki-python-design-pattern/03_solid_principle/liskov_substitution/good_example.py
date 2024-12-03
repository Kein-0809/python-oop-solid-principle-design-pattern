from abc import ABCMeta, abstractmethod

# インターフェース
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def get_area(self) -> int:
        pass


# 具象クラス
# Rectangle implements Shape
class Rectangle(Shape):
    def __init__(self):
        self.__width = 0
        self.__height = 0

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    # インターフェースの内容(抽象メソッドであるget_area)を実装している
    def get_area(self) -> int:
        return self.width * self.height


# 具象クラス
# Square implements Shape
class Square(Shape):
    def __init__(self):
        self.__length = 0

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    # インターフェースの内容(抽象メソッドであるget_area)を実装している
    def get_area(self) -> int:
        return self.__length**2


# DIパターン
# 共通の抽象クラスまたはインターフェースを引数に取る(依存性注入)している
def f(shape: Shape):
    print(shape.get_area())


if __name__ == "__main__":
    r1 = Rectangle()
    r1.width = 3
    r1.height = 4
    f(r1)

    r2 = Square()
    r2.length = 3
    f(r2)
