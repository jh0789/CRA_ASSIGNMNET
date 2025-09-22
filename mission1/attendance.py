from enum import IntEnum

THRESHOLD_SILVER_GRADE = 30
THRESHOLD_GOLD_GRADE = 50
THRESHOLD_BONUS = 9
BONUS_POINT = 10

player_list = {}
total_player = 0

# dat[사용자ID][요일]
attendance_record = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
attend_on_wednesday = [0] * 100
attend_on_weekend = [0] * 100


class Day(IntEnum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6


class Grade(IntEnum):
    gold = 1
    silver = 2
    normal = 0


POINT_RULE = {
    "monday": {"day": Day.monday, "point": 1},
    "tuesday": {"day": Day.tuesday, "point": 1},
    "wednesday": {"day": Day.wednesday, "point": 3},
    "thursday": {"day": Day.thursday, "point": 1},
    "friday": {"day": Day.friday, "point": 1},
    "saturday": {"day": Day.saturday, "point": 2},
    "sunday": {"day": Day.sunday, "point": 2},
}


def calc_score(name, weekday):
    global total_player

    if name not in player_list:
        total_player += 1
        player_list[name] = total_player
        names[total_player] = name

    player_id = player_list[name]

    day = POINT_RULE[weekday]['day']
    attendance_record[player_id][day] += 1
    points[player_id] += POINT_RULE[weekday]['point']

    if weekday == 'wednesday':
        attend_on_wednesday[player_id] += 1
    elif weekday == 'saturday' or weekday == 'sunday':
        attend_on_weekend[player_id] += 1


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, total_player + 1):
        if grade[i] not in (1, 2) and attend_on_wednesday[i] == 0 and attend_on_weekend[i] == 0:
            print(names[i])


def display_info(player_id: int):
    print(f"NAME : {names[player_id]}, POINT : {points[player_id]}, GRADE : ", end="")
    if grade[player_id] == Grade.gold:
        print("GOLD")
    elif grade[player_id] == Grade.silver:
        print("SILVER")
    else:
        print("NORMAL")


def assign_grade(player_id):
    if points[player_id] >= THRESHOLD_GOLD_GRADE:
        grade[player_id] = Grade.gold
    elif points[player_id] >= THRESHOLD_SILVER_GRADE:
        grade[player_id] = Grade.silver
    else:
        grade[player_id] = Grade.normal


def calc_bonus_point(player_id: int):
    if attendance_record[player_id][Day.wednesday] > THRESHOLD_BONUS:
        points[player_id] += BONUS_POINT
    if attendance_record[player_id][Day.saturday] + attendance_record[player_id][Day.sunday] > THRESHOLD_BONUS:
        points[player_id] += BONUS_POINT


def manage_attendance():
    try:
        with open("attendance_weekday_500.txt", encoding='utf-8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                file_input = line.strip().split()
                if len(file_input) == 2:
                    calc_score(file_input[0], file_input[1])

        for player_id in range(1, total_player + 1):
            calc_bonus_point(player_id)
            assign_grade(player_id)
            display_info(player_id)

        print_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    manage_attendance()
