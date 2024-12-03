from abc import ABCMeta, abstractmethod

# インターフェース
class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass


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
# JsonToCsvAdapter implements Target
# 委譲を使用したアダプターパターン (Delegation)
# NewLibraryのインスタンスをプライベート変数に格納している
class JsonToCsvAdapter(Target):
    def __init__(self, adaptee: NewLibrary):
        # JsonToCsvAdapterのインスタンス化時に引数として受け取るNewLibraryのインスタンスをプライベート変数に格納している
        # これにより、JsonToCsvAdapterのインスタンスがNewLibraryのインスタンスを使用することができる
        # JsonToCsvAdapterはインスタンス化時にNewLibraryのインスタンスを引数として注入する必要がある
        self.__adaptee = adaptee # プライベート変数

    def get_csv_data(self) -> str:
        json_data = self.__adaptee.get_json_data()

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

    # JsonToCsvAdapterのインスタンス化時にNewLibraryのインスタンス(adaptee)を引数として注入する
    adapter = JsonToCsvAdapter(adaptee)
    print("=== Adapterに変換されたデータ ===")
    print(adapter.get_csv_data())
