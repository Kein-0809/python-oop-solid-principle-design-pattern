# クラス図 演習1
class Employee:
    def __init__(self, emp_id: int, name: str, salary: int):
        self.__emp_id = emp_id  # プライベート変数
        self.__name = name  # プライベート変数
        self.__salary = salary  # プライベート変数

    # プロテクトメソッド
    def _work(self) -> None:
        print("働きます")


    # def get_salary(self) -> int:
    #     return self.__salary

    # Setter
    # def set_salary(self, salary: int) -> None:
    #     self.__salary = salary

    # Getter
    @property
    def salary(self) -> int:
        return self.__salary

    # Setter
    @salary.setter
    def salary(self, salary: int) -> None:
        self.__salary = salary
