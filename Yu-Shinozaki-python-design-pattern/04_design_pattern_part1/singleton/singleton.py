import datetime


class Logger:
    # Class variable (クラス変数)
    _instance = None

    # __new__は特殊メソッド(特殊メソッドはPythonの組み込みメソッド)
    # __new__インスタンスが作成される前に呼び出される、インスタンスを生成するメソッド
    # __init__はインスタンスが作成された後に呼び出される、インスタンスの初期化を行うメソッド
    def __new__(cls):
        # インスタンスが作成されていない場合はインスタンスを作成する (クラス変数にアクセスしている)
        if cls._instance is None:
            cls._instance = super().__new__(cls) # インスタンスを作成する
        return cls._instance # すでにインスタンスが作成されている場合はそのインスタンスを返す、作成されていない場合は作成したインスタンスを返す

    def output(self, content: str):
        now = datetime.datetime.now()
        print(f"{now}: {content}")


class Test:
    pass


if __name__ == "__main__":
    test1 = Test()
    test2 = Test()
    print("Test: ", test1 == test2)

    logger1 = Logger()
    logger2 = Logger()
    print("Singleton: ", logger1 == logger2)

    logger1.output("logger1のログ")
    logger2.output("logger2のログ")
