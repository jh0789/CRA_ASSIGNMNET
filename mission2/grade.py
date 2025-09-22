from enum import IntEnum
from abc import ABC, abstractmethod

THRESHOLD_SILVER_GRADE = 30
THRESHOLD_GOLD_GRADE = 50


class enumGrade(IntEnum):
    gold = 1
    silver = 2
    normal = 0

class IGrade(ABC):
    @abstractmethod
    def get_grade(self):
        pass
    @abstractmethod
    def print_grade(self):
        pass

class GoldGrade(IGrade):
    def get_grade(self):
        return enumGrade.gold
    def print_grade(self):
        print("GOLD")


class SilverGrade(IGrade):
    def get_grade(self):
        return enumGrade.silver
    def print_grade(self):
        print("SILVER")

class NormalGrade(IGrade):
    def get_grade(self):
        return enumGrade.normal
    def print_grade(self):
        print("NORMAL")

class GradeFactory:
    @staticmethod
    def create_grade(point:int) -> IGrade:
        if point >= THRESHOLD_GOLD_GRADE:
            return GoldGrade()
        elif point >= THRESHOLD_SILVER_GRADE:
            return SilverGrade()
        else:
            return NormalGrade()
