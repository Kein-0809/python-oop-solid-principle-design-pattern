# 誘導可能性 (Navigability interactively)

# 基本クラス: Student (カプセル化とプロパティの実装)
class Student:
    # コンストラクタ (初期化とカプセル化)
    def __init__(self, name):
        self._name = name  # プライベート変数
        self._teacher = None  # 双方向関連のための参照

    # プロパティデコレータ (カプセル化のためのゲッター)
    @property
    def name(self):
        return self._name

    # プロパティセッター (カプセル化のためのセッター)
    @name.setter
    def name(self, name):
        self._name = name

    # 双方向関連のためのプロパティ (カプセル化)
    @property
    def teacher(self):
        return self._teacher

    # 双方向関連のためのセッター
    @teacher.setter
    def teacher(self, teacher):
        self._teacher = teacher


# 基本クラス: Teacher (カプセル化とコレクション管理)
class Teacher:
    # コンストラクタ (初期化とカプセル化)
    def __init__(self, name):
        self._name = name  # プライベート変数
        self._students = []  # コレクション: 関連するStudentオブジェクトのリスト

    # プロパティデコレータ (カプセル化のためのゲッター)
    @property
    def name(self):
        return self._name

    # プロパティセッター (カプセル化のためのセッター)
    @name.setter
    def name(self, name):
        self._name = name

    # 双方向関連を管理するメソッド
    def add_student(self, student):
        self._students.append(student)  # コレクションへの追加
        student.teacher = self  # 双方向関連の維持

    # コレクションへのアクセスを制御するプロパティ (カプセル化)
    @property
    def students(self):
        return self._students


# 使用例: クラス間の双方向関連のデモンストレーション
teacher = Teacher("Mr. Smith")
student1 = Student("Alice")
student2 = Student("Bob")

# 双方向関連の確立
teacher.add_student(student1)
teacher.add_student(student2)

# 双方向関連の確認
print(f"{teacher.name} teaches:")
for student in teacher.students:
    print(f"- {student.name}")

# 逆方向の関連確認
print(f"{student1.name} is taught by {student1.teacher.name}")