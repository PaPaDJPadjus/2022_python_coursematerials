"""Tests for week 8"""
from solution import students_study
from solution import lottery
from solution import fruit_order


def test_students_study_evening_always_true():
    """Test nightly study session times."""
    assert students_study(18, True) is True
    assert students_study(18, False) is True
    assert students_study(24, True) is True
    assert students_study(24, False) is True


def test_students_study_night_always_false():
    """Test if student is sleeping."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False


def test_students_study_day_false():
    """Test if student is awake and had coffee."""
    assert students_study(17, True) is True
    assert students_study(17, False) is False
    assert students_study(5, True) is True
    assert students_study(5, False) is False


def test_lottery_jackpot():
    """Test jackpot aka all 5."""
    assert lottery(5, 5, 5) == 10


def test_lottery_same_number_not_5():
    """Test if numbers are equal but not 5."""
    assert lottery(1, 1, 1) == 5
    assert lottery(4, 4, 4) == 5
    assert lottery(8, 8, 8) == 5


def test_lottery_all_different():
    """Test if numbers are different for mini prize."""
    assert lottery(1, 2, 3) == 1
    assert lottery(4, 1, 9) == 1
    assert lottery(0, 10, 1) == 1


def test_lottery_a_is_b_or_c_not_both():
    """Test if a is equal to b or c."""
    assert lottery(1, 1, 3) == 0
    assert lottery(0, 4, 0) == 0
    assert lottery(0, 1, 1) == 0
