import math
from abc import ABCMeta, abstractmethod

# 抽象クラス
class IEmployee(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.name = name

    # 抽象メソッド
    @abstractmethod
    def get_bonus(self, base: int) -> int:
        pass

# 具象クラス
# JuniorEmployee extends IEmployee
class JuniorEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.1)

# 具象クラス
# MiddleEmployee extends IEmployee
class MiddleEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 1.5)

# 具象クラス
# SeniorEmployee extends IEmployee
class SeniorEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 2)

# 具象クラス
# ExpertEmployee extends IEmployee
class ExpertEmployee(IEmployee):
    def __init__(self, name: str):
        super().__init__(name)

    def get_bonus(self, base: int) -> int:
        return math.floor(base * 3)


if __name__ == "__main__":
    emp1 = JuniorEmployee("Yamada")
    emp2 = MiddleEmployee("Suzuki")
    emp3 = SeniorEmployee("Tanaka")
    emp4 = ExpertEmployee("Bob")

    base = 100
    print(emp1.get_bonus(base))
    print(emp2.get_bonus(base))
    print(emp3.get_bonus(base))
    print(emp4.get_bonus(base))
