# 実現 (Realization)

from abc import ABC, abstractmethod

# インターフェース: Pet
class Pet(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# クラス: Dog (Petを実現)
class Dog(Pet):
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is playing fetch!"

    def eat(self):
        return f"{self.name} is eating dog food!"

# クラス: Cat (Petを実現)
class Cat(Pet):
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is playing with a ball of yarn!"

    def eat(self):
        return f"{self.name} is eating cat food!"

# 使用例
if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Kitty")

    # インターフェースを通じて振る舞いを呼び出す
    print(dog.play())
    print(dog.eat())

    print(cat.play())
    print(cat.eat())
