"""Dates utilities file
"""

from typing import Tuple

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def check_format(date_str: str) -> None:
    """Checks the format of the date string is valid (YYYY-MM-DD)

    Args:
        date (str): Date string
    """

    if not isinstance(date_str, str):
        raise ValueError(f"Date must be a string for input {date_str}")

    date_parts = date_str.split("-")

    if len(date_parts) != 3:
        raise ValueError(f"Date must be in YYYY-MM-DD format for input {date_str}")

    if not all(x.isdigit() for x in date_parts):
        raise ValueError(f"Date must only contain numbers for input {date_str}")

    year, month, day = tuple(int(x) for x in date_parts)

    if not 0 <= year <= 9999 or not len(date_parts[0]) == 4:
        raise ValueError(f"Year value must be of format YYYY for input {date_str}")

    if not 1 <= month <= 12 or not len(date_parts[1]) == 2:
        raise ValueError(
            f"Month value must be of format MM and be between 1 and 12 for input {date_str}"
        )

    if not 0 <= day <= 31 or not len(date_parts[2]) == 2:
        raise ValueError(
            f"Day value must be of format DD and be between 1 and 31 for input {date_str}"
        )

    if (is_leap_year(year) is False) and (month == 2) and (day == 29):
        raise ValueError(
            f"YYYY-02-29 is only valid on a leap year for input {date_str}"
        )


def is_leap_year(year: int) -> bool:
    """Checks if year is a leap year.

    ASSUMPTION: To be a leap year, the year number must be divisible by four,
                except for end-of-century years, which must be divisible by 400.

    Args:
        year (int): Year

    Returns:
        bool: Is leap year or not
    """
    # Check if century year and divisble by 400
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    # Check non-century year and divisible by 4
    if (year % 4 == 0) and (year % 100 != 0):
        return True

    return False


def get_day_month_year(date_str: str) -> Tuple[int, ...]:
    """Returns the day, month and year for a given date string in YYYY-MM-DD format

    Args:
        date_str (str): Date string in YYYY-MM-DD format

    Returns:
        Tuple[int, int, int]: Year, month and day values
    """
    return tuple(int(x) for x in date_str.split("-"))


def get_total_days(year: int, month: int, day: int) -> int:
    """Returns the total number of days in a date since 0001-01-01

    Args:
        day (int): Day value
        month (int): Month Value
        year (int): Year value

    Returns:
        int: Total number of days
    """
    # initialize count using years and day
    num_days = year * 365 + day

    # Add days for months in given date
    for i in range(0, month - 1):
        num_days += month_days[i]

    # Add a day for every leap year where there are 366 days
    num_days += count_leap_years(year, month)

    return num_days


def count_leap_years(year: int, month: int) -> int:
    """Returns the number of extra days incurred from leap years for a given date

    Args:
        year (int): Year value
        month (int): Month value
        day (int): Day value

    Returns:
        int: Number of leap years
    """
    # Check if the current year needs to be considered
    total_years = year
    if month <= 2:
        total_years -= 1

    # A leap year is a multiple of 4 or 400 (not 100)
    return int(total_years / 4) - int(total_years / 100) + int(total_years / 400)
