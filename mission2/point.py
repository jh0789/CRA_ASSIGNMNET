
POINT_RULE = {
    "monday": 1,
    "tuesday": 1,
    "wednesday": 3,
    "thursday": 1,
    "friday": 1,
    "saturday": 2,
    "sunday": 2,
}

class Point:
    def __init__(self):
        self.point = 0

    def add_weekday_point(self, weekday: str):
        self.point += POINT_RULE[weekday]

    def get_point(self):
        return self.point

    def add_point(self, point):
        self.point += point
