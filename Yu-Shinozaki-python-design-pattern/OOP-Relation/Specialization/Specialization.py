# 特化 (Specialization)

# 親クラス: Animal
class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # 共通メソッド
    def move(self):
        return f"{self._name} is moving!"

# 子クラス: Dog (特化)
class Dog(Animal):
    def bark(self):
        return f"{self.name} says: Woof!"

# 子クラス: Bird (特化)
class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying!"

# 使用例
if __name__ == "__main__":
    dog = Dog("Buddy")
    bird = Bird("Tweety")

    # 共通メソッド (move)
    print(dog.move())
    print(bird.move())

    # 特化されたメソッド (bark, fly)
    print(dog.bark())
    print(bird.fly())
