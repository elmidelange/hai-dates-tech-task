from app.date_utils import check_format, get_day_month_year, get_total_days


def date_diff(date1: str, date2: str) -> int:
    """Returns the days difference between two dates.

    Args:
        date1 (str): The first date with format YYYY-MM-DD.
        date2 (str): The second date with format YYYY-MM-DD.

    Returns:
        int: Number of days difference
    """

    # Check for valid input format
    check_format(date_str=date1)
    check_format(date_str=date2)

    # Extract the year, month and day values
    y1, m1, d1 = get_day_month_year(date1)
    y2, m2, d2 = get_day_month_year(date2)

    # Get the total days since 0000-00-00
    total1 = get_total_days(year=y1, month=m1, day=d1)
    total2 = get_total_days(year=y2, month=m2, day=d2)

    # Get the absolute difference between the two dates
    diff = total2 - total1
    abs_diff = int((diff**2) ** (0.5))

    # Exclude the input dates by subtracting a day
    return abs_diff - 1
