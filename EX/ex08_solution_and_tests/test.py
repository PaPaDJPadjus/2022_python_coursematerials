"""Tests for week 8."""
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
    assert lottery(0, 0, 0) == 5
    assert lottery(-1, -1, -1) == 5


def test_lottery_all_different():
    """Test if numbers are different for mini prize."""
    assert lottery(1, 2, 3) == 1
    assert lottery(4, 1, 9) == 1
    assert lottery(0, 10, 1) == 1


def test_lottery_a_is_b_or_c_not_both():
    """Test if a is equal to b or c."""
    assert lottery(1, 1, 3) == 0
    assert lottery(0, 4, 0) == 0


def test_lottery_b_is_c_not_a():
    """Test if b and c are equal but don't equal a."""
    assert lottery(0, 1, 1) == 1


def test_fruit_order_examples():
    """Test examples given in docstring."""
    assert fruit_order(4, 1, 9) == 4
    assert fruit_order(3, 1, 10) == -1


def test_fruit_order_all_zero():
    """Test if all values are zero."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_order_no_big_baskets_possible():
    """Test possible answers if no big baskets."""
    assert fruit_order(4, 0, 3) == 3
    assert fruit_order(12, 0, 10) == 10
    assert fruit_order(1, 0, 1) == 1


def test_fruit_order_no_big_baskets_impossible():
    """Test impossible answers if no big baskets."""
    assert fruit_order(2, 0, 3) == -1
    assert fruit_order(4, 0, 12) == -1
    assert fruit_order(1, 0, 2) == -1


def test_fruit_order_no_small_baskets_possible():
    """Test possible answers if no small baskets."""
    assert fruit_order(0, 1, 5) == 0
    assert fruit_order(0, 2, 10) == 0
    assert fruit_order(0, 4, 20) == 0


def test_fruit_order_no_small_baskets_impossible():
    """Test impossible answers if no small baskets."""
    assert fruit_order(0, 1, 6) == -1
    assert fruit_order(0, 2, 7) == -1
    assert fruit_order(0, 4, 25) == -1


def test_fruit_order_only_need_big_baskets():
    """Test if is enough from just big baskets."""
    assert fruit_order(0, 2, 5) == 0
    assert fruit_order(0, 4, 20) == 0
    assert fruit_order(0, 1, 5) == 0


def test_fruit_order_not_enough_small():
    """Test if is not enough small baskets."""
    assert fruit_order(1, 1, 7) == -1
    assert fruit_order(3, 4, 25) == -1
    assert fruit_order(0, 1, 6) == -1


def test_fruit_order_all_big_some_small():
    """Test if possible to use all big and some small baskets."""
    assert fruit_order(5, 4, 25) == 5
    assert fruit_order(1, 1, 6) == 1


def test_fruit_order_some_big_some_small():
    """Test if possible to use some big and some small baskets."""
    assert fruit_order(5, 4, 21) == 1
    assert fruit_order(12, 3, 20) == 5


def test_fruit_order_some_big_all_small():
    """Test if possible to use all big and all small baskets."""
    assert fruit_order(1, 5, 21) == 1
    assert fruit_order(3, 3, 18) == 3


def test_fruit_order_only_small_not_enough_more_than_five():
    """Test if not enough small baskets if there's more than 5."""
    assert fruit_order(10, 2, 21) == -1
    assert fruit_order(6, 2, 18) == -1
