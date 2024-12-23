from abc import ABCMeta, abstractmethod

# 抽象クラス
class Vehicle(metaclass=ABCMeta):
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fly(self):
        pass


# 具象クラス
# Airplane extends Vehicle
class Airplane(Vehicle):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self):
        print("start!")

    def stop(self):
        print("stop!")

    def fly(self):
        print("fly!")


# 具象クラス
# Car extends Vehicle
class Car(Vehicle):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)

    def start(self):
        print("start!")

    def stop(self):
        print("stop!")

    def fly(self):
        raise Exception("Car can't fly!")


if __name__ == "__main__":
    v1: Vehicle = Airplane("AirBus", "white")
    v2: Vehicle = Car("Prius", "black")

    v1.fly()
    v2.fly()
