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

def test_fare_exactly_minimum_boundary():
    assert base_fare("SL", 50) == 50


def test_negative_distance():
    with pytest.raises(ValueError):
        base_fare("3A", -5)


def test_age_boundary_5():
    assert concession(5, "M", False) == 50


def test_age_boundary_12():
    assert concession(12, "F", False) == 50


def test_age_boundary_13():
    assert concession(13, "M", False) == 0


def test_age_boundary_59():
    assert concession(59, "F", False) == 0


def test_age_boundary_60_male():
    assert concession(60, "M", False) == 40


def test_tatkal_flag_for_child():
    assert concession(3, "M", True) == 0


def test_tatkal_charge_boundary_cap():
    assert tatkal_charge("SL", 4000) == 400


def test_tatkal_charge_boundary_floor():
    assert tatkal_charge("3A", 300) == 100
