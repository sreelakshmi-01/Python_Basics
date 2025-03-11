#Write a function to count how many weekends (Sat & Sun) are there in a given month that starts on a particular weekday.

def weekend_count(tot_days, start_day):
    weekend_day = 0
    for i in range (1, tot_days+1):
        current_day = (start_day + i - 1) % 7
        if current_day == 5 or current_day == 6:
            weekend_day += 1
    return weekend_day


s = int(input("Enter an number assuming 0 for monday and so on: "))
t = int(input("Enter the total days in the month: "))
print("Number of weekdays in the month: ", weekend_count(t, s))
