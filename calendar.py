import calendar

def print_yearly_calendar_no_exceptions(year):
    """
    Prints the calendar for all months of a given year.
    No explicit exception handling is used as the calendar module
    handles valid month inputs gracefully.
    """
    print(f"Calendar for the year {year}:\n")
    for month in range(1, 12):
        print(calendar.month(year, month))
        print("-" * 30)