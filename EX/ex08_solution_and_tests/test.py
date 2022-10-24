import pytest
from solution import students_study


def test_students_study_evening_always_true():
    """Test nightly study session times."""
    assert students_study(18, True) is True
    assert students_study(18, False) is True
    assert students_study(24, True) is True
    assert students_study(24, False) is True


def test_students_study_night_always_false():
    """Test if student is sleaping."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False
