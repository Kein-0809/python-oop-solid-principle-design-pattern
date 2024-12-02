# 一般化 (Generalization)

from abc import ABC, abstractmethod  # 抽象クラスと抽象メソッドのサポート

# 抽象クラス: Animal (直接インスタンス化されない)
class Animal(ABC):
    def __init__(self, name):
        self._name = name  # プライベート変数 (カプセル化)

    # ゲッターとセッター
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # 抽象メソッド: speak (子クラスで実装が必要)
    @abstractmethod
    def speak(self):
        pass

# 子クラス: Dog (Animalを継承)
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"  # 抽象メソッドの実装

# 子クラス: Cat (Animalを継承)
class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"  # 抽象メソッドの実装

# 使用例
if __name__ == "__main__":
    # Dog と Cat のインスタンスを作成
    dog = Dog("Buddy")
    cat = Cat("Kitty")

    # オーバーライドされたメソッドの実行
    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")
