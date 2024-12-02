# クラス図 演習2
from abc import ABCMeta, abstractmethod

# インターフェース
class Shape(metaclass=ABCMeta):
    # 抽象メソッド
    @abstractmethod
    def calc_area(self) -> int:
        pass

# Rectangle implements Shape
class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.__width = width  # プライベート変数
        self.__height = height  # プライベート変数

    # 抽象メソッドの実装
    def calc_area(self) -> int:
        return self.__width * self.__height

# Square implements Shape
class Square(Shape):
    def __init__(self, length: int):
        self.__length = length  # プライベート変数

    # 抽象メソッドの実装
    def calc_area(self) -> int:
        return self.__length**2

# Client has a Shape ()
class Client:
    def __init__(self, shape: Shape):
        self.__shape = shape
