# 多重度 (Multiplicity)

# カプセル化を実現するクラス: Student
class Student:
    def __init__(self, name):
        self._name = name  # プライベート属性によるカプセル化
        self._teacher = None  # プライベート属性、多重度 0..1 を表現

    # プロパティデコレータによるカプセル化
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # プロパティデコレータによる関連の管理
    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        self._teacher = teacher


# カプセル化を実現するクラス: Teacher
class Teacher:
    def __init__(self, name):
        self._name = name  # プライベート属性によるカプセル化
        self._students = []  # プライベート属性、多重度 1..* を表現

    # プロパティデコレータによるカプセル化
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # 関連を管理するメソッド（カプセル化）
    def add_student(self, student):
        # データの整合性チェック
        if student.teacher:
            print(f"{student.name} is already assigned to another teacher.")
        else:
            self._students.append(student)
            student.teacher = self  # 双方向関連の維持

    # プロパティデコレータによる読み取り専用アクセス
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