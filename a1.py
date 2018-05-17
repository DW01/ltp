# Assignment 1 (a1.py).
"""This module is for the first major assignment of UofT's LTC course."""

# These first four functions operate on seconds to retrieve
# various forms of time.

def seconds_difference(time_1, time_2):
    """(number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0"""

    return time_2 - time_1

def hours_difference(time_1, time_2):
    """(number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.

    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0"""

    return seconds_difference(time_1, time_2) / 3600

def to_float_hours(hours, minutes, seconds):
    """(int, int, int) -> float
    Return hours as a float from three integers.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01"""

    hours_total = hours

    if minutes >= 0 & minutes < 60:
        minutes_total = minutes / 60
        if seconds >= 0 & seconds < 60:
            seconds_total = seconds / 3600
            return hours_total + minutes_total + seconds_total
        else:
            return "seconds must be zero or higher but lower than 60!"
    else:
        return "minutes must be zero or higher but lower than 60!"

def to_24_hour_clock(hours):
    """(number) -> number
    Converts a 12-hour time to a 24-hour time if hours is zero or higher.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5"""

    return hours % 24

# The next three functions get the number of hours,
# minutes and seconds that have passed since midnight.

def get_hours(seconds):
    """(int) -> int

    Return the number of hours that have
    elapsed since midnight, as seen on a 24-hour clock

    >>> get_hours(7400)
    2"""

    # Is seconds greater than zero?
    if seconds >= 0:
        return int(to_24_hour_clock(seconds / 3600))
    else:
        return "seconds must be greater than zero!"

def get_minutes(seconds):
    """(int) -> int

    Return the number of minutes that have
    elapsed since midnight, as seen on a 24-hour clock

    >>> get_minutes(7400)
    3"""

    # Is seconds greater than zero?
    if seconds >= 0:
        total_seconds = int((seconds % 3600) / 60)
        return int(total_seconds)
    else:
        return "seconds must be greater than zero!"

def get_seconds(seconds):
    """(int) -> int

    Return the number of seconds that have
    elapsed since midnight, as seen on a 24-hour clock

    >>> get_seconds(7400)
    20"""

    # Is seconds greater than zero?
    if seconds >= 0:
        total_seconds = int((seconds % 3600) % 60)
        return int(total_seconds)
    else:
        return "seconds must be greater than zero!"

# These last two functions determine time to and from UTC,
# or, more accurately, Coordinated Universal Time.

def time_to_utc(offset, clock_time):
    """ (number, float) -> float
    Return time at UTC+0, where [offset] is the number of hours away from
    UTC+0.
    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """

    return to_24_hour_clock(clock_time - offset)

def time_from_utc(offset, clock_time):
    """ (number, float) -> float
    Return UTC time in time zone [offset].
    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """

    return to_24_hour_clock(clock_time + offset)
