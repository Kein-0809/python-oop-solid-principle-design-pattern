# 継承を使用したアダプターパターン

from abc import ABCMeta, abstractmethod

# インターフェース
class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass

# Adaptee
class NewLibrary:
    def get_json_data(self) -> list[dict[str, str]]:
        return [
            {
                "data1": "json_dataA",
                "data2": "json_dataB",
            },
            {
                "data1": "json_dataC",
                "data2": "json_dataD",
            },
        ]

# 具象クラス
# JsonToCsvAdapter extends NewLibrary and implements Target
# NewLibraryを継承しているのでNewLibraryのメソッドを使用することができる
# Adapter
class JsonToCsvAdapter(NewLibrary, Target):
    # JsonToCsvAdapterがインスタンス化されるときに暗黙的(自動的)にNewLibraryのインスタンスが生成される
    # つまり、継承をしていることでNewLibraryのインスタンスを使用することができる
    # このように、継承を使用したアダプターパターンはNewLibraryのインスタンスを生成する必要がない
    # def __init__(self):
    #     self.new_library = NewLibrary()
    
    def get_csv_data(self) -> str:
        # 継承元のNewLibraryのメソッドを使用してJSONデータを取得する
        json_data = self.get_json_data()

        header = ",".join(list(json_data[0].keys())) + "\n"
        body = "\n".join([",".join(list(d.values())) for d in json_data])

        return header + body

# Client
if __name__ == "__main__":
    # NewLibraryのインスタンスを生成する
    adaptee = NewLibrary()
    print("=== Adapteeが提供するデータ ===")
    print(adaptee.get_json_data())

    print("")

    # JsonToCsvAdapterのインスタンスを生成する
    adapter = JsonToCsvAdapter()
    print("=== Adapterに変換されたデータ ===")
    print(adapter.get_csv_data())
