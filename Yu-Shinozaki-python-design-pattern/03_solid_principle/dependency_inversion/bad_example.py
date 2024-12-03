# Dependency Inversion Principle
# 抽象クラスまたはインターフェースを引数に取る(依存性注入)している

class User:
    pass

# Dependency
# UserController uses UserService temporarily
class UserController:
    def __init__(self):
        # プライベート変数
        self.__user_service = UserService()

    def create(self, user: User) -> User:
        return self.__user_service.create(user)

    def find_by_id(self, id: str) -> User:
        return self.__user_service.find_by_id(id)


# Dependency
# UserService uses UserRdbRepository temporarily
class UserService:
    def __init__(self):
        # プライベート変数
        self.__user_repository = UserRdbRepository()

    def create(self, user: User) -> User:
        return self.__user_repository.create(user)

    def find_by_id(self, id: str) -> User:
        return self.__user_repository.find_by_id(id)



# Dependency
# UserRdbRepository is a concrete class (具象クラス)
class UserRdbRepository:
    def create(self, user: User) -> User:
        print("RDBにUserを登録")
        return user

    def find_by_id(self, id: str) -> User:
        print(f"ID: {id}のユーザーを検索")
        return User()


if __name__ == "__main__":
    user_controller = UserController()
    user_controller.find_by_id("123")
