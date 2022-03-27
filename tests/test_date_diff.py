from dates.date_diff import date_diff


def test_no_days_diff():
    assert date_diff(date1="2012-01-10", date2="2012-01-11") == 0


def test_same_month():
    assert date_diff(date1="2012-01-01", date2="2012-01-10") == 8


def test_different_month():
    assert date_diff(date1="1801-06-13", date2="1801-11-11") == 150


def test_different_year():
    assert date_diff(date1="2017-12-14", date2="2021-12-01") == 1447


def test_reverse_dates():
    assert date_diff(date1="2021-12-01", date2="2017-12-14") == 1447
