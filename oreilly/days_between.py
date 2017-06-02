from datetime import date, timedelta

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date_one = date(date1[0], date1[1], date1[2])
    date_two = date(date2[0], date2[1], date2[2])
    diff = date_one - date_two
    return abs(diff.days)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238