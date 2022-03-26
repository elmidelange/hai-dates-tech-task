import pytest
from dates.dates_utils import (
    check_format,
    count_leap_years,
    get_day_month_year,
    get_total_days,
    is_leap_year,
)


@pytest.mark.parametrize(
    "test_year,expected",
    [
        (2000, True),
        (2004, True),
        (2001, False),
        (1900, False),
    ],
)
def test_is_leap_year(test_year, expected):
    assert is_leap_year(test_year) == expected


@pytest.mark.parametrize(
    "test_input",
    [
        ("01-01-2020"),
        ("20000-01-01"),
        ("2022-02-29"),
        ("02022-02-22"),
        ("2022-002-22"),
        ("2022-02-022"),
        (20220222),
        ("2022-02-22T22:22:22"),
        ("2022-02-22-22:22:22"),
    ],
)
def test_check_format(test_input):
    with pytest.raises(ValueError):
        check_format(test_input)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("2012-01-10", (2012, 1, 10)),
        ("9999-12-31", (9999, 12, 31)),
        ("0001-01-01", (1, 1, 1)),
    ],
)
def test_get_day_month_year(test_input, expected):
    assert get_day_month_year(test_input) == expected


@pytest.mark.parametrize(
    "test_year,test_month,test_day,expected",
    [
        (2000, 3, 1, 485),  # 97 / 400 years are leap years in the Gregorian calendar
        (2000, 2, 1, 484),
    ],
)
def test_count_leap_years(test_year, test_month, test_day, expected):
    assert count_leap_years(test_year, test_month) == expected


@pytest.mark.parametrize(
    "test_year,test_month,test_day,expected",
    [
        (2022, 1, 1, 738521),
        (0, 1, 1, 1),
        (3999, 12, 31, 1460969),
    ],
)
def test_get_total_days(test_year, test_month, test_day, expected):
    assert get_total_days(test_year, test_month, test_day) == expected
