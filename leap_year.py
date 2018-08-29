def is_leap(year):
    """Checks if a year is a leap year or not.

    A year is a leap year if the following conditions are met:
        1) the year is divisible by 4 AND 
        2) the year is not divisible by 100 but it is with 400

    Args: 
        year [int]: The year to calculate 

    Returns:
        leap [Bool]: If the year is a leap year or not.
    """
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    
print(is_leap(2100))