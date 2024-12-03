from abc import ABCMeta, abstractmethod

# 抽象クラス
class Vehicle(metaclass=ABCMeta):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

# インターフェース
class Movable(metaclass=ABCMeta):
    # 抽象メソッド
    @abstractmethod
    def start(self):
        pass

    # 抽象メソッド
    @abstractmethod
    def stop(self):
        pass

# インターフェース
class Flyable(metaclass=ABCMeta):
    # 抽象メソッド
    @abstractmethod
    def fly(self):
        pass

# 具象クラス
# Airplane extends Vehicle implements Movable and Flyable
class Airplane(Vehicle, Movable, Flyable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    # インターフェースの内容(抽象メソッドであるstart)を実装している
    def start(self):
        print("start!")

    # インターフェースの内容(抽象メソッドであるstop)を実装している
    def stop(self):
        print("stop!")

    # インターフェースの内容(抽象メソッドであるfly)を実装している
    def fly(self):
        print("fly!")


# 具象クラス
# Car extends Vehicle implements Movable
class Car(Vehicle, Movable):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    # インターフェースの内容(抽象メソッドであるstart)を実装している
    def start(self):
        print("start!")

    # インターフェースの内容(抽象メソッドであるstop)を実装している
    def stop(self):
        print("stop!")


if __name__ == "__main__":
    v1 = Airplane("AirBus", "white")
    v2 = Car("Prius", "black")

    v1.fly()
    v2.start()
