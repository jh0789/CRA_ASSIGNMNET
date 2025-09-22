from grade import GradeFactory, IGrade
from mission2.grade import NormalGrade, SilverGrade

THRESHOLD_BONUS = 9
BONUS_POINT = 10

class Player:
    def __init__(self, name, player_id):
        self.player_id = player_id
        self.name = name
        self.point = 0
        self.grade = NormalGrade()
        self.attend_on_wednesday = 0
        self.attend_on_weekend = 0

    def print_info(self):
        print(f"NAME : {self.name}, POINT : {self.point}, GRADE : ", end="")
        self.grade.print_grade()

    def get_grade(self):
        self.grade = GradeFactory.create_grade(self.point)

    def calc_bonus_point(self, attend_wed, attend_weekend):
        if attend_wed > THRESHOLD_BONUS:
            self.point += BONUS_POINT
        if attend_weekend > THRESHOLD_BONUS:
            self.point += BONUS_POINT


