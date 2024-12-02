# 構成 (Composition)

# クラス: Room (部分)
class Room:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# クラス: House (全体)
class House:
    def __init__(self):
        self._rooms = []

    def add_room(self, room_name):
        # House の内部で Room インスタンスを管理
        self._rooms.append(Room(room_name))

    @property
    def rooms(self):
        return self._rooms


# 使用例
if __name__ == "__main__":
    # House を作成し、部屋を追加
    house = House()
    house.add_room("Living Room")
    house.add_room("Bedroom")

    print("House has rooms:")
    for room in house.rooms:
        print(f"- {room.name}")

    # House を破棄すると Room も破棄される
    del house  # 明示的に削除
