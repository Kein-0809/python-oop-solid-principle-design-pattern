# 誘導可能性 (Navigability one-way)

# 基本クラス: Student (カプセル化の実装)
class Student:
    # コンストラクタ (初期化)
    def __init__(self, name):
        self._name = name  # プライベート変数 (カプセル化)

    # プロパティデコレータ (カプセル化のためのゲッター)
    @property
    def name(self):
        return self._name

    # プロパティセッター (カプセル化のためのセッター)
    @name.setter
    def name(self, name):
        self._name = name


# 基本クラス: Teacher (カプセル化とコレクション管理)
class Teacher:
    # コンストラクタ (初期化)
    def __init__(self, name):
        self._name = name  # プライベート変数 (カプセル化)
        self._students = []  # コレクション: TeacherクラスがStudentクラスのリストを保持

    # プロパティデコレータ (カプセル化のためのゲッター)
    @property
    def name(self):
        return self._name

    # プロパティセッター (カプセル化のためのセッター)
    @name.setter
    def name(self, name):
        self._name = name

    # 関連を管理するメソッド (片方向の誘導可能性)
    def add_student(self, student):
        self._students.append(student)

    # プロパティデコレータ (カプセル化されたコレクションへのアクセス)
    @property
    def students(self):
        return self._students


# 使用例: クライアントコード
teacher = Teacher("Mr. Smith")
student1 = Student("Alice")
student2 = Student("Bob")

# オブジェクト間の関連付け
teacher.add_student(student1)
teacher.add_student(student2)

# 関連したオブジェクトの情報表示
print(f"{teacher.name} teaches:")
for student in teacher.students:
    print(f"- {student.name}")