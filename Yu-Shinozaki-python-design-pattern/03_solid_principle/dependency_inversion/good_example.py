from abc import ABCMeta, abstractmethod


class User:
    pass

# インターフェース
class IUserService(metaclass=ABCMeta):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> User:
        pass

# 具象クラス
# UserControllerはIUserServiceに依存している(使用している)
# UserControllerはIUserServiceを実装しているクラスを使用することができる
class UserController:
    def __init__(self, user_service: IUserService):
        self.__user_service = user_service

    def create(self, user: User) -> User:
        return self.__user_service.create(user)

    def find_by_id(self, id: str) -> User:
        return self.__user_service.find_by_id(id)


# インターフェース
class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> User:
        pass

# 具象クラス
# UserService implements IUserService
# UserServiceはIUserServiceの抽象メソッドの中身を実装している(定義している)
# UserServiceはIUserRepositoryに依存している(使用している)
# UserServiceはIUserRepositoryを実装しているクラスを使用することができる
class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository

    def create(self, user: User) -> User:
        return self.__user_repository.create(user)

    def find_by_id(self, id: str) -> User:
        return self.__user_repository.find_by_id(id)


# 具象クラス
# UserRdbRepository implements IUserRepository
# UserRdbRepositoryはIUserRepositoryの抽象メソッドの中身を実装している(定義している)
class UserRdbRepository(IUserRepository):
    def create(self, user: User) -> User:
        print("RDBにUserを登録")
        return user

    def find_by_id(self, id: str) -> User:
        print(f"ID: {id}のユーザーを検索")
        return User()


# 具象クラス
class TestRepository(IUserRepository):
    def create(self, user: User) -> User:
        print("RDBにUserを登録")
        return user

    def find_by_id(self, id: str) -> User:
        print(f"Test ID: {id}のユーザーを検索")
        return User()


if __name__ == "__main__":
    user_rdb_repository = UserRdbRepository()
    test_repository = TestRepository()
    # user_service = UserService(user_rdb_repository)
    user_service = UserService(test_repository) # IUserRepositoryを実装しているクラスを注入する(使用する)
    user_controller = UserController(user_service) # IUserServiceを実装しているクラスを注入する(使用する)
    user_controller.find_by_id("123")
