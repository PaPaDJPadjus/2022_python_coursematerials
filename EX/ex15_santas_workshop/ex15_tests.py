"""Test for errors in attempt_two.py."""
import pytest
from attempt_two import GiftDatabase


def test_if_reads_info_from_files_singular_name_in_each_list():
    """Feed files to code and see, if it reads the files into the correct lists."""
    result = GiftDatabase().info_from_csv_files("test_nice_one.csv", "test_naughty_one.csv", "test_wish_list_one.csv")
    assert result[0].name == "Kati"
    assert result[1].name == "Mati"
    assert result[1].wishes == ['Cars', 'Money']
    assert result[0].wishes == ['Dolls', 'Money']


def test_if_same_person_on_both_lists_only_represent_naughty():
    """If someone is on both lists, remove them from the nice list and make them naughty."""
    gifts = GiftDatabase()
    result = gifts.info_from_csv_files("nice_list_same_name.csv", "naughty_list_same_name.csv", "wish_list_same_names.csv")
    assert result[0].behaviour == "Naughty"
    assert result[1].behaviour == "Naughty"
    assert result[2].behaviour == "Naughty"
    assert result[3].behaviour == "Nice"


def test_if_gets_gift_info():
    """Test getting gift info if it doesn't have it."""
    gifts = GiftDatabase()
    result_one = gifts.get_gift("Small watering can")
    result_two = gifts.get_gift("Pink tricycle")
    assert result_one == {'gift': 'Small watering can', 'material_cost': 7, 'production_time': 2, 'weight_in_grams': 540}
    assert result_two == {'gift': 'Pink tricycle', 'material_cost': 159, 'production_time': 8, 'weight_in_grams': 5400}


def test_incorrect_wish():
    """If the item doesn't exist, should fail."""
    gifts = GiftDatabase()
    result = gifts.get_gift("Girlfriend")
    assert result == {'message': 'Gift not found! Did you forget to supply the name of the gift as a query parameter?'}


def test_when_nice_list_empty():
    """Test code for circumstance of no nice list."""
    gifts = GiftDatabase()
    result = gifts.info_from_csv_files("empty.csv", "naughty_list_same_name.csv", "wish_list_same_names.csv")
    assert len(result) == 3


def test_when_naughty_list_empty():
    """Test code for circumstance of no naughty list."""
    gifts = GiftDatabase()
    result = gifts.info_from_csv_files("nice_list_same_name.csv", "empty.csv", "wish_list_same_names.csv")
    assert len(result) == 2


def test_when_wish_list_empty():
    """Test code for circumstance of no wishlist."""
    gifts = GiftDatabase()
    gifts.info_from_csv_files("nice_list_same_name.csv", "naughty_list_same_name.csv", "empty.csv")
    result = gifts.get_needed_gifts_for_children()
    assert result == ['3 pieces of coal']
