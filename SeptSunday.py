# Write a program that counts the number of Sundays in the month of September 2024, assuming September starts on a Monday.

def sun_count():
    start_day = 1
    sunday = 0
    totdays = 30
    for days in range(1, totdays+1):
        if (start_day + days - 1) % 7 == 0:
            sunday += 1
    print("Number of Sundays in the September is ", sunday)


sun_count()
