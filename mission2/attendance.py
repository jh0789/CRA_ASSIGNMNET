from enum import IntEnum
from player import Player
from grade import GradeFactory

MAX_PLAYER = 100

THRESHOLD_BONUS = 9
BONUS_POINT = 10

player_list = {}
players = {}
total_player = 0

# dat[사용자ID][요일]
attendance_record = [[0] * MAX_PLAYER for _ in range(MAX_PLAYER)]


class Day(IntEnum):
    monday = 0
    tuesday = 1
    wednesday = 2
    thursday = 3
    friday = 4
    saturday = 5
    sunday = 6


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
        players[total_player] = Player(name, id)

    player_id = player_list[name]

    day = POINT_RULE[weekday]['day']
    attendance_record[player_id][day] += 1
    players[player_id].point += POINT_RULE[weekday]['point']

    if weekday == 'wednesday':
        players[player_id].attend_on_wednesday += 1
    elif weekday == 'saturday' or weekday == 'sunday':
        players[player_id].attend_on_weekend += 1


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for player_id in range(1, total_player + 1):
        if (players[player_id].grade not in (1, 2) and
                players[player_id].attend_on_wednesday == 0 and
                players[player_id].attend_on_weekend == 0):
            print(players[player_id].name)


def display_info(player_id: int):
    print(f"NAME : {players[player_id].name}, POINT : {players[player_id].point}, GRADE : ", end="")
    players[player_id].grade.print_grade()


def calc_bonus_point(player_id: int):
    if attendance_record[player_id][Day.wednesday] > THRESHOLD_BONUS:
        players[player_id].point += BONUS_POINT
    if attendance_record[player_id][Day.saturday] + attendance_record[player_id][Day.sunday] > THRESHOLD_BONUS:
        players[player_id].point += BONUS_POINT


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
            players[player_id].grade = GradeFactory.create_grade(players[player_id].point)
            display_info(player_id)

        print_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    manage_attendance()
