# 集約 (Aggregation)

# クラス: Player (部分)
class Player:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


# クラス: Team (全体)
class Team:
    def __init__(self, name):
        self._name = name
        self._players = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def add_player(self, player):
        self._players.append(player)

    @property
    def players(self):
        return self._players


# 使用例
if __name__ == "__main__":
    # 独立した Player インスタンスを作成
    player1 = Player("Alice")
    player2 = Player("Bob")

    # Team を作成して Player を追加
    team = Team("Dream Team")
    team.add_player(player1)
    team.add_player(player2)

    print(f"Team: {team.name}")
    for player in team.players:
        print(f"- Player: {player.name}")

    # Player は Team とは独立して存在可能
    print(f"Independent Player: {player1.name}")
