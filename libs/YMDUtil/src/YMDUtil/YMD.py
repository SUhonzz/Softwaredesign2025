#Leap year is a year thats divisible by 4 but not 100 OR divisible by 400
def isLeapYear(year :int) -> bool:

    """Determine whether a year is a Gregorian leap year.

    Args:
        year (int): Year number (e.g., 2024).

    Returns:
        bool: True if leap year, otherwise False.

    Examples:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
    """
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else:
        return False
    
#Algorithm to calculate day of the week for a given date
def dayOfWeek(day: int, month: int, year: int) -> str:
    """Calculate the day of the week for a given date using a specific algorithm."""
    if year < 1753:
        return "Algorithm does not work for years before 1753"
    
    month_values = { #Month number values as per algorithm
        1: 1,
        2: 4,
        3: 4,
        4: 0,
        5: 2,
        6: 5,
        7: 0,
        8: 3,
        9: 6,
        10: 1,
        11: 4,
        12: 6
    }

    day_values = { # Day of week values as per algorithm
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        0: "Saturday"
    }

    last_two_digits = year % 100
    step1 = int(last_two_digits * 1.25)
    step2 = step1 + day + month_values[month]
    if isLeapYear(year) and (month == 1 or month == 2):
        step2 -= 1
    if year < 1900:
        step2 += 2
    if year < 1800:
        step2 += 2
    if year > 2000 and year <= 2100:
        step2 -= 1

    result = day_values[step2 % 7]
    return result



# Calculate week number for a given date
def calcWeekNr (day: int, month: int, year: int) -> int:
    """Calculate the week number for a given date."""
    # Month offsets for week number calculation

    # Calculate day of year
    day_of_year = day
    for m in range(1, month):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            day_of_year += 31
        elif m in [4, 6, 9, 11]:
            day_of_year += 30
        elif m == 2:
            day_of_year += 29 if isLeapYear(year) else 28

    # Calculate week number
    week_number = (day_of_year // 7)
    return week_number