from abc import ABCMeta, abstractmethod

# 抽象クラス
# 基底クラス (Base Class)
class TestTemplate(metaclass=ABCMeta):
    def test(self):
        self.setup()
        self.execute()
        self.teardown()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def teardown(self):
        print("teardown")

# 具象クラス (Concrete Class)
# ItemServiceTest extends TestTemplate
class ItemServiceTest(TestTemplate):
    def setup(self):
        print("setup: ItemServiceTest")

    def execute(self):
        print("execute: ItemServiceTest")

# 具象クラス (Concrete Class)
# UserServiceTest extends TestTemplate
class UserServiceTest(TestTemplate):
    def setup(self):
        print("setup: UserServiceTest")

    def execute(self):
        print("execute: UserServiceTest")


if __name__ == "__main__":
    itemServiceTest = ItemServiceTest()
    userServiceTest = UserServiceTest()

    itemServiceTest.test()
    print("")
    userServiceTest.test()
