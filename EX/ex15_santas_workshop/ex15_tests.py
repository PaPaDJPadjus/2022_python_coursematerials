"""Test for errors in attempt_two.py."""
import pytest
from attempt_two import NeededLists
from attempt_two import Child
from attempt_two import GiftDatabase


def test_if_reads_info_from_files_singular_name_in_each_list():
    """Feed files to code and see, if it reads the files into the correct lists."""
    result = Child().info_from_csv_files("test_nice_one.csv", "test_naughty_one.csv", "test_wish_list_one.csv")
    assert result[0][0].name == "Kati"
    assert result[0][1].name == "Mati"
    assert result[0][1].wishes == ['Cars', ' Money']
    assert result[0][0].wishes == ['Dolls', ' Money']


def test_if_same_person_on_both_lists_only_represent_naughty():
    """If someone is on both lists, remove them from the nice list and make them naughty."""
    result = Child().info_from_csv_files("nice_list_same_name.csv", "naughty_list_same_name.csv", "wish_list_same_names.csv")
    assert result[0][0].behaviour == "Naughty"
    assert result[0][1].behaviour == "Naughty"
    assert result[0][2].behaviour == "Naughty"
    assert result[0][3].behaviour == "Nice"
