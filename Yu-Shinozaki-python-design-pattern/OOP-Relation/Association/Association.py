# 関連 (Association)

# クラス定義: カプセル化の原則に従う
class Student:
    # コンストラクタ: オブジェクトの初期化
    def __init__(self, name):
        # カプセル化: プライベート属性
        self._name = name
        self._teacher = None

    # カプセル化: プロパティデコレータを使用したゲッター
    @property
    def name(self):
        return self._name

    # カプセル化: プロパティデコレータを使用したセッター
    @name.setter
    def name(self, name):
        self._name = name

    # カプセル化: プロパティデコレータを使用したゲッター
    @property
    def teacher(self):
        return self._teacher

    # カプセル化: プロパティデコレータを使用したセッター
    @teacher.setter
    def teacher(self, teacher):
        self._teacher = teacher


# クラス定義: カプセル化の原則に従う
class Teacher:
    # コンストラクタ: オブジェクトの初期化
    def __init__(self, name):
        # カプセル化: プライベート属性
        self._name = name
        self._students = []

    # カプセル化: プロパティデコレータを使用したゲッター
    @property
    def name(self):
        return self._name

    # カプセル化: プロパティデコレータを使用したセッター
    @name.setter
    def name(self, name):
        self._name = name

    # メソッド: 関連性を管理
    def add_student(self, student):
        self._students.append(student)
        student.teacher = self

    # カプセル化: プロパティデコレータを使用したゲッター
    @property
    def students(self):
        return self._students


# クライアントコード: オブジェクトの使用例
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