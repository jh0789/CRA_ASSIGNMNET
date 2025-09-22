from attendance import manage_attendance
from grade import GradeFactory, enumGrade


def test_input_file(capsys):
    # arrange
    expected_output = [
        "NAME : Umar, POINT : 48, GRADE : SILVER",
        "NAME : Daisy, POINT : 45, GRADE : SILVER",
        "NAME : Alice, POINT : 61, GRADE : GOLD",
        "NAME : Xena, POINT : 91, GRADE : GOLD",
        "NAME : Ian, POINT : 23, GRADE : NORMAL",
        "NAME : Hannah, POINT : 127, GRADE : GOLD",
        "NAME : Ethan, POINT : 44, GRADE : SILVER",
        "NAME : Vera, POINT : 22, GRADE : NORMAL",
        "NAME : Rachel, POINT : 54, GRADE : GOLD",
        "NAME : Charlie, POINT : 58, GRADE : GOLD",
        "NAME : Steve, POINT : 38, GRADE : SILVER",
        "NAME : Nina, POINT : 79, GRADE : GOLD",
        "NAME : Bob, POINT : 8, GRADE : NORMAL",
        "NAME : George, POINT : 42, GRADE : SILVER",
        "NAME : Quinn, POINT : 6, GRADE : NORMAL",
        "NAME : Tina, POINT : 24, GRADE : NORMAL",
        "NAME : Will, POINT : 36, GRADE : SILVER",
        "NAME : Oscar, POINT : 13, GRADE : NORMAL",
        "NAME : Zane, POINT : 1, GRADE : NORMAL",
        "",
        "Removed player",
        "==============",
        "Bob",
        "Zane",
        "",
    ]
    # act
    manage_attendance()
    output = capsys.readouterr().out.split('\n')

    # assert
    assert output == expected_output


def test_grade():
    # arrange
    gradeGold = GradeFactory.create_grade(50)
    gradeSilver = GradeFactory.create_grade(30)
    gradeNormal = GradeFactory.create_grade(20)
    # act
    enum_gold = gradeGold.get_grade()
    enum_silver = gradeSilver.get_grade()
    enum_normal = gradeNormal.get_grade()
    # assert
    assert enum_gold == enumGrade.gold
    assert enum_silver == enumGrade.silver
    assert enum_normal == enumGrade.normal
