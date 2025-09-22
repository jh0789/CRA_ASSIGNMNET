from abc import ABC, abstractmethod


class IPoint(ABC):
    @abstractmethod
    def add_daily_point(self, weekday: str):
        pass

    @abstractmethod
    def add_point(self, point:int):
        pass

    @abstractmethod
    def get_point(self):
        pass


POINT_RULE = {
    "monday": 1,
    "tuesday": 1,
    "wednesday": 3,
    "thursday": 1,
    "friday": 1,
    "saturday": 2,
    "sunday": 2,
}


class WednesdayPoint(IPoint):
    def __init__(self):
        self.point = 0

    def add_daily_point(self, weekday: str):
        self.point += POINT_RULE[weekday]

    def get_point(self):
        return self.point

    def add_point(self, point):
        self.point += point
