import pytest
from train_fare import base_fare, concession, tatkal_charge


def test_sleeper_fare():
    assert base_fare("SL", 500) == 500


def test_unknown_class():
    with pytest.raises(ValueError):
        base_fare("XX", 100)


def test_invalid_distance():
    with pytest.raises(ValueError):
        base_fare("SL", 0)


def test_minimum_fare():
    assert base_fare("SL", 10) == 50


def test_adult_no_concession():
    assert concession(30, "M", False) == 0


def test_tatkal_no_concession():
    assert concession(70, "F", True) == 0


def test_infant_concession():
    assert concession(3, "M", False) == 100


def test_child_concession():
    assert concession(10, "F", False) == 50


def test_senior_female_concession():
    assert concession(65, "F", False) == 50


def test_senior_male_concession():
    assert concession(65, "M", False) == 40


def test_tatkal_sleeper_charge():
    assert tatkal_charge("SL", 2000) == 200


def test_tatkal_ac_charge():
    assert tatkal_charge("3A", 500) == 150


def test_tatkal_max_cap():
    assert tatkal_charge("1A", 5000) == 400


def test_tatkal_min_floor():
    assert tatkal_charge("SL", 100) == 100