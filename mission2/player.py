from grade import GradeFactory
from mission2.grade import NormalGrade
from point import WednesdayPoint

THRESHOLD_BONUS = 9
BONUS_POINT = 10

class Player:
    def __init__(self, name, player_id):
        self.player_id = player_id
        self.name = name
        self.point = WednesdayPoint()
        self.grade = NormalGrade()
        self.attend_on_wednesday = 0
        self.attend_on_weekend = 0

    def print_info(self):
        print(f"NAME : {self.name}, POINT : {self.point.get_point()}, GRADE : ", end="")
        self.grade.print_grade()

    def get_grade(self):
        self.grade = GradeFactory.create_grade(self.point.get_point())

    def calc_bonus_point(self, attend_wed, attend_weekend):
        if attend_wed > THRESHOLD_BONUS:
            self.point.add_point(BONUS_POINT)
        if attend_weekend > THRESHOLD_BONUS:
            self.point.add_point(BONUS_POINT)

    def check_special_day(self, weekday):
        if weekday == 'wednesday':
            self.attend_on_wednesday += 1
        elif weekday == 'saturday' or weekday == 'sunday':
            self.attend_on_weekend += 1



