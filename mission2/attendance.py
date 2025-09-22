from enum import IntEnum
from player import Player

MAX_PLAYER = 100

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


WEEKDAYS = {
    "monday": Day.monday,
    "tuesday": Day.tuesday,
    "wednesday": Day.wednesday,
    "thursday": Day.thursday,
    "friday": Day.friday,
    "saturday": Day.saturday,
    "sunday": Day.sunday,
}


def calc_score(name, weekday):
    global total_player

    if name not in player_list:
        total_player += 1
        player_list[name] = total_player
        players[total_player] = Player(name, id)

    player_id = player_list[name]

    players[player_id].point.add_weekday_point(weekday)
    players[player_id].check_special_day(weekday)

    attendance_record[player_id][WEEKDAYS[weekday]] += 1


def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for player_id in range(1, total_player + 1):
        if (players[player_id].grade not in (1, 2) and
                players[player_id].attend_on_wednesday == 0 and
                players[player_id].attend_on_weekend == 0):
            print(players[player_id].name)


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
            players[player_id].calc_bonus_point(attendance_record[player_id][Day.wednesday],
                                                attendance_record[player_id][Day.saturday] +
                                                attendance_record[player_id][Day.sunday])
            players[player_id].get_grade()
            players[player_id].print_info()

        print_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


if __name__ == "__main__":
    manage_attendance()
