# Write a program that counts the number of sundays in the month of october. Assume that Oct starts on Tuesday
def sunday_count():
    start_day = 2
    sunday = 0

    for day in range(1, 32):
        if (start_day+day-1) % 7 == 0:
            sunday += 1

    return sunday


print("The number of Sundays in October =", sunday_count())
